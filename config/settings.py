import os
import json
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def CARGAR_INTENTS():
    with open("data/intents.json", encoding="utf-8") as archivo:
        return json.load(archivo)

