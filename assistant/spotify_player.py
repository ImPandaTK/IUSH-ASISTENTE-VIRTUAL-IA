# assistant/spotify_player.py

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

generos_o_moods = {
    "romántica": "romantic",
    "triste": "sad",
    "feliz": "happy",
    "entrenar": "workout",
    "relajante": "chill",
    "tranquila": "calm",
    "energética": "energy",
    "reggaetón": "reggaeton",
    "rock": "rock",
    "electrónica": "electronic",
    "pop": "pop",
    "clásica": "classical"
}

# Scopes necesarios para controlar la reproducción
SCOPE = "user-read-playback-state user-modify-playback-state user-read-currently-playing"

# Crear cliente con autenticación OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
    scope=SCOPE
))

def reproducir_cancion_por_nombre(nombre):
    resultados = sp.search(q=nombre, type='track', limit=1)
    if resultados["tracks"]["items"]:
        cancion = resultados["tracks"]["items"][0]
        nombre_cancion = cancion["name"]
        artista = cancion["artists"][0]["name"]
        album = cancion["album"]["name"]
        link = cancion["external_urls"]["spotify"]
        uri = cancion["uri"]

        dispositivos = sp.devices()
        if not dispositivos["devices"]:
            return "No hay ningún dispositivo activo de Spotify. Abre Spotify en tu PC o navegador y reproduce algo primero."

        sp.start_playback(uris=[uri])

        # ✅ Texto para voz + consola
        mensaje = (
            f"🎵 Reproduciendo ahora:\n"
            f"{nombre_cancion} - {artista}\n"
            f"Álbum: {album}\n"
            f"🔗 {link}"
        )

        # ✅ Versión hablada
        mensaje_hablado = f"Reproduciendo ahora: {nombre_cancion} de {artista}, del álbum {album}"

        return mensaje_hablado + "|||SEP|||" + mensaje  # usamos separador para dividir texto vs voz

    return "No encontré esa canción para reproducir."

def reproducir_por_mood_o_genero(texto_usuario):
    for clave in generos_o_moods:
        if clave in texto_usuario.lower():
            mood_en_inglés = generos_o_moods[clave]
            resultados = sp.search(q=mood_en_inglés, type='track', limit=1)
            if resultados["tracks"]["items"]:
                cancion = resultados["tracks"]["items"][0]
                nombre = cancion["name"]
                artista = cancion["artists"][0]["name"]
                album = cancion["album"]["name"]
                link = cancion["external_urls"]["spotify"]
                uri = cancion["uri"]

                dispositivos = sp.devices()
                if not dispositivos["devices"]:
                    return "No hay ningún dispositivo activo de Spotify. Abre Spotify en tu PC o navegador."

                sp.start_playback(uris=[uri])

                mensaje = f"🎵 Reproduciendo una canción {clave}:\n{nombre} - {artista}\nÁlbum: {album}\n🔗 {link}"
                mensaje_hablado = f"Reproduciendo una canción {clave}: {nombre} de {artista}"
                return mensaje_hablado + "|||SEP|||" + mensaje
    return None  # no se detectó ningún mood/género


def obtener_cancion_actual():
    playback = sp.current_playback()
    if playback and playback["is_playing"]:
        item = playback["item"]
        nombre = item["name"]
        artista = item["artists"][0]["name"]
        album = item["album"]["name"]
        link = item["external_urls"]["spotify"]
        return f"🎧 Ahora suena:\n{nombre} - {artista}\nÁlbum: {album}\n🔗 {link}"
    else:
        return "No hay música sonando en este momento."

