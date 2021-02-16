import pygame

pygame.init()

# setting up display

screen = pygame.display.set_mode([500,500])

# running until user ask to quit
running = True

while running:

    #cheking for user to click close window button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #filling backgroung with white    
    screen.fill((21,9,7))

    # drawing s circle
    pygame.draw.circle(screen,(0,0,255),(250,250),75)

    # updating our display(imp.)
    pygame.display.flip()

# time to quit!
pygame.quit()
