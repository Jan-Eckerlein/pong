from cmath import rect
from re import X
from tokenize import Double
import pygame
import random
pygame.init

#WINDOW OBJECTS
SIZE = WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode(SIZE)
FPS = 60

#COLORS, FONTS
BACKGROUND = (10, 10, 10)

#GAMEPLAY SETTING
SPEEDSEEDER = [1, 5]
POSITIONSEEDER = [20, HEIGHT-20]
DEFAULTBALLDIM = 10

pygame.display.set_caption("Pong")

class Vector:
    x = float
    y = float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    
    # VECTOR MATH    
    def add_vector(self, vector: object):
        self.x = vector.x
        self.y = vector.y
        
    def scale(self, scalar: float):
        self.x = self.x * scalar
        
    # ACTIONS
    def bounce_x(self):
        self.x = -self.x
        
    def bounce_y(self):
        self.y = -self.y
        
        

class Ball:
    position = None
    velocity = None
    rect = None
    
    def __init__(self, position = Vector(0, 0), velocity = Vector(0, 0), width = DEFAULTBALLDIM, height = DEFAULTBALLDIM):
        self.position = position
        self.velocity = velocity
        self.rect = pygame.Rect(position.x, position.y, width, height)
        
    def update_rect_position(self):
        self.rect.x = self.position.x
        self.rect.y = self.position.y
        
    #SEEDERS
    def random_velocity(self, velocity_min = SPEEDSEEDER[0], velocity_max = SPEEDSEEDER[1]):        
        self.velocity.x = random.randrange(velocity_min, velocity_max)
        self.velocity.y = random.randrange(velocity_min, velocity_max)
        
    def random_position(self, position_min: int = POSITIONSEEDER[0], position_max: int = POSITIONSEEDER[1]):
        self.position.x = random.randrange(position_min, position_max)
        self.position.y = random.randrange(position_min, position_max)
        
    
    
    

def main():
    run = True
    clock = pygame.time.Clock()
    
    while run :
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            

        WIN.fill(BACKGROUND)
        pygame.display.update()
        
    pygame.quit

if __name__ == "__main__":
    main()