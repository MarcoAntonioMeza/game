from .screen import *
from .player import *


def caminos_nvl_1(img,img_vida):
    
    group = pygame.sprite.Group()
    zombie = pygame.sprite.Group()
    vida = pygame.sprite.Group()
    star = pygame.sprite.Group()

    
    image = 'img/trofeo.png'
    nvl1, nvl2,  = SCREEN_HEIGHT-50, SCREEN_HEIGHT//2-60
    scale = .15
    nvl  = 35
    tam = 40
    speed  = 0.6

    star.add(Star(SCREEN_WIDTH-90,nvl1-50,50,50,image))
    star.add(Star(0,nvl2-50,50,50,image))

    zombie.add(Enemy(250, nvl2-nvl, scale=scale, speed=speed))
    zombie.add(Enemy(1050, nvl2-nvl, scale=scale, speed=speed))
    zombie.add(Enemy(SCREEN_WIDTH//2, nvl2-nvl, scale=scale, speed=speed))
    #vida.add(Corazon(320,nvl1-tam,80,80,img_vida))
    for i in range(100,SCREEN_WIDTH,300):
        vida.add(Corazon(i+100,nvl1-tam,80,80,img_vida))
    for i in range(50,SCREEN_WIDTH,200):
        zombie.add(Enemy(i+120, nvl1-nvl, scale=scale, speed=speed))
        #vida.add(Corazon(i+100,nvl1-tam,80,80,img_vida))
        vida.add(Corazon(i+520,nvl2-tam,80,80,img_vida))
        
        #zombie.add(Player('enemy','zombie',i+150,nvl2-50, .2,0))
    
    
    group.add(Path(0,nvl1,img,SCREEN_WIDTH))
    group.add(Path(0,nvl2,img,SCREEN_WIDTH))
    #group.add(Path(0,nvl3 ,img,SCREEN_WIDTH))
    
    return group, zombie,vida,star
    


def caminos_nvl_3(img,img_vida):
    zombie = pygame.sprite.Group()
    vida = pygame.sprite.Group()
    star = pygame.sprite.Group()

    image = 'img/trofeo.png'
    nvl1, nvl2 = SCREEN_HEIGHT-50, SCREEN_HEIGHT//2-60
    scale = .15
    nvl  = 100
    tam = 40
    speed  = 0.6

    star.add(Star(SCREEN_WIDTH-90,nvl1-100,50,50,image))
    star.add(Star(0,nvl2-100,50,50,image))

    #zombie.add(Enemy(250, nvl2-nvl, scale=scale, speed=speed+.2))
    #zombie.add(Enemy(1050, nvl2-nvl, scale=scale, speed=speed+.2))
    vida.add(Corazon(320,nvl1-tam,80,80,img_vida))
    vida.add(Corazon(520,nvl2-tam,80,80,img_vida))
    
    #for i in range(50,SCREEN_WIDTH,400):
        #zombie.add(Enemy(i+120, nvl1-nvl, scale=scale, speed=speed+0.1))
        
        
    
    return star


def draw_leaf():
    leaf = pygame.sprite.Group()
    num_leaf  = 90
    leaves = [Leaf() for _ in range(num_leaf)]
    leaf.add(leaves)
    return leaf