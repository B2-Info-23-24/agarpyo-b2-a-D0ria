import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 0
        self.speed = 100
        self.size = 40
        self.control_mode = ""
        self.difficulty = None
        self.mouse_control_enabled = False
        self.keyboard_control_enabled = False

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if self.difficulty == "Easy":
            self.num_balls = 5
        elif self.difficulty == "Normal":
            self.num_balls = 3
        elif self.difficulty == "Hard":
            self.num_balls = 2

    def set_control_mode(self, mode):
        print(mode)
        if mode == "keyboard":
            self.control_mode = "keyboard"
            self.mouse_control_enabled = False
            self.keyboard_control_enabled = True
        elif mode == "mouse":
            self.control_mode = "mouse"
            self.mouse_control_enabled = True
            self.keyboard_control_enabled = False
            print(self.control_mode)

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

        if self.x < 0:
            self.x = 1280
        elif self.x > 1280:
            self.x = 0 
        if self.y < 0:
            self.y = 720  
        elif self.y > 720:
            self.y = 0

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x), int(self.y)), self.size)
