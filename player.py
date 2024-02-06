import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 100
        self.size = 40
        self.control_mode = None

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


    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x), int(self.y)), self.size)
