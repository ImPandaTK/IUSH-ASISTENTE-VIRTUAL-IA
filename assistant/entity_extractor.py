# assistant/entity_extractor.py
import spacy

# Cargar el modelo de español solo una vez
nlp = spacy.load("es_core_news_sm")

def extraer_artista(texto):
    doc = nlp(texto)
    for entidad in doc.ents:
        if entidad.label_ == "PER":  # Persona
            return entidad.text
    return None
