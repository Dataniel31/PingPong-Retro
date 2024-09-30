import pygame as pg
import pygame_textinput

# Configurar el ancho y alto de la pantalla
ANCHO_PANTALLA = 900
ALTO_PANTALLA = 600
pantalla = pg.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# Cambiar el titulo y el icono de la pantalla
pg.display.set_caption("Pong")
icono = pg.image.load("pong.png")
pg.display.set_icon(icono)

# Variables de inicializacion
ejecutando = True
mi_reloj = pg.time.Clock()

# Paleta de colores
BLANCO = (255, 255, 255)
COLOR_FONDO = (150, 200, 170)
AZUL = (70, 130, 180)
ROJO = (200, 70, 90)
NEGRO = (0, 0, 0)

# Definir sonidos
pg.mixer.init()
sonido_golpe_paleta = pg.mixer.Sound("golpe_paleta.mp3")
sonido_golpe_pared = pg.mixer.Sound("golpe_pared.mp3")
sonido_punto = pg.mixer.Sound("punto.mp3")
sonido_golpe_paleta.set_volume(.5)
sonido_golpe_pared.set_volume(.5)
sonido_punto.set_volume(.5)

# Coordenadas y tamaños de jugadores
j1_x = 50
j1_y = 250
j2_x = 820
j2_y = 250
ANCHO_PALETA = 30
ALTO_PALETA = 100

# Coordenadas y dimensiones de la pelota
pelota_x = 450
pelota_y = 300
ANCHO_PELOTA = 10
ALTO_PELOTA = 10
pelota_diferencia_x = 4
pelota_diferencia_y = 4

# Puntajes iniciales
puntos_j1 = 0
puntos_j2 = 0

# Definir las fuentes
pg.font.init()
calibri_bold_35 = pg.font.SysFont("Calibri Bold", 35)
calibri_bold_25 = pg.font.SysFont("Calibri Bold", 25)
calibri_bold_120 = pg.font.SysFont("Calibri Bold", 120)

# Crear los elementos
paleta_j1 = pg.Rect(j1_x, j1_y, ANCHO_PALETA, ALTO_PALETA)
paleta_j2 = pg.Rect(j2_x, j2_y, ANCHO_PALETA, ALTO_PALETA)
pelota = pg.Rect(pelota_x, pelota_y, ANCHO_PELOTA, ALTO_PELOTA)


def dibujar_pantalla():
    pantalla.fill(COLOR_FONDO)
    pg.draw.rect(pantalla, AZUL, paleta_j1)
    pg.draw.rect(pantalla, ROJO, paleta_j2)
    pg.draw.rect(pantalla, BLANCO, pelota)
    texto_puntos_j1 = calibri_bold_35.render("PUNTOS J1: " + str(puntos_j1), True, AZUL)
    texto_puntos_j2 = calibri_bold_35.render("PUNTOS J2: " + str(puntos_j2), True, ROJO)
    pantalla.blit(texto_puntos_j1, (130, 20))
    pantalla.blit(texto_puntos_j2, (620, 20))


