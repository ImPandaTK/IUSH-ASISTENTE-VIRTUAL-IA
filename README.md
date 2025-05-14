# 🤖 Asistente Virtual IA

Este proyecto es un prototipo de asistente virtual desarrollado en Python, diseñado con fines educativos para explorar técnicas de procesamiento de lenguaje natural, reconocimiento de voz y uso de modelos de lenguaje de OpenAI.

---

## 🎯 Contexto y Justificación

Con el auge de la inteligencia artificial y los asistentes conversacionales, este proyecto busca ofrecer una experiencia básica de interacción persona-máquina. El objetivo es:

- Aprender sobre tecnologías de IA aplicadas al lenguaje natural.
- Entender cómo se conectan diferentes herramientas y bibliotecas para construir un asistente virtual.
- Explorar el uso de modelos de lenguaje (LLM) como los de OpenAI en tareas de generación de texto y respuestas contextuales.
- Desarrollar un prototipo funcional, sin altos costos, que pueda ampliarse en futuras etapas.

---

## 📦 Estructura del Proyecto




---

## 🔍 ¿Cómo funciona?

1. **Reconocimiento de voz:** Convierte lo que dice el usuario a texto (`speech_recognition`).
2. **Detección de intención:** Usa coincidencia de patrones con `fuzzywuzzy` y el archivo `intents.json`.
3. **Respuesta:**
   - Si encuentra la intención, responde desde el JSON.
   - Si no la encuentra, consulta la API de OpenAI (GPT-3.5).
4. **Salida por voz:** Usa `pyttsx3` para hablar la respuesta.

---

## 🧠 ¿Qué tipo de inteligencia usa?

- **NLP (Procesamiento de Lenguaje Natural):** para clasificar y emparejar intenciones simples localmente.
- **LLM (Large Language Model):** mediante OpenAI GPT-3.5 para responder preguntas complejas o desconocidas.

---

## 🧰 Herramientas y Librerías

| Librería         | Propósito                                |
|------------------|-------------------------------------------|
| `speech_recognition` | Captura de voz y conversión a texto     |
| `pyttsx3`         | Conversión de texto a voz                 |
| `fuzzywuzzy`      | Coincidencia difusa entre texto y patrón |
| `openai`          | Acceso a la API GPT-3.5                  |
| `python-dotenv`   | Carga de variables desde `.env`          |

---

## 🔐 Configuración de OpenAI

1. Crear archivo `.env` en la raíz del proyecto:

```env
OPENAI_API_KEY=tu_clave_de_api
```

2. Asegurarse de que esté listado en .gitignore para no subirlo a GitHub.

---

## 🚀 Cómo ejecutar

```env
# 1. Instala dependencias
pip install -r requirements.txt

# 2. Ejecuta el asistente
python main.py
```

---

## 📦 Dataset usado

El asistente trabaja con un archivo intents.json que contiene:

```env
{
  "intents": [
    {
      "tag": "saludo",
      "patterns": ["hola", "buenos días", "hey"],
      "responses": ["¡Hola! ¿En qué puedo ayudarte?"]
    },
    {
      "tag": "hora",
      "patterns": ["qué hora es", "me dices la hora"],
      "responses": ["La hora actual es..."]
    }
  ]
}
```

y así sucesivamente...

Este dataset se puede extender con nuevas intenciones, patrones y respuestas.

---

## 📌 Alcance del Proyecto

- Está pensado como una herramienta de aprendizaje, no como producto final (quizás en el futuro).

- Su uso está limitado a pruebas personales con un máximo estimado de 10 usuarios.

- Se utiliza la API de OpenAI con control de uso para evitar costos innecesarios.

---

## 🔮 Posibles mejoras

- Agregar historial de conversaciones

- Crear una interfaz gráfica

- Entrenar un modelo propio de clasificación de intenciones

- Integrar APIs externas (clima, calendario, etc.)

---

## 📄 Licencia

Proyecto con fines educativos. Se puede usar, modificar y adaptar libremente.

---

## ✨ Créditos

Desarrollado por:  
Juan Fernando Sepúlveda Bustamante  
Brahiam Velasquez Rueda

Inspirado en ejemplos de asistentes virtuales con Python y GPT.