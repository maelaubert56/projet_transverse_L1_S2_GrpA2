import pygame.sprite
import DEFAULT
from player import Player
from background_file import Background
from random import randint


class Game:
    def __init__(self, screen=None):
        # self.screen = screen
        self.all_players = pygame.sprite.Group()
        self.object_background = Background()
        self.sea_level = DEFAULT.sea_level
        # mort subite
        self.bool_ms = False
        # dictionnaire de touches
        self.pressed = {}
        # player selectionné pour jouer
        self.player_choice = None

    def start(self):
        if DEFAULT.DEBUG:
            self.spawn_player()
        else:
            self.spawn_player()

    def update(self, screen):
        # on recupere les players
        for player in self.all_players:
            player.fall(screen)

        # appliquer l'image du groupe de joueurs
        self.all_players.draw(screen)

    def spawn_player(self):
        # le player spawn à un x random
        new_player = Player(self, randint(0, DEFAULT.window_width + 50))
        self.all_players.add(new_player)
        # le focus est mis sur le nouveau player
        self.player_choice = new_player

    def change_player_choice(self):
        tmp_list = []
        for player in self.all_players:
            tmp_list.append(player)
        self.player_choice = tmp_list[(tmp_list.index(self.player_choice)+1) % len(tmp_list)]
