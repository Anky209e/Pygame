import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))

# title 
pygame.display.set_caption("Animalopedia")

#icon
icon = pygame.image.load("Images\crab.png")
pygame.display.set_icon(icon)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    
    screen.fill((80,120,8))
    pygame.display.update()



