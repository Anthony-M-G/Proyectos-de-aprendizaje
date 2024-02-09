import pygame.key




class Barra:

    def __init__(self, pantalla, color, pos_x, pos_y, ancho, alto):
        self.pantalla = pantalla
        self.color = color
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.ancho = ancho
        self.alto = alto

    def mover_barra(self, dt, ancho):
        '''Método que define los parámetros del movimiento de la barra a lo largo del eje x'''
        barra = pygame.Rect(self.pos_x, self.pos_y, self.ancho, self.alto) #Rectangulo generado respecto a los atributos de la barra
        keys = pygame.key.get_pressed()
        velocidad = 20
        if keys[pygame.K_a]:
            self.pos_x -= velocidad * dt
            if self.pos_x <= 0:
                self.pos_x = 0 #Limite izquierdo
        if keys[pygame.K_d]:
            self.pos_x += velocidad * dt
            if ancho - self.pos_x <= self.ancho: #Limite derecho
                self.pos_x = 300

        pygame.draw.rect(self.pantalla, self.color, barra)

        return barra


