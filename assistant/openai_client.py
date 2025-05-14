import openai
from config.settings import OPENAI_API_KEY

# Configurar el cliente con la nueva sintaxis
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def consultar_openai(texto_usuario):
    try:
        respuesta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": texto_usuario}],
            max_tokens=100,
            temperature=0.7,
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"Lo siento, hubo un error al consultar la IA: {e}"
