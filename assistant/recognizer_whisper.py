import whisper
import os
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile

# Cargar modelo Whisper
model = whisper.load_model("base")  # Puedes usar "tiny", "base", "small", "medium", "large"

def escuchar_whisper(duracion=5):
    print("🎤 Grabando... Habla ahora.")
    
    fs = 16000  # Frecuencia de muestreo
    grabacion = sd.rec(int(duracion * fs), samplerate=fs, channels=1)
    sd.wait()

    # Guardar temporalmente como WAV
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as archivo_audio:
        write(archivo_audio.name, fs, grabacion)
        print("✅ Audio grabado, transcribiendo...")

        # Transcribir usando Whisper
        resultado = model.transcribe(archivo_audio.name, language="es")
        texto = resultado["text"].strip()
        
        print(f"🗣️ Texto reconocido: {texto}")
        os.remove(archivo_audio.name)
        return texto
