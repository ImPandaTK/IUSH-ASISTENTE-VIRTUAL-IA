import whisper
import sounddevice as sd
import numpy as np
import tempfile
import os
from scipy.io.wavfile import write
import time
from assistant.voice_output import hablar

# Cargar el modelo Whisper
model = whisper.load_model("base")  # podés usar "tiny", "base", "small", etc.

def escuchar_whisper_dinamico():
    fs = 16000  # Frecuencia de muestreo
    segundos_max = 10  # Límite de duración
    silencio_rms = 50   # Umbral de silencio
    duracion_buffer = 0.2  # Segmento de grabación (en segundos)
    espera_silencio = 1.5  # Cuánto silencio seguido se necesita para cortar

    mensaje_bienvenida = ("Estoy escuchando")
    hablar(mensaje_bienvenida)
    print(mensaje_bienvenida)

    audio_grabado = []
    tiempo_silencio = 0

    def callback(indata, frames, time_info, status):
        nonlocal audio_grabado, tiempo_silencio
        volumen = np.linalg.norm(indata) * 1000

        if volumen > silencio_rms:
            tiempo_silencio = 0
            audio_grabado.extend(indata.copy())
        else:
            tiempo_silencio += duracion_buffer
            if tiempo_silencio < espera_silencio:
                audio_grabado.extend(indata.copy())

    with sd.InputStream(callback=callback, samplerate=fs, channels=1, blocksize=int(fs * duracion_buffer)):
        time.sleep(segundos_max)

    # Si no se capturó nada
    if not audio_grabado:
        print("⚠️ No se detectó voz.")
        hablar("No se detectó voz.")
        return ""

    # Guardar en archivo temporal
    audio_np = np.array(audio_grabado)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        write(temp_audio.name, fs, audio_np)
        nombre_temp = temp_audio.name  # Guardamos el nombre para usar fuera del bloque

    print("✅ Audio capturado. Transcribiendo con Whisper...")

    # Transcribir con Whisper
    resultado = model.transcribe(nombre_temp, language="es")
    texto = resultado["text"].strip()

    # Eliminar archivo temporal una vez usado
    try:
        os.remove(nombre_temp)
    except Exception as e:
        print(f"⚠️ No se pudo eliminar el archivo temporal: {e}")

    print(f"🗣️ Texto reconocido: {texto}")
    return texto
