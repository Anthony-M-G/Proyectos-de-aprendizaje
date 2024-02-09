import random

import pygame.draw


class Pelota:  # Clase Pelota-->Atributos-->posicion en x,y,radio,color

    def __init__(self, radio, color, pantalla, posicion_x, posicion_y):
        self.pantalla = pantalla
        self.radio = radio
        self.color = color
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.dir_x = random.randint(-5, 5)
        self.dir_y = random.randint(-5, 5)
        self.puntaje = 0

    def movimiento_pelota(self, factor, alto, ancho):
        '''Método que hace que el movimiento de la pelota sea pseudo aleatorio modificando sus propiedades de dirección y posición'''
        self.alto = alto
        self.ancho = ancho
        self.factor = factor

        pygame.draw.circle(self.pantalla, self.color, (self.posicion_x, self.posicion_y), self.radio)

        velocidad = 80
        pelotaRect = pygame.Rect(self.posicion_x, self.posicion_y, self.radio * 2, self.radio * 2)
        self.posicion_y += self.dir_y * velocidad * factor
        self.posicion_x += self.dir_x * velocidad * factor
        # Condiciones de frontera de la pelota
        if self.posicion_y - self.radio < 0:
            self.posicion_y = self.radio
            self.dir_y *= -1

        if self.posicion_y + self.radio > self.alto:
            self.posicion_y = self.alto - self.radio
            self.dir_y *= -1

        if self.posicion_x - self.radio < 0:
            self.posicion_x = self.radio
            self.dir_x *= -1

        if self.radio + self.posicion_x > self.ancho:
            self.posicion_x = self.ancho - self.radio
            self.dir_x *= -1

        return pelotaRect  # Retorna la caja en cual está la pelota
