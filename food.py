import pygame
import random

BROWN = (139, 69, 19)  

class Food:
    def __init__(self, width, height):
        self.position = (0, 0)
        self.size = 20 
        self.randomize_position(width, height)
        
    def randomize_position(self, width, height):
        self.position = random.randint(0, width), random.randint(0, height)
        
    def draw(self, surface):
        pygame.draw.circle(surface, BROWN, self.position, self.size)

