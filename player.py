import pygame
import sys

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 0
        self.speed = 100
        self.size = 40
        self.control_mode = None
        self.difficulty = None

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if self.difficulty == "Easy":
            self.num_balls = 5
        elif self.difficulty == "Normal":
            self.num_balls = 3
        elif self.difficulty == "Hard":
            self.num_balls = 2

    def set_control_mode(self, mode):
        self.control_mode = mode

    def move(self):
        if self.control_mode == "mouse":
            self.move_with_mouse()
        elif self.control_mode == "keyboard":
            self.move_with_keyboard()

    def move_with_mouse(self):
        move_distance = self.speed  
        mouse_x, mouse_y = pygame.mouse.get_pos()
        direction_x = mouse_x - self.x
        direction_y = mouse_y - self.y
        distance = max(abs(direction_x), abs(direction_y))
        if distance != 0:
            move_x = (direction_x / move_distance) 
            move_y = (direction_y / move_distance) 
            self.x += move_x
            self.y += move_y

    def move_with_keyboard(self):
        move_distance = self.speed / 70

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.x -= move_distance
        if keys[pygame.K_d]:
            self.x += move_distance
        if keys[pygame.K_z]:
            self.y -= move_distance
        if keys[pygame.K_s]:
            self.y += move_distance

    def run(self):
        SCREEN_WIDTH = 1280
        SCREEN_HEIGHT = 720
        player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.set_difficulty(selected_option)  # Appel de la méthode pour configurer la difficulté
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

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x), int(self.y)), self.size)
