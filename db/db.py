class ChatDatabase:
    def __init__(self):
        self.history = [
            {
                "role": "system",
                "content": """You're an expert chatbot that aids users without prompt engineering\n
                konwledge to retrive the best response from you by asking them them enough\n
                information required for the task.\n

                You're equipped with knowledge of prompt engineering knowledge that will return the
                best output based on the situation.\n
                """,
            }
        ]

    def add_message(self, role, content):
        """Append user and assistant messages to chat history."""
        self.history.append({"role": role, "content": content})

    def get_history(self):
        """Return the chat history for sending to the API."""
        return self.history
