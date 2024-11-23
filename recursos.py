import pygame, os
# Constantes de la aplicación
pygame.init()
# Configuración de la ventana
ANCHO_VENTANA = 1100
ALTO_VENTANA = 700

# Sonidos
MUERTE_FX = pygame.mixer.Sound("assets/audio/lose.mp3")
PUNTO_FX = pygame.mixer.Sound("assets/audio/100points.mp3")
SALTO_FX = pygame.mixer.Sound("assets/audio/jump.mp3")

# Imagenes
DINO_CORRIENDO = [pygame.image.load(os.path.join("assets/images/dino", "DinoRun1.png")), 
                  pygame.image.load(os.path.join("assets/images/dino", "DinoRun2.png"))]

DINO_SALTANDO = pygame.image.load(os.path.join("assets/images/dino", "DinoJump.png"))

DINO_AGACHADO = [pygame.image.load(os.path.join("assets/images/dino", "DinoDuck1.png")), 
                pygame.image.load(os.path.join("assets/images/dino", "DinoDuck2.png"))]

CACTUS_CHICO = [pygame.image.load(os.path.join("assets/images/cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("assets/images/cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("assets/images/cactus", "SmallCactus3.png"))]

CACTUS_GRANDE = [pygame.image.load(os.path.join("assets/images/cactus", "LargeCactus1.png")),
                 pygame.image.load(os.path.join("assets/images/cactus", "LargeCactus2.png")),
                 pygame.image.load(os.path.join("assets/images/cactus", "LargeCactus3.png"))]

PAJARO = [pygame.image.load(os.path.join("assets/images/bird", "Bird1.png")), 
          pygame.image.load(os.path.join("assets/images/bird", "Bird2.png"))]

NUBE = pygame.image.load(os.path.join("assets/images/other", "Cloud.png"))

FONDO = pygame.image.load(os.path.join("assets/images/other", "Track.png"))