import pygame
pygame.init

#WINDOW OBJECTS
SIZE = WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode(SIZE)
FPS = 60

#COLORS, FONTS
BACKGROUND = (10, 10, 10)

pygame.display.set_caption("Pong")

class Vector:
    x = 0
    y = 0
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def add_vector(self, vector: object):
        self.x = vector.x
        self.y = vector.y
        
    def bounce_x(self):
        self.x = -self.x
        
    def bounce_y(self):
        self.y = -self.y
        
        

class Ball:
    position = None
    velocity = None
    
    def __init__(self, position: list = None, velocity: list = None):
        if velocity is None:
            velocity = (0, 0)
            
        if velocity is None:
            velocity = (0, 0)
        
        self.position = position
        self.velocity = velocity
    

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