from config import Config


def print_chat(role, message=""):
    """Format and print chat messages clearly."""
    prefix = ""

    if role == "user":
        prefix = Config.user_color + "User: "
        message = input(f"{Config.user_color}You: {Config.text_color + ''}")
        return f"{prefix}{message}"
    else:
        prefix = Config.bot_color + "Assistant: "

    message = Config.text_color + message + "\n"

    print(f"{prefix}{message}")
    print(Config.reset_text)
