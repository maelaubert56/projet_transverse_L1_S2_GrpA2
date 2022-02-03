import pygame
from background_file import Background
import DEFAULT


class Menu():
    def __init__(self):

        # arriere plan
        self.background = pygame.image.load(DEFAULT.path_background)
        self.background_rect = self.background.get_rect()
        self.background_rect.width = DEFAULT.window_width
        self.background = pygame.transform.scale(self.background,(self.background_rect.width + 100, Background().rect.height))

        # bouton settings
        self.settings_image = pygame.image.load(DEFAULT.path_settings)
        self.settings_rect = self.settings_image.get_rect()
        self.settings_rect.x = DEFAULT.window_width/2
        self.settings_rect.y = 500

        # bouton retour
        self.return_image = pygame.image.load(DEFAULT.path_return)
        self.return_rect = self.return_image.get_rect()
        self.return_rect.x = 50
        self.return_rect.y = 50

        # bouton play
        self.play_image = pygame.image.load(DEFAULT.path_play)
        self.play_rect = self.play_image.get_rect()
        self.play_rect.x = DEFAULT.window_width / 2
        self.play_rect.y = 100



    def update(self,screen,menu_number):
        screen.blit(self.background,self.background_rect)
        if menu_number == 0:
            screen.blit(self.settings_image,self.settings_rect)
            screen.blit(self.play_image,self.play_rect)
        elif menu_number == 1:
            screen.blit(self.return_image,self.return_rect)
        elif menu_number == 2:
            screen.blit(self.play_image, self.play_rect)

