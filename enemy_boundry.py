import pygame
from pygame.constants import KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_UP
import random
pygame.init()
#---------------------------------------------

SCREEN_WIDTH = 599
SCREEN_HEIGHT = 401
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# title 
pygame.display.set_caption("Anim0")

#icon
icon = pygame.image.load("Images\crab.png")
pygame.display.set_icon(icon)
#--------------Enemy-------------------
enemy_img = pygame.image.load(r"Images\clown-fish.png")
enemy_x = random.randint(0,585)
enemy_y = random.randint(0,399)




def enemy(x,y):
    screen.blit(enemy_img,(x,y))









#---------------player--------------------------
# player image 

player_img = pygame.image.load(r"Images\crab2128.png")
player_x = 300
player_y = 200
playerx_change = 0
# dont overap--------------
if (enemy_x == player_x-128 and enemy_y == player_y-128):
    print("recalibrtaing")
    enemy_x = random.randint(0,580)
    enemy_y = random.randint(0,395)



#------------------

def player(x,y):
    
    screen.blit(player_img,(x,y))

#bg image
bg_img = pygame.image.load(r"Images\grass.png")
running = True
#--------------------loop----------------------
while running:
    
    for event in pygame.event.get():
        #--------keybinds------------
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                playerx_change = -0.9
            if event.key == K_RIGHT:
                playerx_change = 0.9
            if event.key == K_UP:
                player_y -= 8
            if event.key == K_DOWN:
                player_y += 8

        if event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                playerx_change = 0
                
            if event.key == K_RIGHT:
                playerx_change = 0
            

            
    
    screen.blit(bg_img,(0,0))
    #------boundries------
    player_x += playerx_change
    if player_x <=0:
        player_x = 1
    elif player_x >= 475:
        player_x = 473
    elif player_y <=0:
        player_y = 0
    elif player_y >=288:
        player_y = 287
    #-----------------------
    
    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
        
        
    

    pygame.display.update()