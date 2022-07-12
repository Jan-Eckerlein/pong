import pygame
import random
pygame.init

#WINDOW OBJECTS
SIZE = WIDTH, HEIGHT = 900, 600
WIN = pygame.display.set_mode(SIZE)
FPS = 60

#COLORS, FONTS
BACKGROUND = (10, 10, 10)
WHITE = (255, 255, 255)

#GAMEPLAY SETTING
SPEEDSEEDER = [1, 5]
POSITIONSEEDER = [20, HEIGHT-20]

DEFAULTBALLDIM = 10

PADDLEOFFSET = 10
PADDLEVELOCITY = 10


pygame.display.set_caption("Pong")

class Vector:
    x = float
    y = float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        
    
    # VECTOR MATH    
    def add_vector(self, vector: object):
        self.x += vector.x
        self.y += vector.y
        
    def scale(self, scalar: float):
        self.x = self.x * scalar
        
    # ACTIONS
    def bounce_x(self):
        self.x *= -1
        
    def bounce_y(self):
        self.y *= -1

        
        

class Ball:
    position = None
    velocity = None
    rect = None
    
    def __init__(self, position = Vector(0, 0), velocity = Vector(0, 0), width = DEFAULTBALLDIM, height = DEFAULTBALLDIM):
        self.position = position
        self.velocity = velocity
        self.rect = pygame.Rect(position.x, position.y, width, height)
        
    #SEEDERS
    def random_velocity(self, velocity_min = SPEEDSEEDER[0], velocity_max = SPEEDSEEDER[1]):        
        self.velocity.x = random.randrange(velocity_min, velocity_max)
        self.velocity.y = random.randrange(velocity_min, velocity_max)
        
    def random_position(self, position_min: int = POSITIONSEEDER[0], position_max: int = POSITIONSEEDER[1]):
        self.position.x = random.randrange(position_min, position_max)
        self.position.y = random.randrange(position_min, position_max)
        
    #UPDATE
    def update_position(self):
        self.position.add_vector(self.velocity)
        
    def update_rect(self):
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)
        
        
    def update(self):
        self.update_position()
        self.update_rect()
        
        
    
class Paddle:
    rect: pygame.Rect
    offset = None
    velocity  = None
    location = 0
    max_location = 0
    
    def __init__(self, rect: pygame.Rect, offset = PADDLEOFFSET, velocity = PADDLEVELOCITY) -> None:
        self.rect = rect
        self.offset = offset
        self.velocity = velocity
        self.set_max_location()
        
    def set_max_location(self):
        self.max_location = HEIGHT - self.rect.height
    
    
def render(ball):
        WIN.fill(BACKGROUND)
        pygame.draw.rect(WIN, WHITE, ball.rect)
        pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()
    
    ball = Ball(Vector(WIDTH/4, HEIGHT/4), Vector(6, 2), 20, 20)
    
    
    while run :
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        if(ball.rect.left <= 0 or ball.rect.right >= WIDTH):
            ball.velocity.bounce_x()
            
        if(ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT):
            ball.velocity.bounce_y()
            
            
        ball.update()
        render(ball)
        
    pygame.quit

if __name__ == "__main__":
    main()