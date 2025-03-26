import os

from colorama import Fore, Style
from colorama import init as colorama_init
from dotenv import load_dotenv

load_dotenv()
colorama_init()


class Config:
    # metis api
    METIS_API_KEY = os.getenv("METIS_API_KEY")
    METIS_PROVIDER_URL = os.getenv("METIS_PROVIDER_URL")

    # colorama
    user_color = Fore.RED
    bot_color = Fore.BLUE
    text_color = Fore.WHITE
    reset_text = Style.RESET_ALL
