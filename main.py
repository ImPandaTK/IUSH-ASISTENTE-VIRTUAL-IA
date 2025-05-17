from assistant.recognizer import escuchar
from assistant.intent_matcher import obtener_intencion
from assistant.responder import responder
from assistant.voice_output import hablar
from config.settings import CARGAR_INTENTS
from assistant.spotify_client import buscar_cancion
from assistant.spotify_player import reproducir_cancion_por_nombre

def main():
    intents = CARGAR_INTENTS()
    esperando_artista = False

    hablar("Asistente activado. Di algo...")
    print("Asistente activado. Di algo...")

    while True:
        texto = escuchar()
        if texto:
            if esperando_artista:
                respuesta, tipo = responder("musica", texto, intents)
                esperando_artista = False
            else:
                intencion = obtener_intencion(texto, intents, umbral=80)
                respuesta, tipo = responder(intencion, texto, intents)
                if respuesta == "¿Qué artista o canción quieres escuchar?":
                    esperando_artista = True
        else:
            respuesta = "No entendí lo que dijiste."
            tipo = "error"

        if "|||SEP|||" in respuesta:
            voz, pantalla = respuesta.split("|||SEP|||")
            hablar(voz)
            print(pantalla)
        elif "|||FIN|||" in respuesta:
            mensaje = respuesta.replace("|||FIN|||", "").strip()
            hablar(mensaje)
            print(mensaje)
            break    
        else:
            hablar(respuesta)
            print(respuesta)
            if tipo != "openai" and not esperando_artista:
                break


if __name__ == "__main__":
    main()
