import pygame
import random
import math
from pygame import mixer

# Inicializo pygame
pygame.init()

# creo la pantalla
pantalla = pygame.display.set_mode((800, 600))

# titulo, icono y fondo
icono = pygame.image.load("images/astronave.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("images/fondo.jpg")
pygame.display.set_caption("Astro Shooter")

#

# variables jugador
jugador_img = pygame.image.load("images/astronave.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# variables enemigo
enemigo_img = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cant_enemigos = 8

for e in range(cant_enemigos):
    enemigo_img.append(pygame.image.load("images/ovni.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.4)
    enemigo_y_cambio.append(40)

# variables de la bala
balas = []
bala_img = pygame.image.load("images/bala.png")
bala_x = 0
bala_y = 500
bala_y_cambio = 1
bala_visible = False

# puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# texto final juego
fuente_final = pygame.font.Font('freesansbold.ttf', 32)

# funcion para mostrar el puntaje
def mostrar_puntaje(eje_x, eje_y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (eje_x, eje_y))


def jugador(eje_x, eje_y):
    pantalla.blit(jugador_img, (eje_x, eje_y))


def enemigo(eje_x, eje_y, ene):
    pantalla.blit(enemigo_img[ene], (eje_x, eje_y))


def disparar_bala(eje_x, eje_y):
    global bala_visible
    bala_visible = True
    pantalla.blit(bala_img, (eje_x + 16, eje_y + 10))


# Detectar una colisión
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia < 27:
        return True
    else:
        return False


def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (250, 200))


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

        # eventos nave
        if evento.type == pygame.KEYDOWN:  # esto se fija si hay una tecla presionada
            if evento.key == pygame.K_a:
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_d:
                jugador_x_cambio = +0.5
            if evento.key == pygame.K_SPACE:
                sonido_disparo = mixer.Sound('sonidos/disparo.mp3')
                sonido_disparo.set_volume(0.2)
                sonido_disparo.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -1.5
                }
                balas.append(nueva_bala)
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_a or evento.key == pygame.K_d:
                jugador_x_cambio = 0

    # cambiar ubicación nave jugador
    jugador_x += jugador_x_cambio
    # mantener dentro de la pantalla al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:  # 800px - 64px que es el tamaño del png de nave
        jugador_x = 736

    # cambiar ubicación nave enemigo
    for e in range(cant_enemigos):

        # fin del juego
        if enemigo_y[e] > jugador_y:
            for j in range(cant_enemigos):
                enemigo_y[j] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # mantener dentro de la pantalla al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.4
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:  # 800px - 64px que es el tamaño del png de nave
            enemigo_x_cambio[e] = -0.4
            enemigo_y[e] += enemigo_y_cambio[e]

        # colisiones
        for bala in balas:
            colision_bala_enemigo = hay_colision(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound('sonidos/Golpe.mp3')
                sonido_colision.set_volume(0.3)
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(50, 200)
                break

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento de la bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(bala_img, (bala["x"] + 16, bala["y"] + 10))
        if bala["y"] < 0:
            balas.remove(bala)

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    # actualizar
    pygame.display.update()
