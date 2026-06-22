#importing relevant packages/libraries
import pygame
from random import randint
#Screen setup

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
#player direction and speed used for player movement
player_speed=300
#laser speed used for laser movement
laser_speed=500

surface=pygame.Surface((100,200))
surface.fill((70,70,70))

#imorting player and other useful stuff like stars and meteors for the background
player=pygame.image.load('../images/player.png').convert_alpha()
#assigning rec to player for collision detection and movement
player_rec=player.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-50))
#making it a vector so that we can use it to move the player around the screen
player_vec=pygame.math.Vector2()
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
     #player movement using velocity and frame rate to make it smooth and consistent across different devices
    keys=pygame.key.get_pressed()
    mouse=pygame.mouse.get_just_pressed()
    
    player_vec.x=int(keys[pygame.K_d])-int(keys[pygame.K_a])
    player_vec.y=int(keys[pygame.K_s])-int(keys[pygame.K_w])
    player_vec=player_vec.normalize() if player_vec else player_vec
    if keys[pygame.K_SPACE]:
        print("Shooting")
    if mouse[0]:
        print("Shooting")
        laser_vec.x=int(pygame.mouse.get_pos()[0]-laser_rec.centerx)
        laser_vec.y=int(pygame.mouse.get_pos()[1]-laser_rec.centery)
        #laser_vec=laser_vec.normalize() if laser_vec else laser_vec    
        laser_rec.center+=laser_vec*laser_speed*dt
   
    player_rec.center+=player_vec*player_speed*dt
   # print((player_vec*player_speed).magnitude())
    screen.fill((30,10,60))

    
    for star_x, star_y in star_pos:
        screen.blit(star, (star_x, star_y))
    screen.blit(meteor, meteor_rec)
    screen.blit(laser, laser_rec)
    
    
    


    screen.blit(player, player_rec)
    pygame.display.update()
pygame.quit()