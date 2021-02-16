import pygame
from pygame.constants import KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_UP

pygame.init()

SCREEN_WIDTH = 599
SCREEN_HEIGHT = 401
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# player image 

player_img = pygame.image.load(r"Images\crab2128.png")
player_x = 300
player_y = 200
playerx_change = 0

def player(x,y):
    
    screen.blit(player_img,(x,y))

#bg image
bg_img = pygame.image.load(r"Images\grass.png")
running = True

while running:
    
    for event in pygame.event.get():
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

    player_x += playerx_change
    
    player(player_x,player_y)
        
        
    

    pygame.display.update()