from assistant.recognizer import escuchar
from assistant.intent_matcher import obtener_intencion
from assistant.responder import responder
from assistant.voice_output import hablar
from config.settings import CARGAR_INTENTS

def main():
    hablar("Asistente activado. Di algo...")
    print("Asistente activado. Di algo...")
    texto = escuchar()
    if texto:
        intents = CARGAR_INTENTS()
        intencion = obtener_intencion(texto, intents)
        respuesta = responder(intencion, texto, intents)
        print(respuesta)
        hablar(respuesta)
    else:
        hablar("No entendí lo que dijiste.")
        print("No entendí lo que dijiste.")

if __name__ == "__main__":
    main()
