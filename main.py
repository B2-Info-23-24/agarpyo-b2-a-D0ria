import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Définition de la taille de l'écran
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Page principale")

# Fonction pour dessiner du texte sur l'écran
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

# Fonction pour dessiner une liste déroulante
def draw_dropdown(surface, x, y, width, height, options, selected_option, font, dropdown_color, option_color, selected_color):
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

# Options pour la liste déroulante
options = ["Easy", "Normal", "Hard"]
selected_option = "Easy"
options_visible = False

# Définition des polices de texte
font = pygame.font.Font(None, 36)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
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

    # Effacer l'écran
    screen.fill(BLACK)

    # Fonction pour dessiner un bouton
    def draw_button(surface, color, x, y, width, height, text, text_color, font):
        pygame.draw.rect(surface, color, (x, y, width, height))
        button_text_rect = draw_text(text, font, text_color, surface, x + width / 2, y + height / 2)
        return pygame.Rect(x, y, width, height), button_text_rect

    # Définition des polices de texte
    font = pygame.font.Font(None, 28)

    # Dessiner la liste déroulante
    dropdown_width = 150
    dropdown_height = 50
    dropdown_x = SCREEN_WIDTH // 2 - dropdown_width // 2
    dropdown_y = SCREEN_HEIGHT // 5
    dropdown_rect = pygame.Rect(dropdown_x, dropdown_y, dropdown_width, dropdown_height)
    draw_dropdown(screen, dropdown_x, dropdown_y, dropdown_width, dropdown_height, options, selected_option, font, WHITE, BLACK, GREEN)


    # Dessiner les nouveaux boutons
    button_width = 250
    button_height = 50
    button_x = (SCREEN_WIDTH - button_width) / 2
    button_spacing = 10
    button_y_start = SCREEN_HEIGHT // 3 + 150
    draw_button(screen, GREEN, button_x, button_y_start, button_width, button_height, "Jouer à la souris", BLACK, font)
    draw_button(screen, YELLOW, button_x, button_y_start + button_height + button_spacing, button_width, button_height, "Jouer au clavier", BLACK, font)
    quit_button_rect, quit_button_text_rect = draw_button(screen, RED, button_x, button_y_start + 2 * (button_height + button_spacing), button_width, button_height, "Quitter", BLACK, font)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
