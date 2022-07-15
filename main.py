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
PADDLE_VELOCITY = 10


#USER EVENTS
LEFT_LOST = pygame.USEREVENT + 1
RIGHT_LOST= pygame.USEREVENT + 2


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
        
    def random(self, min: float=0, max: float=1):
        self.random_x(self, min, max)
        self.random_y(self, min, max)
        
    def random_x(self, min: float=0, max: float=1):
        self.x = random.randrange(min, max)
        
    def random_y(self,min: float=0, max: float=1):
        self.y = random.randrange(min, max)
        
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
    def center_ball(self):
        self.position.x = float(WIDTH/2) 
        self.position.y = float(HEIGHT/2)
        self.update
    
    def update_position(self):
        self.position.add_vector(self.velocity)
        
    def update_rect(self):
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y)
        
        
    def update(self):
        self.update_position()
        self.update_rect()
        
    def handle_collision(self, paddle_left, paddle_right):
        
        if(self.rect.left <= 0):
            pygame.event.post(pygame.event.Event(LEFT_LOST))
            
            
        if(self.rect.right >= WIDTH):
            pygame.event.post(pygame.event.Event(RIGHT_LOST))
            
        if(self.rect.top <= 0 or self.rect.bottom >= HEIGHT):
            self.velocity.bounce_y()
            
        for paddle in (paddle_left, paddle_right):
            if paddle.rect.colliderect(self.rect):
                self.velocity.bounce_x()
                self.velocity.y += paddle.velocity * 0.5
        
        
    
class Paddle:
    rect: pygame.Rect
    offset = None
    velocity  = None
    location = 0
    max_location = 0
    
    def __init__(self, rect: pygame.Rect, velocity = PADDLE_VELOCITY) -> None:
        self.rect = rect
        self.velocity = velocity
        self.set_max_location()
        
    def set_max_location(self):
        self.max_location = HEIGHT - self.rect.height
    
    
def move_paddle_left(keys_pressed, paddle: Paddle) : 
    if keys_pressed[pygame.K_w] and (paddle.rect.top - PADDLE_VELOCITY) >= 0: #UP
        paddle.rect.y -= PADDLE_VELOCITY
        paddle.velocity = -PADDLE_VELOCITY
    if keys_pressed[pygame.K_s] and (paddle.rect.bottom + PADDLE_VELOCITY) <= HEIGHT: #DOWN
        paddle.rect.y += PADDLE_VELOCITY
        paddle.velocity = PADDLE_VELOCITY
    
def move_paddle_right(keys_pressed, paddle: Paddle) : 
    if keys_pressed[pygame.K_UP] and (paddle.rect.top - PADDLE_VELOCITY) >= 0: #UP
        paddle.rect.y -= PADDLE_VELOCITY
        paddle.velocity = -PADDLE_VELOCITY
    if keys_pressed[pygame.K_DOWN] and (paddle.rect.bottom + PADDLE_VELOCITY) <= HEIGHT: #DOWN
        paddle.rect.y += PADDLE_VELOCITY
        paddle.velocity = PADDLE_VELOCITY
    
def render(ball: Ball, paddles: (Paddle)):
        WIN.fill(BACKGROUND)
        pygame.draw.rect(WIN, WHITE, ball.rect)
        
        for paddle in paddles:
            pygame.draw.rect(WIN, WHITE, paddle)
            
        pygame.display.update()
        
def seconds(seconds):
    return seconds * FPS

def main():
    run = True
    wait = None
    clock = pygame.time.Clock()
    
    ball = Ball(Vector(WIDTH/2, HEIGHT/2), Vector(6, 2), 20, 20)
    paddle_left = Paddle(pygame.Rect(PADDLEOFFSET, 0, 20, 80))
    paddle_right = Paddle(pygame.Rect(WIDTH - PADDLEOFFSET - 10, 0, 20, 80))
    
    while run :
        clock.tick(FPS)
        
        for paddle in (paddle_left, paddle_right):
            paddle.velocity = 0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type == RIGHT_LOST:
                print("right lost")
                ball.center_ball()
                wait = seconds(2)
            
            if event.type == LEFT_LOST:
                print("left lost")
                ball.center_ball()
                wait = seconds(2)
                
        if(not wait):
            keys_pressed = pygame.key.get_pressed()
            move_paddle_left(keys_pressed, paddle_left)
            move_paddle_right(keys_pressed, paddle_right)
            
            ball.handle_collision(paddle_left, paddle_right)
            ball.update()
        else:
            wait -= 1
        
        render(ball, (paddle_left, paddle_right))
        
    pygame.quit

if __name__ == "__main__":
    main()