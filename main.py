import pygame, random, sys
from clases import *
from recursos import * #ANCHO_VENTANA, ALTO_VENTANA, FONDO
from colores import BLANCO, NEGRO

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

def main():
    global velocidad_juego, fondo_pos_x, fondo_pos_y, puntos, obstaculos

    juego_corriendo = True
    reloj = pygame.time.Clock()

    jugador = Dinosaurio()
    nube = Nube()
    velocidad_juego = 14 # Velocidad inicial del juego
    fondo_pos_x = 0
    fondo_pos_y = 380
    puntos = 0
    fuente_texto = pygame.font.Font('freesansbold.ttf', 20)
    obstaculos = []
    cantidad_muertes = 0 

    def puntaje():
        global puntos, velocidad_juego
        puntos += 0.2
        # Por cada 100 puntos, la velocidad del juego aumenta en 1
        if round(puntos, 1) % 100 == 0: 
            velocidad_juego += 1

        if round(puntos, 1) % 100 == 0 and int(puntos) > 0:
            PUNTO_FX.play()
        texto = fuente_texto.render("Puntos: " + str(int(puntos)), True, NEGRO) # (Texto, suavizado, color)
        texto_rect = texto.get_rect()
        texto_rect.center = (1000, 50) # Parte superior izquierda
        ventana.blit(texto, texto_rect)

    def fondo():
        global fondo_pos_x, fondo_pos_y
        ancho_imagen = FONDO.get_width()
        ventana.blit(FONDO, (fondo_pos_x, fondo_pos_y))
        ventana.blit(FONDO, (ancho_imagen + fondo_pos_x, fondo_pos_y))

        if fondo_pos_x <= -ancho_imagen:
            fondo_pos_x = 0
        
        fondo_pos_x -= velocidad_juego

    while juego_corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_corriendo = False
                pygame.quit()
                sys.exit()

        ventana.fill(BLANCO)

        tecla_presionada = pygame.key.get_pressed()

        jugador.dibujar(ventana)
        jugador.actualizar(tecla_presionada)

        if len(obstaculos) == 0:
            if random.randint(0, 2) == 0:
                obstaculos.append(CactusChico(CACTUS_CHICO))
            elif random.randint(0, 2) == 1:
                obstaculos.append(CactusGrande(CACTUS_GRANDE))
            elif random.randint(0, 2) == 2:
                obstaculos.append(Pajaro(PAJARO))

        for obstaculo in obstaculos:
            obstaculo.dibujar(ventana)
            obstaculo.actualizar(obstaculos, velocidad_juego)

            if jugador.dino_rect.colliderect(obstaculo.rect):
                if abs(jugador.dino_rect.x - obstaculo.rect.x) <= 80 and abs(jugador.dino_rect.y - obstaculo.rect.y) <= 50:
                    MUERTE_FX.play()
                    #pygame.draw.rect(ventana, (255, 0, 0), jugador.dino_rect, 2) # DIbuja un rectangulo rojo alrededor del dinosaurio
                    pygame.time.delay(2000)
                    cantidad_muertes += 1
                    menu(cantidad_muertes)
        
        fondo()

        nube.dibujar(ventana)
        nube.actualizar(velocidad_juego)

        puntaje()

        reloj.tick(30)
        pygame.display.update()  

#main()

def menu(cantidad_muertes):
    global puntos
    juego_corriendo = True

    while juego_corriendo:
        ventana.fill(BLANCO)
        fuente_texto = pygame.font.Font('freesansbold.ttf', 30)

        if cantidad_muertes == 0:
            texto = fuente_texto.render("[PRESIONA CUALQUIER TECLA PARA COMENZAR]", True, NEGRO)
        elif cantidad_muertes > 0:
            texto = fuente_texto.render("[PRECIONA CUALQUIER TECLA PARA REINICIAR]", True, NEGRO)
            puntaje = fuente_texto.render("PUNTOS :" + str(int(puntos)), True, NEGRO)
            puntaje_rect = puntaje.get_rect()
            puntaje_rect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2 + 50)
            ventana.blit(puntaje, puntaje_rect)

        texto_rect = texto.get_rect()
        texto_rect.center = (ANCHO_VENTANA // 2, ALTO_VENTANA // 2)
        ventana.blit(texto, texto_rect)

        ventana.blit(DINO_CORRIENDO[0], (ANCHO_VENTANA // 2 - 20, ALTO_VENTANA // 2 - 140))        

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_corriendo = False
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                main()


menu(cantidad_muertes=0)