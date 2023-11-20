#from pygame.sprite import _Group
from .screen import *

class Player(pygame.sprite.Sprite):
  def __init__(self, char_type, name_char, x, y,scale,speed, enemy = None,vida = None,star = None):
    pygame.sprite.Sprite.__init__(self)
    self.speed = speed
    self.alive = True
    self.char_type = char_type
    self.name_char = name_char
    self.direction = 1
    self.vel_y = 0
    self.jump = False
    self.in_air = True
    self.flip = False
    self.update_time  = pygame.time.get_ticks()
    self.anition_list = []
    self.frame_index = 0
    self.action = 0

    self.nivel_piso = SCREEN_HEIGHT-50 

    #Vidas
    self.health = 3

    #Objetos para la colision
    self.vida = vida
    self.enemy= enemy
    self.star = star

    #Nivel
    self.nivel = 1
    
    self.pausa = False
    

    temp_list = []
    for i in range(2):
      img = pygame.image.load(f'img/{self.char_type}/character_{self.name_char}_idle{i}.png')
      img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
      temp_list.append(img)
    self.anition_list.append(temp_list)

    temp_list = []
    for i in range(3):
      img = pygame.image.load(f'img/{self.char_type}/character_{self.name_char}_run{i}.png')
      img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
      temp_list.append(img)
    self.anition_list.append(temp_list)

    temp_list = []
    for i in range(1):
      img = pygame.image.load(f'img/{self.char_type}/character_{self.name_char}_jump{i}.png')
      img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
      temp_list.append(img)
    self.anition_list.append(temp_list)


    self.image = self.anition_list[self.action][self.frame_index]
    self.rect = self.image.get_rect()
    #self.rect.center = (x, y)
    self.rect.y = y
    self.rect.x = x
    #self.rect.bottom = SCREEN_HEIGHT 

  def move(self,moving_left,moving_right):
    #reset movement variables
    dx = 0
    dy = 0

    #assign movement variables
    if moving_left:
      dx = -self.speed
      self.flip = True
      #self.direction = -1

    if moving_right:
      dx = self.speed
      self.flip = False
      #self.direction = 1
    
    # jump
    if self.jump and not self.in_air:
        self.vel_y = -12
        self.jump = False
        self.in_air = True
        pygame.mixer.Sound('audio/jump.wav').play()
    
    #apply gravity
    self.vel_y += GRAVITY
    if self.vel_y > 10:
      self.vel_y = 1
      #self.in_air = False
      #self.jump = True
    dy += self.vel_y

    #check for collision with floor
    a = (self.rect.bottom + dy > self.nivel_piso)
    if a:
      dy = self.nivel_piso - self.rect.bottom
      self.in_air = False  
          
    if self.enemy:
        collisions = pygame.sprite.spritecollide(self, self.enemy, True)
        if collisions:
            self.health-=1
            pygame.mixer.Sound('audio/zombie.mp3').play()

    if self.vida:
        collisions = pygame.sprite.spritecollide(self, self.vida, True)
        if collisions:
          self.health+=1
          pygame.mixer.Sound('audio/coin.mp3').play()
          
    if self.star:
        collisions = pygame.sprite.spritecollide(self, self.star,True)
        if collisions:  
          self.nivel+=1
          pygame.mixer.Sound('audio/ganar.mp3').play()
          self.pausa = True
          #if self.nivel >= 3:
            #self.star.draw(screen)
            
    #update rectangle position
    self.rect.x += dx
    self.rect.y += dy
    
    pygame.display.flip()


  def update_animation(self):
    if self.action == 0 or self.action == 2:#idle animation
      ANIMATION_COOLDOWN = 320
    else:
      ANIMATION_COOLDOWN = 60 
    #update image depending on current frame
    self.image = self.anition_list[self.action][self.frame_index]

    #check if enough time has passed since the last update
    if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN - self.speed:
      self.update_time = pygame.time.get_ticks()
      self.frame_index += 1
    #if the animation has run out reset back to the start
    if self.frame_index >= len(self.anition_list[self.action]):
      self.frame_index = 0


  def update_action(self, new_action):
    #check if the new action is different to the previous one
    if new_action != self.action:
      self.action = new_action
      #update the animation settings
      self.frame_index = 0
      self.update_time = pygame.time.get_ticks() 

  def draw(self):
    screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
    
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.vel_y = 0
        self.flip = False
        self.update_time = pygame.time.get_ticks()
        self.animation_list = []
        self.frame_index = 0
        self.action = 0

        temp_list = []
        for i in range(2):
            img = pygame.image.load(f'img/enemy/character_zombie_idle{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        temp_list = []
        for i in range(3):
            img = pygame.image.load(f'img/enemy/character_zombie_run{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        temp_list = []
        for i in range(1):
            img = pygame.image.load(f'img/enemy/character_zombie_jump{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def update_animation(self):
        if self.action == 0 or self.action == 2:  # idle animation
            ANIMATION_COOLDOWN = 320
        else:
            ANIMATION_COOLDOWN = 60

        #self.image = self.animation_list[self.action][self.frame_index]
        if 0 <= self.frame_index < len(self.animation_list[self.action]):
          self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN - self.speed:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0

    def follow_player(self, player):
        y_margin = 100  # Margen en el eje Y
        # Verifica si el jugador está dentro del margen en el eje Y
        if abs(self.rect.y - player.rect.y) <= y_margin:
            if self.rect.x < player.rect.x:
                self.rect.x += self.speed
                self.flip = False
                self.direction = 1
                self.action = 1  # Acción de correr hacia la derecha
            elif self.rect.x > player.rect.x:
                self.rect.x -= self.speed
                self.flip = True
                self.direction = -1
                self.action = 1  # Acción de correr hacia la izquierda
            else:
                self.action = 0  # Acción de estar quieto
        else:
            self.action = 0  # Acción de estar quieto

    def update(self, player):
        self.follow_player(player)
        self.update_animation()
        
    def draw(self):
      screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


class Path(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path, width=200, height=50):
        pygame.sprite.Sprite.__init__(self)
        original_image = pygame.image.load(image_path).convert_alpha()
        original_width, original_height = original_image.get_size()

        # Crear una nueva superficie del tamaño deseado
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        
        # Duplicar la imagen a lo largo del ancho
        for i in range(0, width, original_width):
            self.image.blit(original_image, (i, 0))

        self.rect = self.image.get_rect(topleft=(x, y))



class Corazon(pygame.sprite.Sprite):
  def __init__(self,x,y,alto,ancho,img,type='corazon'):
    pygame.sprite.Sprite.__init__(self)
    self.tipo = type
    self.img = img
    self.ancho = ancho
    self.alto = alto
    self.image = pygame.image.load(self.img)
    self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

class Star(pygame.sprite.Sprite):
  def __init__(self,x,y,alto,ancho,img):
    pygame.sprite.Sprite.__init__(self)
    self.img = img
    self.ancho = ancho
    self.alto = alto
    self.image = pygame.image.load(self.img)
    self.image = pygame.transform.scale(self.image, (self.ancho, self.alto))
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

  def reset_star_position(self):
    self.rect.x = self.rect.x
    self.rect.y = self.rect.y