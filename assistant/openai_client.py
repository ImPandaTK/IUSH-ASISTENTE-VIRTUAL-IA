import openai
from config.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def consultar_openai(texto_usuario):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": texto_usuario}]
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"No se pudo obtener respuesta de OpenAI: {e}"
