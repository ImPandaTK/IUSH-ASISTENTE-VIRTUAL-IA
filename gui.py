import tkinter as tk
from tkinter import ttk
from assistant.recognizer import escuchar
from assistant.responder import responder
from assistant.intent_matcher import obtener_intencion
from assistant.voice_output import hablar
from config.settings import CARGAR_INTENTS

intents = CARGAR_INTENTS()

# --- Función principal ---
def ejecutar_asistente():
    texto = escuchar()
    
    if texto:
        entrada_usuario.set(f"🗣️ Tú: {texto}")
        intencion = obtener_intencion(texto, intents)
        respuesta = responder(intencion, texto, intents)
        salida_asistente.set(f"🤖 Asistente: {respuesta}")
        hablar(respuesta)
    else:
        salida_asistente.set("🤖 Asistente: No entendí lo que dijiste.")
        hablar("No entendí lo que dijiste.")

# --- Diseño de interfaz ---
ventana = tk.Tk()
ventana.title("IUSH Asistente Virtual IA")
ventana.geometry("600x400")
ventana.configure(bg="#1e1e2f")
ventana.resizable(False, False)

# Título principal
titulo = tk.Label(ventana, text="🎙️ IUSH Asistente Virtual", font=("Helvetica", 20, "bold"), bg="#1e1e2f", fg="#00BFFF")
titulo.pack(pady=20)

# Frame para mostrar conversación
frame_respuestas = tk.Frame(ventana, bg="#2c2f3f", padx=10, pady=10)
frame_respuestas.pack(padx=20, pady=10, fill="both", expand=True)

entrada_usuario = tk.StringVar()
salida_asistente = tk.StringVar()

label_usuario = tk.Label(frame_respuestas, textvariable=entrada_usuario, font=("Arial", 12), bg="#2c2f3f", fg="white", anchor="w", justify="left", wraplength=500)
label_usuario.pack(anchor="w", pady=5)

label_asistente = tk.Label(frame_respuestas, textvariable=salida_asistente, font=("Arial", 12), bg="#2c2f3f", fg="#00ffcc", anchor="w", justify="left", wraplength=500)
label_asistente.pack(anchor="w", pady=5)

# Botón con estilo
boton_escuchar = ttk.Button(ventana, text="🎤 Escuchar", command=ejecutar_asistente)
boton_escuchar.pack(pady=20)

# Estilo moderno para ttk
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton",
                font=("Helvetica", 14, "bold"),
                foreground="white",
                background="#007ACC",
                padding=10)
style.map("TButton",
          background=[("active", "#005f9e")])

# Ejecutar interfaz
ventana.mainloop()
