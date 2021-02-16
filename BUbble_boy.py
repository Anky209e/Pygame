import pygame
from pygame.constants import KEYDOWN, K_DOWN, K_LEFT, K_RIGHT, K_UP
from pygame import mixer
import random
import math
pygame.init()
#--------------------------------------------

SCREEN_WIDTH = 600
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
enemy_y = 100
enemy_xchange = 0.3
enemy_ychange = 0.2

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
    enemy_y = 395
#------------------collision
def isCollision(enemy_x,enemy_y,player_x,player_y):
    distance = math.sqrt(math.pow(enemy_x-player_x,2)+math.pow(enemy_y-player_y,2))
    
    if distance <=random.randint(49,59):
        return True
    else:
        return False

#------------Game over text-----------

def gameOver():
    global score_value
    game_overfnt = font.render("GAME OVER",True,(8,8,239))
    screen.blit(game_overfnt,(200,150))
    score_value = 0


#------------------------------
# back ground sound
mixer.music.load(r"sounds\bgm.wav")
mixer.music.play(-1)

#-----------SCORE-------------
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

def ShowScore(x,y):
    score = font.render("Score: "+str(score_value),True,(248,3,3))
    screen.blit(score,(x,y))



#----------------------------

def player(x,y):
    
    screen.blit(player_img,(x,y))

#bg image
bg_img = pygame.image.load(r"Images\sea.png")
running = True
#--------------------loop----------------------
while running:
    
    for event in pygame.event.get():
        #--------keybinds------------
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                playerx_change = -0.5
            if event.key == K_RIGHT:
                playerx_change = 0.5
            if event.key == K_UP:
                player_y -= random.randint(3,10)
            if event.key == K_DOWN:
                player_y += random.randint(3,10)

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
    enemy_x += enemy_xchange
    enemy_y += enemy_ychange
    if enemy_x <=0:
        enemy_xchange = 0.2
    elif enemy_x >= 475:
        enemy_xchange = -0.2
    elif enemy_y <=0:
        enemy_ychange = 0.2
    elif enemy_y >=288:
        enemy_ychange = -0.2
    
    player(player_x,player_y)
    enemy(enemy_x,enemy_y)
    collision = isCollision(enemy_x,enemy_y,player_x,player_y)
    if collision:
        mixer.Sound(r"sounds\hit.wav").play()

        score_value +=1
        enemy_x = random.randint(0,580)
        enemy_y = 100
        player_x = 300
        player_y = 200
    if enemy_y >=200:
        gameOver()

        
        
    
    ShowScore(textX,textY)
    pygame.display.update()
