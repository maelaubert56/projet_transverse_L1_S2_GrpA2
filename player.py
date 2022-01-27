import pygame
import DEFAULT
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = 5
        self.fall_velocity = 1
        self.image = pygame.image.load(DEFAULT.path_player)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.x = 50 + random.randint(0,DEFAULT.window_width-100)
        self.rect.y = -100
        self.mask = pygame.mask.from_surface(self.image)

    def fall(self):
        self.rect.y += self.fall_velocity

