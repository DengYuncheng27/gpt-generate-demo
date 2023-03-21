import pygame
import random

# initialize pygame
pygame.init()

# set up the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Tank Battle")

# set up the game clock
clock = pygame.time.Clock()

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# define game variables
tank_width = 40
tank_height = 60
enemy_tank_width = 40
enemy_tank_height = 60
bullet_width = 5
bullet_height = 10
tank_speed = 5
bullet_speed = tank_speed * 3
enemy_tank_speed = tank_speed
enemy_tank_spawn_rate = 3
enemy_tank_spawn_counter = 0
enemy_tanks = []
bullets = []
score = 0
game_over = False

# define game objects

class Tank:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, tank_width, tank_height)
        self.direction = "up"
        self.bullet_cooldown = 0

    def move(self):
        if self.direction == "up":
            self.y -= tank_speed
        elif self.direction == "down":
            self.y += tank_speed
        elif self.direction == "left":
            self.x -= tank_speed
        elif self.direction == "right":
            self.x += tank_speed

        # keep tank within game window
        if self.x < 0:
            self.x = 0
        elif self.x > window_width - tank_width:
            self.x = window_width - tank_width
        elif self.y < 0:
            self.y = 0
        elif self.y > window_height - tank_height:
            self.y = window_height - tank_height

        # update tank rectangle
        self.rect = pygame.Rect(self.x, self.y, tank_width, tank_height)

    def shoot(self):
        if self.bullet_cooldown == 0:
            bullet = Bullet(self.x + tank_width / 2 - bullet_width / 2, self.y, self.direction)
            bullets.append(bullet)
            self.bullet_cooldown = 30



class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.rect = pygame.Rect(self.x, self.y, bullet_width, bullet_height)

    def move(self):
        if self.direction == "up":
            self.y -= bullet_speed
        elif self.direction == "down":
            self.y += bullet_speed
        elif self.direction == "left":
            self.x -= bullet_speed
        elif self.direction == "right":
            self.x += bullet_speed

        # update bullet rectangle
        self.rect = pygame.Rect(self.x, self.y, bullet_width, bullet_height)

    def check_collision(self):
        for enemy_tank in enemy_tanks:
            if self.rect.colliderect(enemy_tank.rect):
                bullets.remove(self)
                enemy_tanks.remove(enemy_tank)
                break

class EnemyTank(Tank):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.direction = random.choice(["up", "down", "left", "right"])
        self.bullet_cooldown = random.randint(30, 60)

    def move(self):
        if self.direction == "up":
            self.y -= enemy_tank_speed
        elif self.direction == "down":
            self.y += enemy_tank_speed
        elif self.direction == "left":
            self.x -= enemy_tank_speed
        elif self.direction == "right":
            self.x += enemy_tank_speed

        # keep tank within game window
        if self.x < 0:
            self.x = 0
            self.direction = random.choice(["down", "left", "right"])
        elif self.x > window_width - enemy_tank_width:
            self.x = window_width - enemy_tank_width
            self.direction = random.choice(["up", "left", "right"])
        elif self.y < 0:
            self.y = 0
            self.direction = random.choice(["down", "left", "right"])
        elif self.y > window_height - enemy_tank_height:
            self.y = window_height - enemy_tank_height
            self.direction = random.choice(["up", "left", "right"])

        # update tank rectangle
        self.rect = pygame.Rect(self.x, self.y, enemy_tank_width, enemy_tank_height)

    def shoot(self):
        if self.bullet_cooldown == 0:
            bullet = Bullet(self.x + enemy_tank_width / 2 - bullet_width / 2, self.y + enemy_tank_height, self.direction)
            bullets.append(bullet)
            self.bullet_cooldown = random.randint(30, 60)


player_tank = Tank(window_width / 2 - tank_width / 2, window_height - tank_height, green)

while not game_over:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_tank.direction = "up"
            elif event.key == pygame.K_DOWN:
                player_tank.direction = "down"
            elif event.key == pygame.K_LEFT:
                player_tank.direction = "left"
            elif event.key == pygame.K_RIGHT:
                player_tank.direction = "right"
            elif event.key == pygame.K_SPACE:
                player_tank.shoot()

    # spawn enemy tanks
    if len(enemy_tanks) < enemy_tank_spawn_rate:
        enemy_tank_x = random.randint(0, window_width - enemy_tank_width)
        enemy_tank_y = random.randint(-100, -enemy_tank_height)
        enemy_tank = EnemyTank(enemy_tank_x, enemy_tank_y, blue)
        enemy_tanks.append(enemy_tank)

    # move player tank
    player_tank.move()

    # move bullets
    for bullet in bullets:
        bullet.move()
        bullet.check_collision()

    # move enemy tanks
    for enemy_tank in enemy_tanks:
        enemy_tank.move()
        enemy_tank.shoot()

    # check for enemy tank collisions with player tank
    for enemy_tank in enemy_tanks:
        if enemy_tank.rect.colliderect(player_tank.rect):
            game_over = True

    # draw game objects
    game_window.fill(white)
    pygame.draw.rect(game_window, black, (0, 0, window_width, window_height), 2)
    pygame.draw.rect(game_window, player_tank.color, player_tank.rect)
    for bullet in bullets:
        pygame.draw.rect(game_window, red, bullet.rect)
    for enemy_tank in enemy_tanks:
        pygame.draw.rect(game_window, enemy_tank.color, enemy_tank.rect)
    pygame.display.update()

    # update bullet cooldowns
    if player_tank.bullet_cooldown > 0:
        player_tank.bullet_cooldown -= 1
    for enemy_tank in enemy_tanks:
        if enemy_tank.bullet_cooldown > 0:
            enemy_tank.bullet_cooldown -= 1

    # increase score and enemy tank speed
    if score % 10 == 0:
        enemy_tank_speed += 1
        score += 1

    # set game over message
    font = pygame.font.SysFont(None, 50)
    game_over_message = font.render("Game Over", True, red)
    game_over_rect = game_over_message.get_rect(center=(window_width / 2, window_height / 2))

    # update game clock
    clock.tick(60)

# display game over message
game_window.blit(game_over_message, game_over_rect)
pygame.display.update()

# quit pygame
pygame.quit()




