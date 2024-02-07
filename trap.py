import pygame
import random

BROWN = (0, 255, 0)  

class Trap:
    def __init__(self, width, height):
        self.size = random.randint(40, 150)   
        self.randomize_position(width, height)
        
    def randomize_position(self, width, height):
        self.position = random.randint(0, width), random.randint(0, height)
        
    def draw(self, surface):
        pygame.draw.circle(surface, BROWN, self.position, self.size)

