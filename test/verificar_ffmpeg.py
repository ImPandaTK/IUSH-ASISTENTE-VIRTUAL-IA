import subprocess
import shutil

def verificar_ffmpeg():
    ruta = shutil.which("ffmpeg")
    if ruta:
        print(f"✅ ffmpeg está instalado en: {ruta}")
        try:
            resultado = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
            print("Versión detectada:\n")
            print(resultado.stdout.splitlines()[0])
        except Exception as e:
            print("⚠️ Error al ejecutar ffmpeg:", e)
    else:
        print("❌ ffmpeg no está instalado o no está en el PATH.")
        print("▶️ Solución recomendada:")
        print("1. Descarga FFmpeg desde: https://www.gyan.dev/ffmpeg/builds/")
        print("2. Extrae la carpeta y agrega la ruta /bin al PATH de tu sistema.")
        print("3. Luego reinicia tu terminal o VS Code.")

# Ejecutar verificación
if __name__ == "__main__":
    verificar_ffmpeg()
