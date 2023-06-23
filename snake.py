import pygame
import random

WIDTH = 600
HEIGHT = 600

class Snake:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.body = [(self.x, self.y)]
        self.dx = 0
        self.dy = -1

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.body.insert(0, (self.x, self.y))
        self.body.pop()

    def draw(self, surface):
        for x, y in self.body:
            pygame.draw.rect(surface, (255, 255, 255), (x, y, 10, 10))

    def grow(self):
        self.body.append((self.x, self.y))

    def change_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def check_collision(self, x, y):
        for bx, by in self.body:
            if bx == x and by == y:
                return True
        return False

class Food:
    def __init__(self):
        self.x = random.randint(0, WIDTH // 10) * 10
        self.y = random.randint(0, HEIGHT // 10) * 10

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, 10, 10))

def main():
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(0, -1)
                if event.key == pygame.K_DOWN:
                    snake.change_direction(0, 1)
                if event.key == pygame.K_LEFT:
                    snake.change_direction(-1, 0)
                if event.key == pygame.K_RIGHT:
                    snake.change_direction(1, 0)

        surface.fill((0, 0, 0))
        snake.update()
        snake.draw(surface)
        food.draw(surface)
        if snake.check_collision(food.x, food.y):
            snake.grow()
            food = Food()
        if snake.x < 0 or snake.y < 0 or snake.x >= WIDTH or snake.y >= HEIGHT or snake.check_collision(snake.x, snake.y):
            running = False
        pygame.display.update()
        clock.tick(10)
    pygame.quit()

if __name__ == '__main__':
    main()
