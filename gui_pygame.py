import pygame
import math
from assistant.recognizer import escuchar
from assistant.intent_matcher import obtener_intencion
from assistant.responder import responder
from assistant.voice_output import hablar
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
intents = CARGAR_INTENTS()
texto_respuesta = "Toca la esfera para hablar"

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
                    intencion = obtener_intencion(texto, intents)
                    respuesta = responder(intencion, texto, intents)
                    hablar(respuesta)
                    texto_respuesta = f"🤖 {respuesta}"
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
