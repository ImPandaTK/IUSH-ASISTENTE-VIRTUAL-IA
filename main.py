import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import json
import random
import openai

with open("API Key.txt", "r") as f:
    openai.api_key = f.read().strip()

def consultar_openai(pregunta):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": pregunta}],
            max_tokens=100,
            temperature=0.7,
        )
        return respuesta.choices[0].message["content"].strip()
    except Exception as e:
        return f"Lo siento, hubo un error al consultar la IA: {e}"


# Cargar datos de intenciones
with open("intents.json", "r", encoding='utf-8') as archivo:
    data = json.load(archivo)

# Configurar el motor de texto a voz
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    if "spanish" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break

"""def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
    try:
        texto = r.recognize_google(audio, language="es-CO")
        return texto.lower()
    except:
        return "No entendí"
"""

def hablar(texto):
    #Convierte texto a voz
    engine.say(texto)
    engine.runAndWait()


def detectar_intencion(texto):
    """Detecta la intención del texto ingresado."""
    mejor_coincidencia = {"tag": None, "similitud": 0}
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            similitud = fuzz.ratio(texto, pattern)
            if similitud > mejor_coincidencia["similitud"]:
                mejor_coincidencia = {"tag": intent["tag"], "similitud": similitud}
    # Considerar una intención válida si la similitud es mayor a un umbral (por ejemplo, 60)
    if mejor_coincidencia["similitud"] > 60:
        return mejor_coincidencia["tag"]
    return None

def ejecutar_accion(intent):
    """Ejecuta una acción basada en la intención detectada."""
    for intent_data in data["intents"]:
        if intent_data["tag"] == intent:
            # Seleccionar una respuesta aleatoria del JSON
            return random.choice(intent_data["responses"])
    # Si no se encuentra la intención, devolver un mensaje genérico
    return "No entendí lo que quisiste decir."


# Bucle principal
while True:
    # Quemar una entrada para pruebas
    texto = "hora"
    texto = texto.lower()
    print(f"Texto recibido: {texto}")
    
    # Detectar intención
    intent = detectar_intencion(texto)
    if intent:
        respuesta = ejecutar_accion(intent)
    else:
        print("No se detectó intención, consultando OpenAI...")
        respuesta = consultar_openai(texto)
    
    # Hablar la respuesta
    print(f"Respuesta: {respuesta}")
    hablar(respuesta)
    break
