import pygame, random
from recursos import *

class Dinosaurio:
    X_POS = 80
    Y_POS = 310
    Y_POS_AGACHADO = 340
    VEL_SALTO = 8.5

    def __init__(self):
        # Imágenes del dinosaurio
        self.agachado_img = DINO_AGACHADO
        self.corriendo_img = DINO_CORRIENDO
        self.saltando_img = DINO_SALTANDO

        # Estado del dinosaurio
        self.dino_agachado = False
        self.dino_corriendo = True
        self.dino_saltando = False

        # Posición del dinosaurio
        # Controla el ritmo de la animación del dinosaurio al correr o agacharse. 
        # Divide la tasa de actualización del juego (los cuadros) para asegurarse de 
        # que las imágenes cambien de forma suave y en intervalos definidos
        self.frame_animacion = 0

        self.vel_salto = self.VEL_SALTO
        self.imagen = self.corriendo_img[0] # Imagen actual del dinosaurio (corriendo)
        self.dino_rect = self.imagen.get_rect() # Rectángulo del dinosaurio
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
    
    def actualizar(self, tecla_presionada):
        # Actualiza a la funcion correspondiente segun el estado del dino
        if self.dino_corriendo:
            self.correr()
        if self.dino_saltando:
            self.saltar()
        if self.dino_agachado:
            self.agacharse()

        # Evita que el valor crezca indefinidamente y mantiene la animación en un ciclo constante
        if self.frame_animacion >= 10:
            self.frame_animacion = 0
        
        if tecla_presionada[pygame.K_UP] and not self.dino_saltando:
            # En caso que la tecla presionada sea la de hacia arriba y el dinosaurio no este en el aire (saltando)
            # entonces su estado ahora sera saltando
            SALTO_FX.play()
            self.dino_agachado = False
            self.dino_corriendo = False
            self.dino_saltando = True
        elif tecla_presionada[pygame.K_DOWN] and not self.dino_saltando:
            # En caso que la tecla presionada sea la de hacia abajo y el dinosaurio no este en el aire (saltando)
            # entonces significa que se desea agachar
            self.dino_agachado = True
            self.dino_corriendo = False
            self.dino_saltando = False
        elif not (self.dino_saltando or tecla_presionada[pygame.K_DOWN]):
            # Si ya no se esta presionando la tecla de hacia abajo (cuando se suelta) y 
            # el dinosaurio no esta saltando, entonces vuelve al estado de correr
            self.dino_agachado = False
            self.dino_corriendo = True
            self.dino_saltando = False

    def correr(self):
        # Alterna entre 0 y 1 (ya que step_index incrementa de 1 en 1), permitiendo que
        # el juego  cambie entre las dos imágenes cada 5 cuadros. 
        # Esto hace que el dinosaurio parezca estar corriendo.
        self.imagen = self.corriendo_img[self.frame_animacion // 5]
        self.dino_rect = self.imagen.get_rect() # Rectángulo del dinosaurio
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.frame_animacion += 1
    
    def saltar(self):
        self.imagen = self.saltando_img # Establece la imagen del dinosaurio saltando
        # Mientras el dinosaurio esta saltando..
        if self.dino_saltando:
            # Reduce el valor de y, por lo que el dinosaurio se mueve hacia arriba en el eje Y
            # Al multiplicar por 4 escala la velocidad de salto para que el movimiento sea más pronunciado
            self.dino_rect.y -= self.vel_salto * 4
            # Cada cuadro, la velocidad de salto disminuye, simulando el efecto de la gravedad
            # Lo que hace que el dinosaurio eventualmente deje de subir y comience a bajar
            self.vel_salto -= 0.8
        
        # Verifica si la velocidad de salto ha alcanzado su valor negativo máximo
        # Lo que significa que el dinosaurio ha completado el ciclo de salto (subida y bajada).
        if self.vel_salto < - self.VEL_SALTO:
            self.dino_saltando = False
            self.vel_salto = self.VEL_SALTO
    
    def agacharse(self):
        self.imagen = self.agachado_img[self.frame_animacion // 5]
        self.dino_rect = self.imagen.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_AGACHADO
        self.frame_animacion += 1

    def dinbujar(self, ventana):
        ventana.blit(self.imagen, (self.dino_rect.x, self.dino_rect.y))

class Nube:
    def __init__(self):
        self.x = ANCHO_VENTANA + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.imagen = NUBE
        self.ancho = self.imagen.get_width()

    def actualizar(self, velocidad_juego):
        self.x -= velocidad_juego
        if self.x < -self.ancho:
            self.x = ANCHO_VENTANA + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.x, self.y))

class Obstaculo:
    def __init__(self, imagen, tipo):
        self.imagen = imagen
        self.tipo = tipo
        self.rect = self.imagen[self.tipo].get_rect()
        self.rect.x = ANCHO_VENTANA

    def actualizar(self, obstaculos, velocidad_juego):
        self.rect.x -= velocidad_juego
        if self.rect.x < -self.rect.width: # Cuando el objeto sale de la ventana lo elimina
            obstaculos.pop()

    def dibujar(self, ventana):
        ventana.blit(self.imagen[self.tipo], self.rect)

class CactusChico(Obstaculo):
    def __init__(self, imagen):
        self.tipo = random.randint(0, 2)
        super().__init__(imagen, self.tipo)
        self.rect.y = 325

class CactusGrande(Obstaculo):
    def __init__(self, imagen):
        self.tipo = random.randint(0, 2)
        super().__init__(imagen, self.tipo)
        self.rect.y = 300

class Pajaro(Obstaculo):
    def __init__(self, imagen):
        self.tipo = 0
        super().__init__(imagen, self.tipo)
        self.rect.y = random.randint(200, 320)
        self.frame_animacion = 0

    def dibujar(self, ventana):
        if self.frame_animacion >= 9:
            self.frame_animacion = 0
        ventana.blit(self.imagen[self.frame_animacion // 5], self.rect)
        self.frame_animacion += 1