import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.size = 20
        self.control_mode = None

    def set_control_mode(self, mode):
        self.control_mode = mode

    def move(self):
        if self.control_mode == "mouse":
            self.move_with_mouse()
        elif self.control_mode == "keyboard":
            self.move_with_keyboard()

    def move_with_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        direction_x = mouse_x - self.x
        direction_y = mouse_y - self.y
        distance = max(abs(direction_x), abs(direction_y))
        if distance != 0:
            move_x = (direction_x / distance) * self.speed
            move_y = (direction_y / distance) * self.speed
            self.x += move_x
            self.y += move_y

    def move_with_keyboard(self):
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_q]:
                self.x -= self.speed
            if keys[pygame.K_d]:
                self.x += self.speed
            if keys[pygame.K_z]:
                self.y -= self.speed
            if keys[pygame.K_s]:
                self.y += self.speed

            # Assurez-vous que le joueur continue de se déplacer même si aucune touche n'est enfoncée
            if not any(keys):
                return

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), (int(self.x), int(self.y)), self.size)
