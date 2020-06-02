import pygame
from pygame.locals import *
from asteroid import *

pygame.init()

# makes screen info and stuff
screen_info = pygame.display.Info()

# set size of game board to screen size
screen_size = (width, height) = (screen_info.current_w, screen_info.current_h)

# set screen to screen size
screen = pygame.display.set_mode(screen_size)

#color of background
color = (8, 8, 105)

#asteroids created
asteroids = pygame.sprite.Group() 

# game code
def main():
  #while true == will always run
  while True:

    #makes background color
    screen.fill(color)

    for event in pygame.event.get():
      if event.type == quit:
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
          asteroids.add(Asteroid(event.pos))
      
    
    for asteroid in asteroids:
      asteroid.update()
    for asteroid in asteroids:
      asteroid.draw(screen)

    #updates it
    pygame.display.flip()



#game loop
if __name__ == '__main__':
  main()  