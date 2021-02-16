import pygame
pygame.init()

screen = pygame.display.set_mode((801,601))

# title 
pygame.display.set_caption("Animalopedia")

#icon
icon = pygame.image.load("Images\crab.png")
pygame.display.set_icon(icon)

# player image
player_img = pygame.image.load(r"Images\bee.png")

player_x = 370
player_y = 300

#background image

bg_img = pygame.image.load(r"Images\bgimage.png")


def player():
    screen.blit(player_img,(player_x,player_y))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    screen.fill((80,120,8))
    screen.blit(bg_img,(0,0))
    player()
    pygame.display.update()



