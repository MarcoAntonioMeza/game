import pygame
import sys
import random

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('audio/music2.mp3')
pygame.mixer.music.play(-1) 

clock = pygame.time.Clock()


#colors
RED = (255,0,0)

FPS = 60

#define game variables
GRAVITY = .55

#create game window
info = pygame.display.Info()
#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 432
SCREEN_WIDTH = info.current_w
SCREEN_HEIGHT = info.current_h
SCREEN_HEIGHT = SCREEN_HEIGHT - 80

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CompuActual Game")

icon = pygame.image.load('img/icono.png')  # o .png
pygame.display.set_icon(icon)


def draw_bgg():
    pygame.draw.line(screen, RED, (0, 370), (SCREEN_WIDTH, 370))


def draw_level(font,msg):
    text = font.render(msg, True, (0, 0, 0))  # Texto, antialiasing, color
    # Obtener el rectángulo del objeto de texto
    text_rect = text.get_rect()
    # Centrar el texto en la pantalla
    text_rect.center = (SCREEN_WIDTH // 2, 40)
    # Dibujar texto en la pantalla
    screen.blit(text, text_rect)

def mensaje(nvl):
    pygame.init()
    screen_msg = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #pygame.display.set_caption(f'Estas en el nivel {nvl}')
    
    def cargar(img):
        imagen = pygame.image.load(img)
        width = imagen.get_width()
        height = imagen.get_height()
        #print(f'width {width} height { height}')
        imagen = pygame.transform.scale(imagen, (width,height))
        return imagen
    
    esperar = True
    i = 1
    img = f"img/nvl-{nvl}/ser-{i}.png"
    while esperar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN  :
                if event.key == pygame.K_RETURN:
                    i+=1
                    img = f"img/nvl-{nvl}/ser-{i}.png"

        try:
            image = cargar(img)
            screen_msg.blit(image, (0, 0))
            pygame.display.flip()
        except:
            #pass
            esperar =  False
    
    return True
        


