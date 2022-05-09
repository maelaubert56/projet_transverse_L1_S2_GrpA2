import pygame
from ground import Ground
import DEFAULT
#  from state import State

class Menu():
    def __init__(self):
        self.windows_height = Ground().rect.height+100
        self.previous_menu_number = 0
        # arriere plan
        self.background = pygame.image.load(DEFAULT.path_background)
        self.background_rect = self.background.get_rect()
        self.background_rect.width = DEFAULT.window_width
        self.background = pygame.transform.scale(self.background,
                                                 (self.background_rect.width + 100, Ground().rect.height))
        self.background_rect = self.background.get_rect()

        # bouton settings
        self.settings_image = pygame.image.load(DEFAULT.path_settings)
        self.settings_image = pygame.transform.scale(self.settings_image, (120, 120))
        self.settings_rect = self.settings_image.get_rect()
        self.settings_rect.x = 1270
        self.settings_rect.y = 0

        # bouton retour
        self.return_image = pygame.image.load(DEFAULT.path_return)
        self.return_image = pygame.transform.scale(self.return_image, (120, 120))
        self.return_rect = self.return_image.get_rect()
        self.return_rect.x = 50
        self.return_rect.y = 50

        # bouton credits
        self.credit_image = pygame.image.load(DEFAULT.path_credit)
        self.credit_image = pygame.transform.scale(self.credit_image, (120, 120))
        self.credit_rect = self.credit_image.get_rect()
        self.credit_rect.x = 0
        self.credit_rect.y = 0

        # bouton info
        self.info_image = pygame.image.load(DEFAULT.path_info)
        self.info_image = pygame.transform.scale(self.info_image, (120, 120))
        self.info_rect = self.info_image.get_rect()
        self.info_rect.x = 5
        self.info_rect.y = 150

        # bouton play
        self.play_image = pygame.image.load(DEFAULT.path_play)
        self.play_image = pygame.transform.scale(self.play_image, (150, 150))
        self.play_rect = self.play_image.get_rect()
        self.play_rect.x = DEFAULT.window_width / 2
        self.play_rect.y = 250

        # bouton volume on/off
        self.sound_on_image = pygame.image.load(DEFAULT.path_sound_on)
        self.sound_off_image = pygame.image.load(DEFAULT.path_sound_off)
        self.sound_on_image = pygame.transform.scale(self.sound_on_image, (120, 120))
        self.sound_off_image = pygame.transform.scale(self.sound_off_image, (120, 120))
        self.sound_rect = self.sound_on_image.get_rect()
        self.sound_rect.x = 50
        self.sound_rect.y = 170

        # Image Titre du jeu
        self.name = pygame.image.load(DEFAULT.path_title)
        self.name_rect = self.name.get_rect()
        self.name = pygame.transform.scale(self.name, (960*1.2,460*1.2))
        self.name_rect.x = DEFAULT.window_width / 9
        self.name_rect.y = 50

        # Image Credits
        self.credits = pygame.image.load(DEFAULT.path_credits)
        self.credits_rect = self.credits.get_rect()
        self.credits = pygame.transform.scale(self.credits, (1402 * 0.8, 999 * 0.8))
        self.credits_rect.x = 0
        self.credits_rect.y = 0

        # image quitter jeu
        self.quit_game = pygame.image.load(DEFAULT.path_quit_game)
        self.quit_game = pygame.transform.scale(self.quit_game, (120, 120))
        self.quit_game_rect = self.quit_game.get_rect()
        self.quit_game_rect.x = 0
        self.quit_game_rect.y = 0


    def update(self, screen, menu_number):
        screen.blit(self.background, self.background_rect)
        if menu_number == 0:  # menu d'accueil
            screen.blit(self.name, self.name_rect)
            screen.blit(self.settings_image, self.settings_rect)
            screen.blit(self.play_image, self.play_rect)
            screen.blit(self.credit_image, self.credit_rect)
            screen.blit(self.info_image, self.info_rect)


        elif menu_number == 1:  # menu de paramètres
            screen.blit(self.return_image, self.return_rect)  # bouton retour
            if DEFAULT.music_level == 0:  # bouton volume on/off
                screen.blit(self.sound_off_image, self.sound_rect)
            else:
                screen.blit(self.sound_on_image, self.sound_rect)

        elif menu_number == 2:  # menu pause
            screen.blit(self.settings_image, self.settings_rect)  # ==> menu paramètre
            screen.blit(self.play_image, self.play_rect)  # ==> retour au jeu
            screen.blit(self.quit_game,self.quit_game_rect)

        elif menu_number == 3:  # menu info
            screen.blit(self.return_image, self.return_rect)  # ==> retour au menu precedent

        elif menu_number == 4:  # menu credit
            screen.blit(self.return_image, self.return_rect)
            screen.blit(self.credits,self.credits_rect)