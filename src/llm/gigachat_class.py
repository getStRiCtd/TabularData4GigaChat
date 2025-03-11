import json
import asyncio
import aiohttp
import requests
import functools


from src.config import giga_config
from src.config import GigaAPI


def ahandle_exceptions(func):
    @functools.wraps(func)
    async def wrapper(self, *args, **kwargs):
        for _ in range(6):
            try:
                return await func(self, *args, **kwargs)
            except Exception as e:
                print(f"An error occurred in Giga Module, f: {func.__name__}, e: {e}")
                self.get_token()

    return wrapper


class GigaChat:
    """
    GigaChat interaction class

    Attributes
    ----------
    base_url: str
        token API link

    chat_url: str
        chat completion API link

    data: dict
        GigaChat scope

    prompt: str
        prompt to role GigaChat

    headers: dict
        token API authorization dict

    token: str
        GigaChat token

    Methods
    -------
    ask_giga()
        returns <str> GigaChat response
    """

    def __init__(self, headers=giga_config.requests_headers):
        self.base_url = GigaAPI.base_url
        self.chat_url = GigaAPI.chat_url
        self.embeddings_url = GigaAPI.embeddings_url
        self.data = {"scope": giga_config.GIGACHAT_SCOPE}
        self.prompt = "Привет"
        self.headers = headers
        self.token = None
        self.get_token()
        self.model = giga_config.GIGACHAT_MODEL

    def get_token(self):
        self.token = requests.post(
            self.base_url, headers=self.headers, data=self.data, verify=False
        ).json()['access_token']

    def __create_payload(self, text: str, prompt: str, model: str, temperature):
        pr = prompt
        payload = json.dumps(
            {
                "messages": [
                    {"role": "system", "content": pr},
                    {"role": "user", "content": text},
                ],
                "model": model,
                "profanity_check": False,
                "temperature": temperature,
            }
        )
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "accept": "application/json",
        }
        return payload, headers

    @ahandle_exceptions
    async def async_ask_giga(
        self, text, prompt, **kwargs) -> str:

        temperature = kwargs.get("temperature")
        payload, headers = self.__create_payload(
            text, prompt, self.model, temperature=temperature
        )
        connector = aiohttp.TCPConnector(ssl=False, limit=None)
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.post(
                f"{self.chat_url}chat/completions", headers=headers, data=payload
            ) as response:
                json_response = await response.json()
        return json_response["choices"][0]["message"]["content"]

