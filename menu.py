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
        self.background_rect = self.background.get_rect()

        # bouton settings
        self.settings_image = pygame.image.load(DEFAULT.path_settings)
        self.settings_image = pygame.transform.scale(self.settings_image, (100, 100))
        self.settings_rect = self.settings_image.get_rect()
        self.settings_rect.x = DEFAULT.window_width/2
        self.settings_rect.y = 500


        # bouton retour
        self.return_image = pygame.image.load(DEFAULT.path_return)
        self.return_image = pygame.transform.scale(self.return_image, (100, 100))
        self.return_rect = self.return_image.get_rect()
        self.return_rect.x = 50
        self.return_rect.y = 50

        # bouton credits
        self.credit_image = pygame.image.load(DEFAULT.path_credit)
        self.credit_image = pygame.transform.scale(self.credit_image, (100, 100))
        self.credit_rect = self.credit_image.get_rect()
        self.credit_rect.x = 25
        self.credit_rect.y = 25

        # bouton info
        self.info_image = pygame.image.load(DEFAULT.path_info)
        self.info_image = pygame.transform.scale(self.info_image, (100, 100))
        self.info_rect = self.info_image.get_rect()
        self.info_rect.x = 12
        self.info_rect.y = 12

        # bouton play
        self.play_image = pygame.image.load(DEFAULT.path_play)
        self.play_image = pygame.transform.scale(self.play_image, (100, 100))
        self.play_rect = self.play_image.get_rect()
        self.play_rect.x = DEFAULT.window_width / 2
        self.play_rect.y = 110

        # bouton volume on/off
        self.sound_on_image = pygame.image.load(DEFAULT.path_sound_on)
        self.sound_off_image = pygame.image.load(DEFAULT.path_sound_off)
        self.sound_on_image = pygame.transform.scale(self.sound_on_image, (100, 100))
        self.sound_off_image = pygame.transform.scale(self.sound_off_image, (100, 100))
        self.sound_rect = self.sound_on_image.get_rect()
        self.sound_rect.x = 50
        self.sound_rect.y = 170


    def update(self,screen,menu_number):
        screen.blit(self.background,self.background_rect)
        if menu_number == 0: # menu d'accueil
            screen.blit(self.settings_image,self.settings_rect)
            screen.blit(self.play_image,self.play_rect)
            screen.blit(self.credit_image, self.credit_rect)

        elif menu_number == 1: # menu de parametres
            screen.blit(self.return_image,self.return_rect)
            # switch entre le bouton volume off ou on
            if DEFAULT.music_level == 0:
                screen.blit(self.sound_on_image, self.sound_rect)
            else:
                screen.blit(self.sound_off_image, self.sound_rect)

        elif menu_number == 2: # menu pause
            screen.blit(self.settings_image, self.settings_rect)
            screen.blit(self.play_image, self.play_rect)
        elif menu_number == 3: # menu info
            screen.blit(self.return_image, self.return_rect)
        elif menu_number == 4: # menu credit
            screen.blit(self.return_image,self.return_rect)

