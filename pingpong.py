import pygame as pg

# Configurar el ancho y alto de la pantalla (Constantes)
ANCHO_PANTALLA = 900
ALTO_PANTALLA = 600
pantalla = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# titulo y el icono de la pantalla
pg.display.set_caption('PingPong')
icono = pg.image.load('Pong.png')
pg.display.set_icon(icono)

# variable de inicializacion
ejecutando = True
reloj = pg.time.Clock()

# Paleta de colores
BLANCO = (255, 255, 255)
COLOR_FONDO = (150, 200, 170)
AZUL = (70, 130, 180)
ROJO = (200, 70, 90)

# Coordenadas | Tamaño de jugadores
j1_x = 50
j1_y = 250
j2_x = 820
j2_y = 250
ANCHO_PALETA = 30
ALTO_PALETA = 100

# Coordenadas y dimensiones de la paleta
pelota_x = 450
pelota_y = 300
ANCHO_PELOTA = 12
ALTO_PELOTA = 12

# Crear los elementos
paleta_j1 = pg.Rect(j1_x, j1_y, ANCHO_PALETA, ALTO_PALETA)
paleta_j2 = pg.Rect(j2_x, j2_y, ANCHO_PALETA, ALTO_PALETA)
pelota = pg.Rect(pelota_x, pelota_y, ANCHO_PELOTA, ALTO_PELOTA)


def dibujar_pantalla():
    pantalla.fill(COLOR_FONDO)
    pg.draw.rect(pantalla, AZUL, paleta_j1)
    pg.draw.rect(pantalla, ROJO, paleta_j2)
    pg.draw.rect(pantalla, BLANCO, pelota)


# loop principal
while ejecutando:
    # verificar el cierre del juego
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            ejecutando = False

    dibujar_pantalla()

    pg.display.flip()
    reloj.tick(60)

pg.quit()  # Limpiar recursos
quit()  # Cerrar programa
