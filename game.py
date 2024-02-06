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
        self.start_time = pygame.time.get_ticks()  # Temps de départ
        self.game_over = False

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

            if not self.game_over:
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

                font = pygame.font.Font(None, 24)
                score_text = font.render(f"Score: {self.player.score}", True, (0, 0, 0))
                speed_text = font.render(f"Vitesse: {self.player.speed}", True, (0, 0, 0))
                size_text = font.render(f"Taille: {self.player.size}", True, (0, 0, 0))
                difficulty_text = font.render(f"Difficulté: {self.player.difficulty}", True, (0, 0, 0))

                # Calcul du temps restant
                elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
                time_left = max(0, 60 - elapsed_time)  # Limite à 0 pour ne pas avoir de temps négatif
                timer_text = font.render(f"Temps restant: {time_left} secondes", True, (0, 0, 0))

                # Affichage des informations
                self.screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))
                self.screen.blit(speed_text, (SCREEN_WIDTH - speed_text.get_width() - 10, 30))
                self.screen.blit(size_text, (SCREEN_WIDTH - size_text.get_width() - 10, 50))
                self.screen.blit(difficulty_text, (SCREEN_WIDTH - difficulty_text.get_width() - 10, 70))
                self.screen.blit(timer_text, (SCREEN_WIDTH - timer_text.get_width() - 10, 90))

                for food in self.food_list:
                    food.draw(self.screen)

                self.player.draw(self.screen)

                pygame.display.flip()

                # Vérification si le temps est écoulé
                if time_left <= 0:
                    self.game_over = True
                    self.show_game_over_screen()

            else:
                # Affichage de l'écran de fin de jeu
                self.show_game_over_screen()

            self.clock.tick(60)

    def show_game_over_screen(self):
        font = pygame.font.Font(None, 36)
        game_over_text = font.render("Temps écoulé !", True, (255, 0, 0))
        score_text = font.render(f"Score final: {self.player.score}", True, (0, 0, 0))
        return_button_text = font.render("Retour à la page d'accueil", True, (0, 0, 255))

        # Centrage des textes sur l'écran
        game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        score_text_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        return_button_text_rect = return_button_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        self.screen.blit(game_over_text, game_over_text_rect)
        self.screen.blit(score_text, score_text_rect)
        self.screen.blit(return_button_text, return_button_text_rect)

        pygame.display.flip()

        # Attendre que l'utilisateur clique sur le bouton de retour
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if return_button_text_rect.collidepoint(event.pos):
                        return