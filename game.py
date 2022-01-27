import pygame.sprite

from player import Player
from object_background import Object_background

class Game:
    def __init__(self):
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.object_background = Object_background()
        self.all_player.add(self.player)

    def update(self,screen):
        # appliquer l'image des joueurs
        screen.blit(self.player.image,self.player.rect)

        #on recupere les player
        for player in self.all_player:
            if pygame.sprite.collide_mask(self.object_background,self.player) != None:
                pygame.draw.circle(surface=screen,color=(255,0,0),center=(pygame.sprite.collide_mask(self.object_background,self.player)),radius=2)
            else:
                pygame.draw.circle(surface=screen, color=(0, 255, 0),center=self.player.rect.bottomleft, radius=2)
                pygame.draw.circle(surface=screen, color=(0, 255, 0), center=self.player.rect.bottomright, radius=2)
                player.fall()

