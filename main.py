import pygame

# Inicializo pygame
pygame.init()

# creo la pantalla
pantalla = pygame.display.set_mode((800, 600))

# titulo, icono y fondo
icono = pygame.image.load("images/astronave.png")
pygame.display.set_icon(icono)

pygame.display.set_caption("Astro Shooter")

# variables jugador
jugador_img = pygame.image.load("images/astronave.png")
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0


def jugador(eje_x, eje_y):
    pantalla.blit(jugador_img, (eje_x, eje_y))


# loop que actualiza el juego
se_ejecuta = True
while se_ejecuta:

    # fondo pantalla
    pantalla.fill((205, 144, 228))

    # iterar y actualizar juego con eventos
    for evento in pygame.event.get():
        # cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento movimiento nave
        if evento.type == pygame.KEYDOWN:  # esto se fija si hay una tecla presionada
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio -= 0.1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio += 0.1

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # cambiar ubicación nave
    jugador_x += jugador_x_cambio

    # mantener dentro de la pantalla
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736: # 800px - 64px que es el tamaño del png de nave
        jugador_x = 736

    jugador(jugador_x, jugador_y)

    # actualizar
    pygame.display.update()
