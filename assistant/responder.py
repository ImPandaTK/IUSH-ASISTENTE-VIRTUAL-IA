from assistant.openai_client import consultar_openai
from assistant.spotify_client import buscar_cancion
from assistant.spotify_player import reproducir_cancion_por_nombre, obtener_cancion_actual, reproducir_por_mood_o_genero
from assistant.entity_extractor import extraer_artista
import random
from datetime import datetime
from modules.pc_control import abrir_programa, cerrar_programa, escribir_texto, abrir_url

# Función auxiliar para detectar nombres de programas en el texto
def extraer_programa(texto):
    posibles = ["word", "excel", "spotify", "navegador", "calculadora", "bloc de notas", "explorador", "chrome"]
    for prog in posibles:
        if prog in texto.lower():
            return prog
    return None

# Función auxiliar para extraer URLs
def extraer_url(texto):
    palabras = texto.lower().split()
    for palabra in palabras:
        if "." in palabra:  # ej: youtube.com
            return palabra
    return "google.com"  # valor por defecto

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
        return "La buena mi so", "despedida"

    for intent in intents["intents"]:
        if intent["tag"] == intencion:
        # ACCIONES ESPECIALES PRIMERO
            if intencion == "abrir_programa":
                nombre = extraer_programa(texto)
                return abrir_programa(nombre) if nombre else "No entendí qué programa querés abrir.", "pc"

            elif intencion == "cerrar_programa":
                nombre = extraer_programa(texto)
                return cerrar_programa(nombre) if nombre else "No entendí qué programa querés cerrar.", "pc"

            elif intencion == "escribir_texto":
                mensaje = texto.replace("escribe", "").strip()
                return escribir_texto(mensaje), "pc"

            elif intencion == "abrir_url":
                url = extraer_url(texto)
                return abrir_url(url), "pc"

            # RESPUESTA NORMAL
            respuesta = random.choice(intent["responses"])
            if "{hora_actual}" in respuesta:
                ahora = datetime.now().strftime("%I:%M %p")  # Formato de 12 horas con AM/PM
                respuesta = respuesta.replace("{hora_actual}", ahora)

            return respuesta, intencion


    return consultar_openai(texto), "openai"
