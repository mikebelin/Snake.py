from winreg import DisableReflectionKey
import pygame, sys, time, random 

speed = 15

#size of the window
frame_size_x = 720
frame_size_y = 480 

check_errors = pygame.init()

#game initialized 
if(check_errors[1] > 0):
    print("Error" + check_errors[1])
else:
    print("Gane initialized Successfully")

pygame.display.set_caption("Snake Game")
game_window = pygame.display.set_mode(frame_size_x, frame_size_y)

#colours used 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


fps_controller = pygame.time.Clock()

square_size = 20

def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, DisableReflection
    direction = "RIGHT"
    head_pos = [120, 60]
    snake_pody = [120, 60]
    food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                random.randrange(1, (frame_size_y // square_size)) * square_size]
    food_spawn = True
    score = 0 

init_vars)
)

def show_score():
    print("Showing Score")

#gameplay 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_UP or event.key == ord("w")
            and direction != "DOWN"):
            direction = "UP"
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_UP or event.key == ord("w")
            and direction != "DOWN"):
            direction = "UP"
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_UP or event.key == ord("w")
            and direction != "DOWN"):
            direction = "UP"
        elif event.type == pygame.KEYDOWN:
            if(event.key == pygame.K_UP or event.key == ord("w")
            and direction != "DOWN"):
            direction = "UP"