import pygame
import DEFAULT
import random
from math import sqrt


class Weapon(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.dmg = 100
        self.velocity = 10
        # image
        self.direction = player.direction
        self.image = pygame.image.load('assets/shuriken.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        # position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = player.rect.x+20, player.rect.x
        self.origin_img = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_img,self.angle,1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        if self.rect.x > 1000 or self.rect.x < 10:
            self.kill()
        if self.direction == 0:
            self.rect.x -= self.velocity
        else:
            self.rect.x += self.velocity
        self.rotate()
