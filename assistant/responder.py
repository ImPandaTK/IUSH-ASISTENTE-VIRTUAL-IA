from assistant.openai_client import consultar_openai
from assistant.spotify_client import buscar_cancion
from assistant.spotify_player import reproducir_cancion_por_nombre, obtener_cancion_actual, reproducir_por_mood_o_genero
from assistant.entity_extractor import extraer_artista
import random
from datetime import datetime

def responder(intencion, texto, intents):
    if intencion is None:
        return consultar_openai(texto), "openai"

    if intencion == "musica":
        artista = extraer_artista(texto)

        if artista:
            return reproducir_cancion_por_nombre(artista), "musica"

        # Intentar detectar un mood o género
        mood_resultado = reproducir_por_mood_o_genero(texto)
        if mood_resultado:
            return mood_resultado,"musica"

        # Si el texto no tiene contenido útil
        texto_limpio = texto.lower().strip()
        if texto_limpio in ["quiero escuchar música", "pon algo", "quiero música", "pon una canción", "quiero escuchar música de", "reproduce algo"]:
            return "¿Qué artista o canción quieres escuchar?", "musica"

        # Si el texto tiene varias palabras, asumir que hay algo útil
        if len(texto_limpio.split()) >= 2:
            return reproducir_cancion_por_nombre(texto), "musica"
        
    if intencion == "cancion_actual":
        return obtener_cancion_actual(), "cancion_actual"

    if intencion == "despedida":
        return "|||FIN|||La buena mi so", "despedida"

    for intent in intents["intents"]:
        if intent["tag"] == intencion:
            respuesta = random.choice(intent["responses"])
            if "{hora_actual}" in respuesta:
                ahora = datetime.now().strftime("%H:%M")
                respuesta = respuesta.replace("{hora_actual}", ahora)
            return respuesta, intencion

    return consultar_openai(texto), "openai"
