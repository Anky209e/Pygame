import pygame
from pygame.constants import KEYDOWN

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        else:
    
            screen.fill((34,31,30))

            # creating a surface and giving its width and height
            surf = pygame.Surface((70,70))

            # giving surface a color
            surf.fill((107,247,17))
            rect = surf.get_rect()

            # drawing surf on screen
            screen.blit(surf,(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
            pygame.display.flip()
        
pygame.quit()