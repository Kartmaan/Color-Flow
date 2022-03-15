import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1024, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))

window.fill("white")

def update():
    pygame.display.update()

def create_circle(pos):
    """ Create circles with random color and radius at cursor position """
    r = random.randint(0, 255) # Red value
    g = random.randint(0, 255) # Green value
    b = random.randint(0, 255) # Blue value
    rad = random.randint(5, 10) # Circle's radius
    pygame.draw.circle(window, (r, g, b), pos, rad)

def run():
    pen_down = False # Does the cursor draw?
    run = True
    clock = pygame.time.Clock()
    fps = 30
    clock.tick(fps)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN: # Mouse click
                if pygame.mouse.get_pressed()[0]: #Left click
                    if pen_down == False:
                        pen_down = True # Cursor draws
                    else:
                        pen_down = False # Cursor doesn't draw

                if pygame.mouse.get_pressed()[2]: #Right click
                    window.fill("white") # Erase the screen

            if event.type == pygame.MOUSEMOTION: # When cursor move
                if pen_down:
                    pos = pygame.mouse.get_pos() # cursor coordinates
                    create_circle(pos)
        
        update()

    pygame.quit()

if __name__ == "__main__":
    run()