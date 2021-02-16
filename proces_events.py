import pygame
from pygame.constants import K_DOWN

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


#---------------------------

pygame.init()

# constant for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# creating screen

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# running our main loop.

running = True

while running:

    # looking at events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            
            if event.key == K_ESCAPE:
                running = False

        # close button
        elif event.type == QUIT:
            running = False
