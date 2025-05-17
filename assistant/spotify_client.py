# assistant/spotify_client.py

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def buscar_cancion(nombre_usuario):
    # Paso 1: Buscar artista
    resultado_artista = sp.search(q=nombre_usuario, type="artist", limit=1)
    if resultado_artista["artists"]["items"]:
        artista = resultado_artista["artists"]["items"][0]
        artista_id = artista["id"]
        nombre_real = artista["name"]

        # Paso 2: Obtener top canciones del artista
        top_tracks = sp.artist_top_tracks(artista_id, country='US')
        if top_tracks["tracks"]:
            cancion = top_tracks["tracks"][0]
            nombre = cancion["name"]
            album = cancion["album"]["name"]
            link = cancion["external_urls"]["spotify"]
            return f"🎵 {nombre} - {nombre_real}\nÁlbum: {album}\nEscúchala aquí: {link}"

    # Si no encontró artista, buscar como track general
    resultados = sp.search(q=nombre_usuario, type="track", limit=1)
    if resultados["tracks"]["items"]:
        cancion = resultados["tracks"]["items"][0]
        nombre = cancion["name"]
        artista = cancion["artists"][0]["name"]
        album = cancion["album"]["name"]
        link = cancion["external_urls"]["spotify"]
        return f"🎵 {nombre} - {artista}\nÁlbum: {album}\nEscúchala aquí: {link}"
    
    return "No encontré esa canción ni artista en Spotify."
