from fuzzywuzzy import fuzz

def obtener_intencion(texto_usuario, intents):
    mejor_score = 0
    mejor_intencion = "desconocido"

    for intent in intents["intents"]:
        for patron in intent["patterns"]:
            score = fuzz.partial_ratio(texto_usuario.lower(), patron.lower())
            if score > mejor_score:
                mejor_score = score
                mejor_intencion = intent["tag"]
    
    return mejor_intencion