def mostrar_menu_inicial():
    pantalla.fill(NEGRO)

    titulo = calibri_bold_120.render("PONG", True, BLANCO)
    icono_escalado = pg.transform.scale(icono, (titulo.get_height(), titulo.get_height()))

    pantalla.blit(titulo, (ANCHO_PANTALLA // 2 - titulo.get_width() // 2, ALTO_PANTALLA // 2 - 200))
    pantalla.blit(icono_escalado, (ANCHO_PANTALLA // 2 + titulo.get_width() // 2 + 10, ALTO_PANTALLA // 2 - 200))

    mensaje_inicio = calibri_bold_35.render("¿A cuántos puntos jugamos esta partida?", True, BLANCO)
    pantalla.blit(mensaje_inicio, (ANCHO_PANTALLA // 2 - mensaje_inicio.get_width() // 2, ALTO_PANTALLA // 2 - 100))

    # Crear el campo de texto
    textinput = pygame_textinput.TextInputVisualizer()
    clock = pg.time.Clock()

    while True:
        pantalla.fill(NEGRO)
        pantalla.blit(titulo, (ANCHO_PANTALLA // 2 - titulo.get_width() // 2, ALTO_PANTALLA // 2 - 200))
        pantalla.blit(icono_escalado, (ANCHO_PANTALLA // 2 + titulo.get_width() // 2 + 10, ALTO_PANTALLA // 2 - 200))
        pantalla.blit(mensaje_inicio, (ANCHO_PANTALLA // 2 - mensaje_inicio.get_width() // 2, ALTO_PANTALLA // 2 - 100))

        # Renderizar el campo de texto
        pantalla.blit(textinput.surface, (ANCHO_PANTALLA // 2 - 50, ALTO_PANTALLA // 2 + 50))

        # Actualizar los eventos
        eventos = pg.event.get()
        for e in eventos:
            if e.type == pg.QUIT:
                pg.quit()
                quit()

        # Actualizar el campo de texto
        textinput.update(eventos)

        # Si se presiona Enter, verificar el valor
        if textinput.value.isdigit() and pg.key.get_pressed()[pg.K_RETURN]:
            puntos_para_ganar = int(textinput.value)
            if puntos_para_ganar > 0:
                return puntos_para_ganar

        pg.display.flip()
        clock.tick(30)


def verificar_ganador():
    if puntos_j1 >= puntos_para_ganar:
        return "Jugador 1"
    elif puntos_j2 >= puntos_para_ganar:
        return "Jugador 2"
    return None


def mostrar_ganador():
    pantalla.fill(NEGRO)
    mensaje = calibri_bold_25.render("¡Ha ganado " + ganador + "!", True, BLANCO)
    pantalla.blit(mensaje, (ANCHO_PANTALLA // 2 - mensaje.get_width() // 2, ALTO_PANTALLA // 2 - 100))

    mensaje_reinicio = calibri_bold_25.render("¿Quieres volver a jugar?", True, BLANCO)
    pantalla.blit(mensaje_reinicio, (ANCHO_PANTALLA // 2 - mensaje_reinicio.get_width() // 2, ALTO_PANTALLA // 2))

    mensaje_si = calibri_bold_25.render("SÍ (s)", True, BLANCO)
    pantalla.blit(mensaje_si, (ANCHO_PANTALLA // 2 - 100, ALTO_PANTALLA // 2 + 50))

    mensaje_no = calibri_bold_25.render("NO (n)", True, BLANCO)
    pantalla.blit(mensaje_no, (ANCHO_PANTALLA // 2 + 50, ALTO_PANTALLA // 2 + 50))

    pg.display.flip()
    while True:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
                quit()
            if e.type == pg.KEYDOWN:
                if e.key == pg.K_s:
                    return True
                if e.key == pg.K_n:
                    return False
        mi_reloj.tick(10)


def resetaer_pelota_y_paletas():
    global pelota_x, pelota_y, pelota_diferencia_x, pelota_diferencia_y, j1_y, j2_y
    pelota_x = 450
    pelota_y = 300
    pelota_diferencia_x = 4
    pelota_diferencia_y = 4
    j1_y = 250
    j2_y = 250


# Loop principal
while ejecutando:

    # Mostrar el menu inicial
    puntos_para_ganar = mostrar_menu_inicial()
    jugando = True

    while jugando:

        # Verificar cierre del juego
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                ejecutando = False
                jugando = False
                break
        if not ejecutando:
            break

        # Definir el evento al presionarse cualquier tecla
        teclas = pg.key.get_pressed()

        # Actualizar posiciones de elementos
        paleta_j1.y = j1_y
        paleta_j2.y = j2_y
        pelota.x = pelota_x
        pelota.y = pelota_y

        # Redefinir coordenadas paletas
        if teclas[pg.K_w] and j1_y > 0:
            j1_y -= 5
        elif teclas[pg.K_s] and j1_y + ALTO_PALETA < ALTO_PANTALLA:
            j1_y += 5

        if teclas[pg.K_UP] and j2_y > 0:
            j2_y -= 5
        elif teclas[pg.K_DOWN] and j2_y + ALTO_PALETA < ALTO_PANTALLA:
            j2_y += 5

        # Redefinir las coordenadas de la pelota
        pelota_x += pelota_diferencia_x
        pelota_y += pelota_diferencia_y

        # Verificar colisiones en cada movimiento
        if pelota.colliderect(paleta_j1):
            sonido_golpe_paleta.play()
            pelota_diferencia_x = abs(pelota_diferencia_x)
        elif pelota.colliderect(paleta_j2):
            sonido_golpe_paleta.play()
            pelota_diferencia_x = abs(pelota_diferencia_x) * -1
        elif pelota_y <= 0:
            sonido_golpe_pared.play()
            pelota_diferencia_y = abs(pelota_diferencia_y)
        elif pelota_y >= ALTO_PANTALLA:
            sonido_golpe_pared.play()
            pelota_diferencia_y = abs(pelota_diferencia_y) * -1
        elif pelota_x <= 0 or pelota_x >= ANCHO_PANTALLA:
            sonido_punto.play()
            if pelota_x >= ANCHO_PANTALLA:
                puntos_j1 += 1
            elif pelota_x <= 0:
                puntos_j2 += 1

            # Verificar si hay un ganador antes de resetear la pantalla
            ganador = verificar_ganador()
            if ganador:
                # Preguntar di quieren volver a jugar
                # Si ganador regresa con False
                if not mostrar_ganador():
                    ejecutando = False
                    jugando = False
                    break
                # Si "ganador" regresa con True
                else:
                    # Si decide volver a jugar reiniciar puntos, y continuar
                    puntos_j1 = 0
                    puntos_j2 = 0
                    resetaer_pelota_y_paletas()
                    break
            resetaer_pelota_y_paletas()

        dibujar_pantalla()

        pg.display.flip()
        mi_reloj.tick(60)

pg.quit()
quit()
