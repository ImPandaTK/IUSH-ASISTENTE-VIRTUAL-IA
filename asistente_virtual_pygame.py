
import pygame
import math
import whisper
from assistant.recognizer_whisper_Inteligente import escuchar_whisper_dinamico as escuchar
from assistant.intent_matcher import obtener_intencion
from assistant.responder import responder
from assistant.voice_output import hablar
from assistant.weather import obtener_clima
from config.settings import CARGAR_INTENTS

# Inicializar pygame
pygame.init()

# Pantalla
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asistente Virtual AI")

# Colores
BACKGROUND = (10, 10, 30)
CIRCLE_COLOR = (100, 200, 255)
TEXT_COLOR = (255, 255, 255)

# Fuente
font = pygame.font.SysFont("Arial", 26)
response_font = pygame.font.SysFont("Arial", 20)

# Asistente
model = whisper.load_model("base")
print("Whisper cargado correctamente.")
intents = CARGAR_INTENTS()
texto_respuesta = "Toca la esfera para hablar"

esperando_artista = False
esperando_ciudad = False

bienvenida = "¡Que más! En que te atiendo mi fafacho."
hablar(bienvenida)

# Animación
clock = pygame.time.Clock()
t = 0

# Main loop
running = True
while running:
    screen.fill(BACKGROUND)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Al hacer clic en la esfera
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            dist = math.hypot(x - WIDTH//2, y - HEIGHT//2)
            if dist <= 120:
                texto_respuesta = "🎧 Escuchando..."
                pygame.display.update()
                pygame.time.delay(500)

                texto = escuchar()
                if texto:
                    if esperando_artista:
                        respuesta, tipo = responder("musica", texto, intents)
                        esperando_artista = False
                    elif esperando_ciudad:
                        ciudad = texto
                        respuesta = obtener_clima(ciudad)
                        tipo = "clima"
                        esperando_ciudad = False
                    else:
                        intencion = obtener_intencion(texto, intents, umbral=80)
                        if intencion == "clima":
                            respuesta = "¿Para qué ciudad quieres saber el clima?"
                            tipo = "clima"
                            esperando_ciudad = True
                        else:
                            respuesta, tipo = responder(intencion, texto, intents)
                            if respuesta == "¿Qué artista o canción quieres escuchar?":
                                esperando_artista = True
                    texto_respuesta = f"🤖 {respuesta}"
                    hablar(respuesta)
                else:
                    texto_respuesta = "⚠️ No entendí lo que dijiste."
                    hablar("No entendí lo que dijiste.")

    # Animar esfera
    t += 0.05
    scale = 1 + 0.1 * math.sin(t)
    radius = int(100 * scale)
    pygame.draw.circle(screen, CIRCLE_COLOR, (WIDTH//2, HEIGHT//2), radius)

    # Texto superior
    titulo = font.render("Asistente Virtual AI", True, TEXT_COLOR)
    screen.blit(titulo, (WIDTH//2 - titulo.get_width()//2, 40))

    # Texto de respuesta
    respuesta = response_font.render(texto_respuesta, True, TEXT_COLOR)
    screen.blit(respuesta, (WIDTH//2 - respuesta.get_width()//2, HEIGHT - 80))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
