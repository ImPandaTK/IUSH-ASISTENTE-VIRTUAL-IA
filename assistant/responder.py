from assistant.openai_client import consultar_openai

def responder(intencion, texto, intents):
    if intencion is None:
        return consultar_openai(texto)
    # Si la intención es válida, devuelve la respuesta correspondiente
    for intent in intents["intents"]:
        if intent["tag"] == intencion:
            return intent["responses"][0]
    
    # Si no se encuentra un tag que coincida (por seguridad)
    return consultar_openai(texto)
