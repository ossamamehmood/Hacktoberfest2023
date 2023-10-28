
# Import necessary libraries and modules
import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Initialize the tokenizer and model for the DialoGPT chatbot
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Define the user function to handle user input and update the chat history
def user(message, history):
    # The user function simply adds the user's message to the chat history.
    return "", history + [[message, None]]

# Define the bot function to generate responses
def bot(history):
    # Retrieve the user's message from the chat history
    user_message = history[-1][0]
    
    # Encode the user's message and append it to the chat history
    new_user_input_ids = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")
    
    # Concatenate user input tokens with the chat history
    bot_input_ids = torch.cat([torch.LongTensor([]), new_user_input_ids], dim=-1)
    
    # Generate a response from the model
    response = model.generate(
        bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
    ).tolist()

    # Decode the response tokens and split them into dialogue lines
    response = tokenizer.decode(response[0]).split("")

    # Convert the response into a list of dialogue tuples
    response = [(response[i], response[i + 1]) for i in range(0, len(response) - 1, 2)]

    # Update the chat history with the bot's response
    history[-1] = response[0]
    
    # Return the updated chat history
    return history

# Create a Gradio Blocks interface for the chatbot
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.Button("Clear")

    # Define the user message submission and bot response behavior
    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(
        bot, chatbot, chatbot
    )

    # Define the behavior of the "Clear" button (currently set to do nothing)
    clear.click(lambda: None, None, chatbot, queue=False)

# Launch the Gradio interface for the chatbot
demo.launch()
