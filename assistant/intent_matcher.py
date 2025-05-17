from fuzzywuzzy import fuzz

def obtener_intencion(texto_usuario, intents, umbral=80):
    mejor_score = 0
    mejor_intencion = None

    for intent in intents["intents"]:
        for patron in intent["patterns"]:
            score = fuzz.partial_ratio(texto_usuario.lower(), patron.lower())
            if score > mejor_score:
                mejor_score = score
                mejor_intencion = intent["tag"]
    
    print(f"➡️ INTENCIÓN DETECTADA: {mejor_intencion} (score: {mejor_score})")
    return mejor_intencion if mejor_score >= umbral else None
