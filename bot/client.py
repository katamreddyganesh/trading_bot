import os
from binance.client import Client
from dotenv import load_dotenv

from pathlib import Path
load_dotenv(Path(__file__).resolve().parent.parent / "environment.env")


def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    return Client(api_key, api_secret, testnet=True)