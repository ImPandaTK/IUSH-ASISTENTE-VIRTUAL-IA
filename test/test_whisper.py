import whisper
import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000
duracion = 5  # segundos
print("🎤 Grabando...")
audio = sd.rec(int(fs * duracion), samplerate=fs, channels=1)
sd.wait()
write("audio_prueba.wav", fs, audio)
print("✅ Audio guardado.")


def probar_whisper():
    try:
        print("🔄 Cargando modelo Whisper...")
        model = whisper.load_model("base")
        print("✅ Modelo Whisper cargado correctamente.")

        # Verifica si podés transcribir un archivo (opcional)
        archivo_prueba = "audio_prueba.wav"  # Reemplaza por un audio real si querés probar

        try:
            resultado = model.transcribe(archivo_prueba, language="es")
            print("✅ Transcripción completada:")
            print("🗣️", resultado["text"])
        except FileNotFoundError:
            print("⚠️ No se encontró un archivo de audio de prueba. Solo se verificó carga del modelo.")
        except Exception as e:
            print("❌ Error al transcribir:", e)

    except Exception as e:
        print("❌ Falló la carga de Whisper.")
        print("Detalles del error:", e)

if __name__ == "__main__":
    probar_whisper()
