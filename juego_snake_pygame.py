import random
import pygame

ancho = 500
alto = 500
pygame.init()
screen = pygame.display.set_mode((ancho, alto))
clock = pygame.time.Clock()
running = True
fuente = pygame.font.Font(None, 36)

class Comida:
    def __init__(self, pos_x, pos_y, radio):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio

    def mostrar_circulo(self, pantalla, color):
        '''Metodo que genera el círculo en pantalla'''
        pygame.draw.circle(pantalla, color, [self.pos_x, self.pos_y], self.radio)

class Snake:
    def __init__(self, pantalla, color, posicion_x, posicion_y, lado):
        self.pantalla = pantalla
        self.color = color
        self.posicion_x = posicion_x
        self.posicion_y = posicion_y
        self.lado = lado
        self.puntaje = 0
        self.segmentos = []

    def mover_snake(self, dt):
        '''Metodo que mueve la serpiente dentro de la ventana'''
        keys = pygame.key.get_pressed()
        velocidad = 100
        if keys[pygame.K_w]:
            self.posicion_y -= velocidad * dt
        if keys[pygame.K_s]:
            self.posicion_y += velocidad * dt
        if keys[pygame.K_a]:
            self.posicion_x -= velocidad * dt
        if keys[pygame.K_d]:
            self.posicion_x += velocidad * dt

    def anhadir_cuadro(self, color):
        '''Metodo que al tocar los círculos (comida) aumenta el cuerpo de la serpiente'''
        cabeza = pygame.Rect(self.posicion_x, self.posicion_y, self.lado, self.lado)

        # Insertar la cabeza en la primera posición de la lista de segmentos
        self.segmentos.insert(0, (self.posicion_x, self.posicion_y))

        # Si la cabeza colisiona con la comida, añadir un nuevo segmento a la serpiente
        if cabeza.colliderect(pygame.Rect(comida.pos_x, comida.pos_y, comida.radio * 2, comida.radio * 2)):
            comida.pos_x = random.randrange(0, ancho)
            comida.pos_y = random.randrange(0, alto)
            self.puntaje += 1
        else:
            # Si no hay colisión con la comida, eliminar el último segmento de la serpiente
            self.segmentos.pop()

        pygame.draw.rect(self.pantalla, color, cabeza)  # Dibujar la cabeza de la serpiente

        # Dibujar los segmentos de la serpiente
        for segmento in self.segmentos:
            pygame.draw.rect(self.pantalla, color, (segmento[0], segmento[1], self.lado, self.lado))

    def chocar(self):
        '''Metodo para terminar el juego si choca con los bordes'''
        if self.posicion_x + self.lado >= ancho or self.posicion_x <= 0 or \
           self.posicion_y + self.lado >= alto or self.posicion_y <= 0:
            return True


# pygame setup
snake_x = 250.0
snake_y = 250.0
snake = Snake(screen, "white", snake_x, snake_y, 20)

comida = Comida(random.randrange(0, ancho), random.randrange(0, alto), 10)

while running:
    dt = clock.tick(10) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")  # Llena la pantalla con el color negro

    texto_puntaje = fuente.render(f"SCORE={snake.puntaje}", True, "white")
    screen.blit(texto_puntaje, (10, 10))

    game_over=snake.chocar()
    snake.anhadir_cuadro("white")
    snake.mover_snake(dt)
    comida.mostrar_circulo(screen, "white")

    pygame.display.flip()

    clock.tick(60)
    if game_over:
        pygame.time.delay(5000)
        running = False

# Esperar hasta que el usuario cierre la ventana
pygame.quit()
