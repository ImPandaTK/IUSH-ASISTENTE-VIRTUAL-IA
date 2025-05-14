from assistant.openai_client import consultar_openai

def responder(intencion, texto, intents):
    for intent in intents["intents"]:
        if intent["tag"] == intencion:
            return intent["responses"][0]
    
    return consultar_openai(texto)
