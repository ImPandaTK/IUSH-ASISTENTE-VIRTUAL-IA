import requests
import os
from dotenv import load_dotenv

load_dotenv()

def obtener_clima(ciudad):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&lang=es&units=metric"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        descripcion = datos["weather"][0]["description"]
        temperatura = datos["main"]["temp"]
        return f"El clima en {ciudad} es {descripcion} con una temperatura de {temperatura}°C."
    else:
        return "No pude obtener el clima en este momento."