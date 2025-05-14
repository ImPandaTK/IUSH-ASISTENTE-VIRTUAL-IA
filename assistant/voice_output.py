import pyttsx3

def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()
    respuesta = "No entendí lo que quisiste decir."
    # Si no se encuentra la intención, devolver un mensaje genérico