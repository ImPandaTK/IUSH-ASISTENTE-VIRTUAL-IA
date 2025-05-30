import whisper
import sounddevice as sd
import numpy as np
import tempfile
import os
from scipy.io.wavfile import write
import time

# Cargar modelo Whisper
model = whisper.load_model("base")  # Puedes usar "tiny" para más velocidad

def escuchar_whisper_dinamico():
    fs = 16000  # Frecuencia de muestreo
    segundos_max = 10  # Límite máximo
    silencio_rms = 50   # Nivel de silencio (ajustable)
    duracion_buffer = 0.5  # Tamaño de bloque en segundos
    espera_silencio = 1.5  # Cuánto silencio seguido se necesita para cortar

    print("🎤 Grabando... Habla cuando quieras.")

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

    # Guardar el audio
    if not audio_grabado:
        print("⚠️ No se detectó voz.")
        return ""

    audio_np = np.array(audio_grabado)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        write(temp_audio.name, fs, audio_np)
        print("✅ Audio capturado. Transcribiendo con Whisper...")

        resultado = model.transcribe(temp_audio.name, language="es")
        texto = resultado["text"].strip()

        os.remove(temp_audio.name)
        print(f"🗣️ Texto reconocido: {texto}")
        return texto
