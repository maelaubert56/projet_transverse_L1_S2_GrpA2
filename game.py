import pygame.sprite

import DEFAULT
from player import Player
from background_file import Background

class Game:
    def __init__(self):
        self.all_players= pygame.sprite.Group()
        self.object_background= Background()
        self.sea_level = DEFAULT.sea_level
        # dictionnaire de touches
        self.pressed = {}


    def start(self):
        print("Lancement du jeu")
        if DEFAULT.DEBUG:
            for i in range(0,DEFAULT.window_width+50,5):
                self.spawn_player(i)
        else : self.spawn_player()


    def update(self,screen):
        # on recupere les players
        for player in self.all_players:
            player.fall(screen)

        # appliquer l'image du groupe de joueurs
        self.all_players.draw(screen)


    def spawn_player(self,i=0):
        self.all_players.add(Player(self,i))
