# Import necessary libraries
import gradio as gr  # Gradio for building the interface
from transformers import AutoModelForCausalLM, AutoTokenizer  # Hugging Face Transformers for the DialoGPT model
import torch  # PyTorch for tensor operations

# Load the DialoGPT tokenizer and model from Hugging Face's model hub
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Define a function for user input
def user(message, history):
    # This function takes a message and a history of the conversation so far as input.
    # It appends the user's message to the history.
    # Returns an empty string to clear the input field and updates the history.
    return "", history + [[message, None]]

# Define a function for the chatbot's response
def bot(history):
    # Extract the user's last message from the history
    user_message = history[-1][0]

    # Encode the user's message using the DialoGPT tokenizer and add the end-of-sequence token
    new_user_input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")

    # Append the new user input tokens to the chat history
    bot_input_ids = torch.cat([torch.LongTensor([]), new_user_input_ids], dim=-1)

    # Generate a response using the DialoGPT model
    response = model.generate(
        bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
    ).tolist()

    # Convert the generated tokens to text and split the responses into lines
    response = tokenizer.decode(response[0]).split("")

    # Organize the responses into pairs of (response, None)
    response = [
        (response[i], response[i + 1]) for i in range(0, len(response) - 1, 2)
    ]

    # Update the history with the bot's response
    history[-1] = response[0]

    # Return the updated history
    return history

# Create a Gradio interface using blocks
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    # When the user submits a message, call the user function first and then the bot function
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )

    # When the "Clear" button is clicked, do nothing (clears the input field)
    clear.click(lambda: None, None, chatbot, queue=False)

# Launch the Gradio interface
demo.launch()
