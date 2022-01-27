import pygame.sprite

from player import Player

class Game:
    def __init__(self):
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)

    def update(self,screen):
        # appliquer l'image des joueurs
        screen.blit(self.player.image,self.player.rect)

        #on recupere les player
        for player in self.all_player:
            player.fall()



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

