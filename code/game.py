#importing relevant packages/libraries
import pygame
from random import randint,uniform
from pygame.sprite import Sprite,Group
#Screen setup

class Player(Sprite):
    def __init__(self,groups):
        super().__init__(groups)
        self.image=pygame.image.load('../images/player.png').convert_alpha()
        self.rect=self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-50))
        self.direction=pygame.math.Vector2()
        self.speed=300


        #cooldown for shooting the laser, to avoid spamming the laser
        self.shoot=True
        self.laser_shoot_time=0
        self.cooldown_period=500 #in milliseconds
        
    
    def laser_time(self):
        
        if not self.shoot:
            current_time=pygame.time.get_ticks()
            #print(current_time)
        #logic for cooldown for shooting the laser, to avoid spamming the laser
            if current_time-self.laser_shoot_time>=self.cooldown_period:
              self.shoot=True
              print("Laser can be fired again")

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
        if recent_click[0] and self.shoot:
           # print("Laser fired")
            Laser((sprites,laser_sprites), laser, self.rect.midtop)
            self.shoot=False
            self.laser_shoot_time=pygame.time.get_ticks()
        self.laser_time()


 #Sprite class for stars in the background, just for aesthetic purposes
class Stars(Sprite):
    def __init__(self,groups,surf):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))
   
#Laser class for shooting the laser
class Laser(Sprite):
    def __init__(self,groups,surf,pos):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_frect(midbottom=pos)
    def update(self,dt):
        #moving the laser in y-axis
        self.rect.centery-=300*dt
        if self.rect.bottom<0:
            self.kill()

#Meteor class for meteor movement in random sides
class Meteor(Sprite):
    def __init__(self,groups,surf,pos):
        super().__init__(groups)
        self.image=surf
        self.rect=self.image.get_frect(topleft=pos)
        self.direction=pygame.Vector2(uniform(-0.5,0.5),1)
        self.speed=150
    def update(self,dt):
        #moving the meteor in y-axis
        self.rect.center+=self.direction*self.speed*dt
        if self.rect.top>WINDOW_HEIGHT:
            self.kill()


def collisions():
    #testing collision between laser and meteor
    collisions=pygame.sprite.groupcollide(laser_sprites,meteor_sprites,True,True)


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
meteor_sprites=Group()
laser_sprites=Group()
star_surf=pygame.image.load('../images/star.png').convert_alpha()
for i in range(50):
    Stars(sprites,star_surf)

player=Player(sprites)


meteor=pygame.image.load('../images/meteor.png').convert_alpha()
meteor_rec=meteor.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
#importing laser and as of now just putting it in the middle of the screen, will change later
laser=pygame.image.load('../images/laser.png').convert_alpha()



#custom event for meteor movement 
meteor_event=pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 1000)


#game loop
while running:
    dt=clock.tick()/1000
    #cls
    # print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==meteor_event:
            Meteor((sprites,meteor_sprites),meteor,(randint(0,WINDOW_WIDTH),randint(-150,-100)))


    sprites.update(dt)
    collisions()



   # print((player_vec*player_speed).magnitude())
    screen.fill((30,10,60))

    #screen.blit(meteor, meteor_rec)

    sprites.draw(screen)
    
    pygame.display.update()
pygame.quit()