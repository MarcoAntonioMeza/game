import pygame


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

def mensaje(msg):
    screen_msg = pygame.display.set_mode(SCREEN_HEIGHT,SCREEN_HEIGHT)
    pygame.display.set_caption('')