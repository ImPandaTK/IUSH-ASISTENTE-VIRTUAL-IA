# 🤖 Asistente Virtual con IA y NLP

## 🧠 ¿Qué es un Asistente Virtual?
Un asistente virtual es un programa que simula conversación humana para realizar tareas, responder preguntas o asistir al usuario mediante voz o texto.

---

## ⚙️ Tecnologías Usadas

### 🔉 Entrada de voz (Speech-to-Text)
- **Librería:** `speech_recognition`
- **Motores posibles:** Google Web Speech API, Whisper, Vosk
- **Función:** Convierte voz en texto para su posterior procesamiento.

### 🧠 Procesamiento del Lenguaje Natural (NLP)
- **Modelos posibles:**
  - Regresores o clasificadores simples con TF-IDF
  - `spaCy`, `NLTK`, `transformers` (intermedio)
  - LLMs como GPT (avanzado)
- **Función:** Identificar intención y entidades en el texto.

### 📄 Intenciones (`intents.json`)
Define categorías como saludo, despedida, música, etc.
```json
{
  "intents": [
    {
      "tag": "saludo",
      "patterns": ["hola", "buenos días"],
      "responses": ["¡Hola! ¿Cómo estás?"]
    }
  ]
}
```

### 🗣️ Salida de voz (Text-to-Speech)
- **Librería:** `pyttsx3`, `gTTS`
- **Función:** Convierte texto a voz para la respuesta hablada.

### 🔗 Integraciones
- **Spotify API:** Para buscar y reproducir música.
- **OpenAI API:** Para generar respuestas naturales.

---

## 🧪 Ciclo de funcionamiento
```
1. Usuario habla 🎤
2. Se transcribe a texto 📝
3. Se interpreta la intención 🧠
4. Se ejecuta la acción ⚙️
5. Se genera la respuesta 📤
6. Se reproduce por voz 🔊
```

---

## 🧠 Modelos para NLP

### Nivel básico
- **Clasificador** entrenado con `scikit-learn`
- Técnicas:
  - Bag of Words
  - TF-IDF
  - Red neuronal básica (`keras` + `tensorflow`)

### Nivel intermedio
- **Embeddings** con `spaCy`, `BERT`, `sentence-transformers`
- **Modelos:** SVM, Random Forest, Redes neuronales

### Nivel avanzado
- **Modelos LLM preentrenados:** como GPT
- Se usa como servicio con "prompt engineering" o fine-tuning

---

## 🎓 Entrenamiento de un modelo simple

### Paso 1: Cargar datos
Desde `intents.json`, se extraen los `patterns` y su `tag`.

### Paso 2: Preprocesamiento
- Tokenización
- Remoción de stopwords
- Stemming o lematización

### Paso 3: Vectorización
- TF-IDF o Bag of Words

### Paso 4: Modelo de clasificación
```python
model = Sequential()
model.add(Dense(128, input_shape=(X.shape[1],), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(len(labels), activation='softmax'))
```

### Paso 5: Entrenamiento
```python
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=200)
```

---

# 🌎 Mundo del NLP

## 🔍 1. ¿Qué es NLP?

El Procesamiento del Lenguaje Natural (NLP) es un campo de la inteligencia artificial que se encarga de la interacción entre computadoras y lenguaje humano. Su objetivo es leer, interpretar, entender y generar lenguaje humano.

## 🧩 2. Tareas comunes en NLP

| Tarea                        | ¿Para qué sirve?                                         | Ejemplo                                     |
| ---------------------------- | -------------------------------------------------------- | ------------------------------------------- |
| **Tokenización**             | Separar el texto en palabras o frases                    | "Hola, ¿cómo estás?" → \[Hola, cómo, estás] |
| **Stopword Removal**         | Eliminar palabras irrelevantes (el, la, y...)            | "el perro come" → \[perro, come]            |
| **Stemming / Lemmatization** | Reducir palabras a su raíz o forma base                  | "jugando" → "jugar"                         |
| **POS Tagging**              | Etiquetar la categoría gramatical de cada palabra        | perro (sustantivo), corre (verbo)           |
| **NER (Named Entity Rec.)**  | Detectar entidades nombradas (personas, lugares, fechas) | "Juan vive en Colombia" → Juan (Persona)    |
| **Clasificación de texto**   | Asignar una categoría a un texto                         | spam / no spam                              |
| **Análisis de sentimientos** | Detectar si un texto es positivo, negativo o neutral     | "¡Esto me encantó!" → positivo              |
| **Traducción**               | Convertir de un idioma a otro                            | "Hello" → "Hola"                            |

## 🛠️ 3. Librerías populares

| Librería                     | ¿Para qué sirve?                           | Nivel        |
| ---------------------------- | ------------------------------------------ | ------------ |
| `NLTK`                       | Procesamiento básico y análisis gramatical | Principiante |
| `spaCy`                      | Tokenización, POS, NER, embeddings         | Intermedio   |
| `transformers` (HuggingFace) | Modelos preentrenados (BERT, GPT, etc.)    | Avanzado     |
| `scikit-learn`               | Clasificación y vectorización              | Intermedio   |

## 🧪 4. Flujo típico de NLP

Texto crudo  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Tokenización  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓    
Eliminación de stopwords  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Stemming o lematización  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Vectorización (TF-IDF, Word2Vec, BERT)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓    
Modelo de ML / Red Neuronal  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;↓  
Predicción (Intención, Sentimiento, Categoría, etc.)

## 🧠 5. Modelos de NLP

| Tipo de modelo    | Ejemplos                 | ¿Qué hace?                              |
| ----------------- | ------------------------ | --------------------------------------- |
| Basados en reglas | Regex, diccionarios      | Simples, rápidos pero limitados         |
| Estadísticos      | Naive Bayes, SVM, LR     | Basados en frecuencia y probabilidades  |
| Embeddings        | Word2Vec, GloVe          | Capturan contexto semántico             |
| Deep Learning     | LSTM, CNN para texto     | Reconocen patrones en secuencia         |
| Transformers      | BERT, GPT, RoBERTa, etc. | Modelos SOTA con comprensión contextual |




