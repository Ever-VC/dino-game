import pygame, sys
from colores import *

pygame.init()

dimensiones = (700, 500)

ventana = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Mi primer juego en pygame")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(BLANCO)

    # -------- AREA DE DIBUJO ------

    #Dibujando una linea
    punto_inicio = (20, 500)
    punto_fin = (40, 500)
    pygame.draw.line(ventana, VERDE, punto_inicio, punto_fin, 5)

    pygame.display.update()