from Clases.screen import *
from Clases.player import *
from Clases.caminos import *

clock = pygame.time.Clock()

x = 400
y = 343
scale = .2

#define game variables
scroll = 0

bg_images = []
for i in range(1, 5):
  bg_image = pygame.image.load(f"img/bg/plx-{i}.png").convert_alpha()
  bg_image =pygame.transform.smoothscale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def draw_bg():
  for x in range(10):
    speed = 0
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed+2, 0))
      speed += 0.1 

def  main():
  global scroll 
  #Nivel 1 y dos
  camino,zombie,vida,star = caminos_nvl_1('img/ground.png','img/corazon.png')
  star2,enemy,vida2=caminos_nvl_3('img/ground.png','img/corazon.png')
  player = Player('character','maleAdventurer',50,
                  SCREEN_HEIGHT-50, .2, 3,
                  enemy=zombie,vida=vida, star=star
                  )
  moving_left = False
  moving_right = False

  #leaf
  leaves = draw_leaf()

  #mensaje(player.nivel)


  # Configuración de la fuente
  letra = pygame.font.Font(None, 56)
  
  #game loop
  run = True
  is_paused = not mensaje(player.nivel)
  while run:
    if player.nivel == 5:
      #is_paused = False 
      mensaje(5)
      pygame.time.delay(1000)
      pygame.quit()
      sys.exit()

    if player.health <= 0:
        mensaje(6)
        main()
        return
    if  not is_paused:
      is_paused = player.pausa
      clock.tick(FPS)
      #draw world
      draw_bg()
      player.update_animation()
      leaves.draw(screen)
      player.draw()
      camino.draw(screen)
      vida.draw(screen)
      star.draw(screen)
      leaves.update()


      #draw msg
      msg = f'Nivel {player.nivel}  Vidas: {player.health}'
      draw_level(letra,msg)
      #zombie.draw(screen)
      if  player.nivel % 2   == 0:
        player.nivel_piso = SCREEN_HEIGHT//2-55
      else:
        player.nivel_piso = SCREEN_HEIGHT-50
      

      nvl = player.nivel
      if nvl <= 2:
        for i in zombie:
          if nvl == 2:
            i.update(player)
          i.update_animation()
          i.draw()
      elif nvl >=3 and nvl <=4:
        zombie.empty()
        vida.empty()

        for i in enemy:
          if nvl == 3:
            i.speed = .9
            player.speed = 3.5
            #player.speed +=
          elif nvl == 4:
            player.speed = 3.6
            i.speed = 3

            #player.speed += 1
          i.update(player)
          i.update_animation()
          i.draw()
          
          star2.draw(screen)
          enemy.draw(screen)
          vida2.draw(screen)
          #pygame.time.delay(500)
          #player.rect.y = 1
          player.star = star2
          player.enemy = enemy
          player.vida = vida2
        
        #star.draw(screen)
      #update player actions
      if player.alive:
        if player.in_air:
          player.update_action(2) #2 means jump
        elif moving_left or moving_right:
          player.update_action(1)#1 means walk
        else:
          player.update_action(0)#0 means idle

      player.move(moving_left,moving_right)
      
      
      #screen.fill((0, 0, 0))
      #get keypresses Animation
      key = pygame.key.get_pressed()
      if key[pygame.K_a] and scroll > 0:
        scroll -= 2
      if key[pygame.K_d] and scroll < 1000:
        scroll += 2

      #event handlers
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
        #Keyboard presses 
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a:
            moving_left = True
          if event.key == pygame.K_d:
            moving_right = True
          if event.key == pygame.K_w and player.alive and player.in_air == False:
            player.jump = True  
          if event.key == pygame.K_ESCAPE:
            run = False
            
        #Keyboard button released
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_a:
            moving_left = False
          if event.key == pygame.K_d:
            moving_right = False

      pygame.display.update()
      pygame.display.flip()
    
    else:
      is_paused = not  mensaje(player.nivel)
      player.pausa = False
      moving_left = False
      moving_right = False
  pygame.quit()

def reiniciar_juego():
    pygame.time.delay(1000) 
    main()


if __name__ == '__main__':  
  main()