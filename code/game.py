#importing relevant packages/libraries
import pygame
from random import randint
from pygame.sprite import Sprite,Group
#Screen setup

class Player(Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.image=pygame.image.load('../images/player.png').convert_alpha()
        self.rect=self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-50))
        self.direction=pygame.math.Vector2()
        self.speed=300
    def update(self,dt):
        #print("Ship is moving")
        #Ship movement using Object Oriented Programming
        keys=pygame.key.get_pressed()
        #player vector for movement, using the direction vector to move the player
        player_vec=self.direction
        player_vec.x=int(keys[pygame.K_d])-int(keys[pygame.K_a])
        player_vec.y=int(keys[pygame.K_s])-int(keys[pygame.K_w])
        #normalizing the vector to avoid diagonal speed boost
        player_vec=player_vec.normalize() if player_vec else player_vec
        self.rect.center+=player_vec*self.speed*dt
        #checking recent mouse click for shooting the laser
        recent_click=pygame.mouse.get_just_pressed()
        if recent_click[0]:
            print("Laser fired")
 


pygame.init()

clock=pygame.time.Clock()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
screen=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
running = True
#game frame setup
logo=pygame.image.load('../void raider.png')
pygame.display.set_caption('Void Raider')
pygame.display.set_icon(logo)


x=100
y=175
#just in case if i require speed and direction for player movement



surface=pygame.Surface((100,200))
surface.fill((70,70,70))

#creating player using sprite class
sprites=Group()
player=Player(sprites)

star=pygame.image.load('../images/star.png').convert_alpha()
star_pos=[(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for x in range(50)]
meteor=pygame.image.load('../images/meteor.png').convert_alpha()
meteor_rec=meteor.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
#importing laser and as of now just putting it in the middle of the screen, will change later
laser=pygame.image.load('../images/laser.png').convert_alpha()
laser_rec=laser.get_frect(center=(WINDOW_WIDTH-30, WINDOW_HEIGHT-50))
#vector for laser movement (straight line movement)
laser_vec=pygame.math.Vector2(0, -1)
#game loop
while running:
    dt=clock.tick()/1000
    #cls
    # print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    
 

    sprites.update(dt)


   # print((player_vec*player_speed).magnitude())
    screen.fill((30,10,60))

    
    for star_x, star_y in star_pos:
        screen.blit(star, (star_x, star_y))
    screen.blit(meteor, meteor_rec)
    screen.blit(laser, laser_rec)

    sprites.draw(screen)
    
    pygame.display.update()
pygame.quit()