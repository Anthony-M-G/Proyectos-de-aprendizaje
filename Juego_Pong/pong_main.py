import random

from Barra import *
from pong import *
import pygame

alto = 400
ancho = 400

pygame.init()
pantalla = pygame.display.set_mode((alto, ancho))
reloj = pygame.time.Clock()
corriendo = True

pelota = Pelota(10, "red", pantalla, ancho / 2, alto / 2)
barra= Barra(pantalla,"white",ancho/2,350,100,20)
fuente = pygame.font.Font(None, 36)
while corriendo:

    dt = pygame.time.Clock()
    dtt=dt.tick(60)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False

    # fill the screen with a color to wipe away anything from last frame
    pantalla.fill("black")
    texto_puntaje = fuente.render(f"SCORE={pelota.puntaje}", True, "white")
    pantalla.blit(texto_puntaje, (10, 10))
    pelotax=pelota.movimiento_pelota(dtt / 1000, alto, ancho)
    barrax=barra.mover_barra(dtt/100,ancho)

    if pelotax.colliderect(barrax):
       try:
           pelota.dir_y *= -1
           pelota.posicion_y -= dtt
           pelota.puntaje += 1
       except ValueError:
           raise print("error")










    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    reloj.tick(60)  # limits FPS to 60


pygame.quit()
