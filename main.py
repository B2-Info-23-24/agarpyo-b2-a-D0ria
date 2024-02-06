import pygame
import sys
from game import Game
from player import Player

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Page principale")

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def draw_dropdown(surface, x, y, width, height, options, selected_option, font, dropdown_color, option_color, selected_color, options_visible):
    pygame.draw.rect(surface, dropdown_color, (x, y, width, height))
    draw_text(selected_option, font, BLACK, surface, x + 75, y + 25)
    if options_visible:
        pygame.draw.rect(surface, BLACK, (x, y + height, width, len(options) * height))
        option_y = y + height
        for option in options:
            if option == selected_option:
                pygame.draw.rect(surface, selected_color, (x, option_y, width, height))
            else:
                pygame.draw.rect(surface, option_color, (x, option_y, width, height))
            draw_text(option, font, WHITE, surface, x + 75, option_y + 25)
            option_y += height


options = ["Easy", "Normal", "Hard"]
selected_option = "Easy"
options_visible = False

font = pygame.font.Font(None, 36)

control_mode = "keyboard"
mouse_button_rect, mouse_button_text_rect = None, None
keyboard_button_rect, keyboard_button_text_rect = None, None
quit_button_rect, quit_button_text_rect = None, None
dropdown_rect = None
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

def run_game():
    game = Game()
    game.run()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if mouse_button_rect.collidepoint(mouse_pos):  
                control_mode = "mouse"  
                player.set_control_mode("mouse")
                run_game()  
            elif keyboard_button_rect.collidepoint(mouse_pos):  
                control_mode = "keyboard"  
                player.set_control_mode("keyboard")
                run_game()  
            if dropdown_rect.collidepoint(mouse_pos):
                options_visible = not options_visible
            elif options_visible:
                option_index = (mouse_pos[1] - dropdown_rect.bottom) // dropdown_height
                if 0 <= option_index < len(options):
                    selected_option = options[option_index]
                    options_visible = False

            if quit_button_rect.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    screen.fill(BLACK)

    def draw_button(surface, color, x, y, width, height, text, text_color, font):
        pygame.draw.rect(surface, color, (x, y, width, height))
        button_text_rect = draw_text(text, font, text_color, surface, x + width / 2, y + height / 2)
        return pygame.Rect(x, y, width, height), button_text_rect

    font = pygame.font.Font(None, 28)

    dropdown_width = 150
    dropdown_height = 50
    dropdown_x = SCREEN_WIDTH // 2 - dropdown_width // 2
    dropdown_y = SCREEN_HEIGHT // 5
    dropdown_rect = pygame.Rect(dropdown_x, dropdown_y, dropdown_width, dropdown_height)
    draw_dropdown(screen, dropdown_x, dropdown_y, dropdown_width, dropdown_height, options, selected_option, font, WHITE, BLACK, GREEN, options_visible)

    button_width = 250
    button_height = 50
    button_x = (SCREEN_WIDTH - button_width) / 2
    button_spacing = 10
    button_y_start = SCREEN_HEIGHT // 3 + 150
    mouse_button_rect, mouse_button_text_rect = draw_button(screen, GREEN, button_x, button_y_start, button_width, button_height, "Jouer à la souris", BLACK, font)
    keyboard_button_rect, keyboard_button_text_rect = draw_button(screen, YELLOW, button_x, button_y_start + button_height + button_spacing, button_width, button_height, "Jouer au clavier", BLACK, font)
    quit_button_rect, quit_button_text_rect = draw_button(screen, RED, button_x, button_y_start + 2 * (button_height + button_spacing), button_width, button_height, "Quitter", BLACK, font)

    pygame.display.flip()

pygame.quit()
sys.exit()

