import requests

from config import Config

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": Config.METIS_API_KEY,
}


def send_request(messages):
    """Send a chat request to Metis AI and return the assistant's response."""
    payload = {
        "model": Config.model,
        "messages": messages,
        "max_tokens": Config.max_tokens,
        "temperature": Config.temperature,
    }

    response = requests.post(Config.METIS_PROVIDER_URL, json=payload, headers=HEADERS)

    if response.status_code == 200:
        bot_response = response.json()
        return bot_response["choices"][0]["message"]["content"]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
