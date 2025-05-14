import pyttsx3

def hablar(texto):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "spanish" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    engine.say(texto)
    engine.runAndWait()
    respuesta = "No entendí lo que quisiste decir."
    # Si no se encuentra la intención, devolver un mensaje genérico