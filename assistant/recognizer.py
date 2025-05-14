import speech_recognition as sr

def escuchar():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        try:
            texto = recognizer.recognize_google(audio, language="es-ES")
            print(f"Tú: {texto}")
            return texto
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return "No se puede conectar al servicio de reconocimiento de voz."
