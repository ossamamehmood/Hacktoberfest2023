import nltk
from nltk.chat.util import Chat, reflections
import boto3
import logging

# Set up logging
logging.basicConfig(filename='chatbot.log', level=logging.INFO)

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I assist you with your cloud security tasks today?",]
    ],
    [
        r"quit",
        ["Bye. Stay secure!",]
    ],
    [
        r"security check",
        ["Performing security check...", aws_security_check]
    ],
]

def aws_security_check():
    try:
        # Use boto3 to interact with AWS API for security checks
        client = boto3.client('ec2')
        response = client.describe_security_groups()
        
        # Analyze the response and perform security checks
        # This is a placeholder - replace this with your actual security check logic
        insecure_groups = [group for group in response['SecurityGroups'] if 'insecure' in group['GroupName']]
        
        if insecure_groups:
            return "Warning: Found potentially insecure security groups: " + ', '.join([group['GroupName'] for group in insecure_groups])
        else:
            return "Security check complete. No insecure groups found."
    except Exception as e:
        logging.error("Error performing security check: " + str(e))
        return "Error performing security check. Please check the logs for more details."

def chatbot():
    print("Hi, I'm your cloud security assistant.")
    
    chat = Chat(pairs, reflections)
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            break
        
        responses = chat.respond(user_input)
        
        for response in responses:
            if callable(response):
                print(response())  # If the response is a function, call it
            else:
                print("ChatBot: " + response)

if __name__ == "__main__":
    chatbot()