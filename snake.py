# Import necessary modules
import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define screen size
dis_width = 800
dis_height = 600

# Create the screen
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Define clock
clock = pygame.time.Clock()

# Define font
font_style = pygame.font.SysFont(None, 50)

# Define function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

# Define function to run the game
def gameLoop():
    # Define game variables
    game_over = False
    game_close = False

    # Define starting position of snake
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Define change in position of snake
    x1_change = 0
    y1_change = 0

    # Define length of snake
    snake_List = []
    Length_of_snake = 1

    # Define position of food
    foodx = round(random.randrange(0, dis_width - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - 10) / 10.0) * 10.0

    # Run game loop
    while not game_over:

        # Display message if game is over
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Check for user input
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                elif event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
            elif event.type == pygame.QUIT:
                game_over = True
                game_close = False

        # Check if snake hits the boundary
        if x1 >= dis_width:
            x1 = 0
        elif x1 < 0:
            x1 = dis_width - 10
        elif y1 >= dis_height:
            y1 = 0
        elif y1 < 0:
            y1 = dis_height - 10

        # Update position of snake
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)

        # Draw food
        pygame.draw.rect(dis, green, [foodx, foody, 10, 10])

        # Update snake length
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if snake hits itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw snake
        for x in snake_List:
            pygame.draw.rect(dis, white, [x[0], x[1], 10, 10])

        # Update display
        pygame.display.update()

        # Check if snake hits food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - 10) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - 10) / 10.0) * 10.0
            Length_of_snake += 1

        # Set game speed
        clock.tick(30)

    # Deactivate Pygame
    pygame.quit()

# Run game
gameLoop()
