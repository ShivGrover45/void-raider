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
player_direction=-1
player_speed=10

surface=pygame.Surface((100,200))
surface.fill((70,70,70))

#imorting player and other useful stuff like stars and meteors for the background
player=pygame.image.load('../images/player.png').convert_alpha()
player_rec=player.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT-50))
player_vec=pygame.math.Vector2(x=20,y=-10)
star=pygame.image.load('../images/star.png').convert_alpha()
star_pos=[(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for x in range(50)]
meteor=pygame.image.load('../images/meteor.png').convert_alpha()
meteor_rec=meteor.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
#importing laser and as of now just putting it in the middle of the screen, will change later
laser=pygame.image.load('../images/laser.png').convert_alpha()
laser_rec=laser.get_frect(center=(WINDOW_WIDTH-30, WINDOW_HEIGHT-50))
#game loop
while running:
    dt=clock.tick()/1000
    #cls
    # print(clock.get_fps())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill((30,10,60))
    print(pygame.mouse.get_pressed())  

    
    for star_x, star_y in star_pos:
        screen.blit(star, (star_x, star_y))
    screen.blit(meteor, meteor_rec)
    screen.blit(laser, laser_rec)
    keys=pygame.key.get_pressed()
    #player movement using velocity and frame rate to make it smooth and consistent across different devices
    player_rec.center+=player_vec*player_speed*dt
    #input handling for player movement using wasd keys for ship and mouse for shooting and ensure the player doesn't go out of bounds
    #speed increase cz its too slow
    if keys[pygame.K_a] and player_rec.left > 0:
        player_vec.x=-1
    elif keys[pygame.K_d] and player_rec.right < WINDOW_WIDTH:
        player_vec.x=1
    else:
        player_vec.x=0

    screen.blit(player, player_rec.topleft)
    pygame.display.update()
pygame.quit()