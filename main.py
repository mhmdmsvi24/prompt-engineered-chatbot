from api import send_request
from config import Config

# DB is just an object that holds user sessions in a data structure, it's not an actual Database
# Using this the chatbot will keep track of the context or implementing chain of thought
from db import ChatDatabase
from utils import print_chat

# Initialize chat history database
db = ChatDatabase()

# Start the chat
print("Welcome to the chatbot! Type 'exit' to quit.\n")

while True:
    user_input = print_chat("user")

    if user_input.find("exit") != -1:
        break

    # Add user message to history
    db.add_message("user", user_input)

    # Get assistant response
    bot_response = send_request(db.get_history())

    if bot_response:
        db.add_message("assistant", bot_response)

        print_chat("assistant", bot_response)
