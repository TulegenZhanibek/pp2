import random

import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BROWN = (165,42,42)
ORANGE = (255, 165, 0)
clock = pygame.time.Clock()
SCORE_FONT = pygame.font.SysFont("comicsansms", 25)
SCORE_LEVEL = pygame.font.SysFont("comicsansms", 25)
FPS = 5


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [
            Point(
                x = WIDTH // BLOCK_SIZE // 2,
                y = HEIGHT // BLOCK_SIZE // 2,
            ),
            
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 1:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    
    def snake_collision(self):
        for rect in range(len(self.body) - 1, 1, -1):
            if (self.body[0].x == self.body[rect].x and self.body[0].x + 1 == self.body[rect].x + 1) and (self.body[0].y == self.body[rect].y and self.body[0].y + 1 == self.body[rect].y + 1):
                return True
            return False

def draw_grid():
    pygame.draw.rect(
        SCREEN,
        YELLOW,
        pygame.Rect(
            0,
            0,
            WIDTH,
            BLOCK_SIZE
        )
    )
    # for x in range(0, WIDTH, BLOCK_SIZE):
    #     pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    # for y in range(0, HEIGHT, BLOCK_SIZE):
    #     pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

class Big_Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            ORANGE,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )

class Remove:
    def __init__(self, x, y):
        self.location = Point(x, y)
        
    def draw(self):
        pygame.draw.rect(
            SCREEN,
            BROWN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
    

def main():
    running = True
    snake = Snake()
    food = Food(5, 5)
    delete = Remove(7, 7)
    big_food = Big_Food(3, 7)
    dx, dy = 0, 0
    score = 0
    level = 0
    global FPS
    dict = {"up": True,"down" : True,'right': True,'left' : True}
    while running:
        SCREEN.fill(BLACK)
        SCORE = SCORE_FONT.render(f"Your score {score}", True, BLACK)
        LEVEL = SCORE_LEVEL.render(f"Level {level}", True, BLACK)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dict['up']:
                    dx, dy = 0, -1
                    dict = {"up": True,"down" : False,'right': True,'left' : True}
                elif event.key == pygame.K_DOWN and dict['down']:
                    dx, dy = 0, 1
                    dict = {"up": False,"down" : True,'right': True,'left' : True}
                elif event.key == pygame.K_RIGHT and dict['right']:
                    dx, dy = 1, 0
                    dict = {"up": True,"down" : True,'right': True,'left' : False}
                elif event.key == pygame.K_LEFT and dict['left']:
                    dx, dy = -1, 0
                    dict = {"up": True,"down" : True,'right': False,'left' : True}

        snake.move(dx, dy)
        if snake.check_collision(food):
            score += 1
            snake.body.append(
                Point(snake.body[-1].x, snake.body[-1].y)
            )
            food.location.x = random.randint(1, WIDTH // BLOCK_SIZE - 1)
            food.location.y = random.randint(1, HEIGHT // BLOCK_SIZE - 1)
            if score % 4 == 0 and score != 0: 
                FPS += 1
                level += 1
        
        if score % 5 == 0 and score != 0:   
            big_food.draw() 
            if snake.check_collision(big_food):
                score += 2
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
                snake.body.append(
                    Point(snake.body[-1].x, snake.body[-1].y)
                )
                big_food.location.x = random.randint(1, WIDTH // BLOCK_SIZE - 1)
                big_food.location.y = random.randint(1, HEIGHT // BLOCK_SIZE - 1)
        
        if score % 3 == 0 and score != 0:
            delete.draw()
            if snake.check_collision(delete):
                pygame.quit
        
        if snake.snake_collision():
            pygame.quit()
            
        snake.draw()
        food.draw()
        
        draw_grid()
        SCREEN.blit(SCORE, (0, 0))
        SCREEN.blit(LEVEL, (WIDTH - 100, 0))
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    main()