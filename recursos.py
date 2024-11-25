import pygame, os, sys

def ruta_recurso(ruta_relativa):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath("."), ruta_relativa)

# Constantes de la aplicación
pygame.init()
# Configuración de la ventana
ANCHO_VENTANA = 1100
ALTO_VENTANA = 700

# Sonidos
MUERTE_FX = pygame.mixer.Sound(ruta_recurso("assets/audio/lose.mp3"))
PUNTO_FX = pygame.mixer.Sound(ruta_recurso("assets/audio/100points.mp3"))
SALTO_FX = pygame.mixer.Sound(ruta_recurso("assets/audio/jump.mp3"))

# Imágenes
DINO_CORRIENDO = [
    pygame.image.load(ruta_recurso("assets/images/dino/DinoRun1.png")),
    pygame.image.load(ruta_recurso("assets/images/dino/DinoRun2.png"))
]

DINO_SALTANDO = pygame.image.load(ruta_recurso("assets/images/dino/DinoJump.png"))

DINO_AGACHADO = [
    pygame.image.load(ruta_recurso("assets/images/dino/DinoDuck1.png")),
    pygame.image.load(ruta_recurso("assets/images/dino/DinoDuck2.png"))
]

CACTUS_CHICO = [
    pygame.image.load(ruta_recurso("assets/images/cactus/SmallCactus1.png")),
    pygame.image.load(ruta_recurso("assets/images/cactus/SmallCactus2.png")),
    pygame.image.load(ruta_recurso("assets/images/cactus/SmallCactus3.png"))
]

CACTUS_GRANDE = [
    pygame.image.load(ruta_recurso("assets/images/cactus/LargeCactus1.png")),
    pygame.image.load(ruta_recurso("assets/images/cactus/LargeCactus2.png")),
    pygame.image.load(ruta_recurso("assets/images/cactus/LargeCactus3.png"))
]

PAJARO = [
    pygame.image.load(ruta_recurso("assets/images/bird/Bird1.png")),
    pygame.image.load(ruta_recurso("assets/images/bird/Bird2.png"))
]

NUBE = pygame.image.load(ruta_recurso("assets/images/other/Cloud.png"))

FONDO = pygame.image.load(ruta_recurso("assets/images/other/Track.png"))