import pygame.sprite
import DEFAULT
from player import Player
from background_file import Background


class Game:
    def __init__(self, screen=None):
        # joueurs et équipes
        self.all_players = pygame.sprite.Group()
        self.all_players_blue = pygame.sprite.Group()
        self.all_players_red = pygame.sprite.Group()
        self.liste_team = [ self.all_players, self.all_players_blue, self.all_players_red]
        # décor
        self.object_background = Background()
        self.sea_level = DEFAULT.sea_level
        # mort subite
        self.bool_ms = False
        # dictionnaire de touches
        self.pressed = {}
        # player selectionné pour jouer
        self.player_choice = None
        # équipes
        self.last_team = 0

    def start(self):
        self.spawn_player()

    def update(self, screen):
        # on update les players
        for player in self.all_players:
            player.fall(screen)
            player.all_projectiles.draw(screen)
            for projectile in player.all_projectiles:
                projectile.move()

        # appliquer l'image du groupe de joueurs
        self.all_players.draw(screen)

    def spawn_player(self):
        # décide de l'équipe et l'équipe adverse
        if self.last_team == 0:
            new_player = Player(self, 1)
            self.all_players_blue.add(new_player)
            new_player.equipe_adverse = self.all_players_red
            # témoin pour que le jeu alterne entre bleu et rouge
            self.last_team = 1
        else:
            new_player = Player(self, 0)
            self.all_players_red.add(new_player)
            new_player.equipe_adverse = self.all_players_blue
            # témoin pour que le jeu alterne entre bleu et rouge
            self.last_team = 0

        # ajoute le nouveau joueur dans la liste des joueurs
        self.all_players.add(new_player)
        # le focus est mis sur le nouveau player
        self.player_choice = new_player

    def change_player_choice(self):
        tmp_list = []
        for player in self.all_players:
            tmp_list.append(player)
        if len(tmp_list) != 0:
            self.player_choice = tmp_list[(tmp_list.index(self.player_choice)+1) % len(tmp_list)]
        else:
            self.player_choice = None
