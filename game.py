import pygame
import sys
from player import Player
from food import Food 

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Agarpyo")
        self.clock = pygame.time.Clock()
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.food_list = [] 

    def generate_food(self, num_food, width, height):
        for _ in range(num_food):
            food = Food(width, height)
            self.food_list.append(food)

    def run(self):
        SCREEN_WIDTH = 1280
        SCREEN_HEIGHT = 720
        # self.player.set_difficulty(selected_option)
        self.generate_food(20, SCREEN_WIDTH, SCREEN_HEIGHT)  

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.player.move_with_mouse()
            self.player.move_with_keyboard()

            for food in self.food_list:
                if pygame.Rect(self.player.x - self.player.size, self.player.y - self.player.size, self.player.size * 2, self.player.size * 2).colliderect(pygame.Rect(food.position[0] - food.size, food.position[1] - food.size, food.size * 2, food.size * 2)):
                    self.player.score += 1
                    self.player.speed = min(500, self.player.speed + 5)
                    self.player.size = min(200, self.player.size + 2)
                    self.food_list.remove(food)
                    new_food = Food(SCREEN_WIDTH, SCREEN_HEIGHT)
                    self.food_list.append(new_food)

            self.screen.fill((255, 255, 255))

            for food in self.food_list:
                food.draw(self.screen)

            self.player.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(60)
