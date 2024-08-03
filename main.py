import pygame
import random

# Inicializo pygame
pygame.init()

# creo la pantalla
pantalla = pygame.display.set_mode((800, 600))

# titulo, icono y fondo
icono = pygame.image.load("images/astronave.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("images/fondo.jpg")

pygame.display.set_caption("Astro Shooter")

# variables jugador
jugador_img = pygame.image.load("images/astronave.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# variables enemigo
enemigo_img = pygame.image.load("images/ovni.png")
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
enemigo_x_cambio = 0.4
enemigo_y_cambio = 40


def jugador(eje_x, eje_y):
    pantalla.blit(jugador_img, (eje_x, eje_y))


def enemigo(eje_x, eje_y):
    pantalla.blit(enemigo_img, (eje_x, eje_y))


# loop que actualiza el juego
se_ejecuta = True
while se_ejecuta:

    # fondo pantalla
    pantalla.blit(fondo, (0, 0))

    # iterar y actualizar juego con eventos
    for evento in pygame.event.get():
        # cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento movimiento nave
        if evento.type == pygame.KEYDOWN:  # esto se fija si hay una tecla presionada
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +0.5

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # cambiar ubicación nave jugador
    jugador_x += jugador_x_cambio
    # mantener dentro de la pantalla al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:  # 800px - 64px que es el tamaño del png de nave
        jugador_x = 736

    # cambiar ubicación nave enemigo
    enemigo_x += enemigo_x_cambio
    # mantener dentro de la pantalla al enemigo
    if enemigo_x <= 0:
        enemigo_x_cambio = 0.4
        enemigo_y += enemigo_y_cambio
    elif enemigo_x >= 736:  # 800px - 64px que es el tamaño del png de nave
        enemigo_x_cambio = -0.4
        enemigo_y += enemigo_y_cambio

    jugador(jugador_x, jugador_y)
    enemigo(enemigo_x, enemigo_y)

    # actualizar
    pygame.display.update()
