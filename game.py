import pygame 
import sys
from player import Player

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Agarpyo")
        self.clock = pygame.time.Clock()

    def run(self):
        SCREEN_WIDTH = 1280
        SCREEN_HEIGHT = 720
        player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            player.move_with_mouse()

            player.move_with_keyboard()

            self.screen.fill((255, 255, 255))

            player.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(60)
