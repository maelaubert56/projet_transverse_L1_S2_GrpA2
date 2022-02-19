import pygame.sprite
import DEFAULT
from player import Player
from ground import Ground


class Game:
    def __init__(self):
        # joueurs et équipes
        self.all_players = pygame.sprite.Group()
        self.all_players_blue = pygame.sprite.Group()
        self.all_players_red = pygame.sprite.Group()
        self.liste_team = [self.all_players, self.all_players_blue, self.all_players_red]
        # décors
        self.object_ground = Ground()
        self.sea_level = DEFAULT.sea_level
        # mort subite
        self.bool_ms = False
        # dictionnaire de touches
        self.pressed = {}
        # player sélectionné pour jouer
        self.player_choice = None
        # équipes
        self.last_team = 0

        # decors
        self.object_ground = Ground()
        # on importe et redimensionne l'arrière-plan
        self.background = pygame.image.load(DEFAULT.path_background)
        self.background_rect = self.background.get_rect()
        self.background_rect.width = DEFAULT.window_width
        self.background = pygame.transform.scale(self.background,
                                                 (self.background_rect.width + 100, self.object_ground.rect.height))

        # on importe et redimensionne la mer
        self.sea = pygame.image.load(DEFAULT.path_sea)
        self.sea_rect = self.sea.get_rect()
        self.sea_rect.width = DEFAULT.window_width
        self.sea = pygame.transform.scale(self.sea, (self.sea_rect.width + 100, self.object_ground.rect.height))

    def start(self):
        self.spawn_player()

    def update(self, screen):
        # appliquer le terrain
        screen.blit(self.background, (0, 0))
        # appliquer l'eau sur le terrain
        screen.blit(self.sea, (0, screen.get_height() - self.sea_level))
        screen.blit(self.object_ground.image, (0, 0))
        screen.blit(self.sea, (0, screen.get_height() - self.sea_level + 20))

        # on update les players
        for player in self.all_players:
            # on affiche la vie des joueurs
            player.show_life(screen)
            if player.jumping and not player.is_falling:
                player.jump(screen)
            else:
                player.fall(screen)

            player.all_projectiles.draw(screen)
            for projectile in player.all_projectiles:
                projectile.move()

        # si il y à des joueurs sur la map
        if len(self.all_players) > 0:
            # on affiche indicateur du joueur sélectionné
            screen.blit(self.player_choice.indicator_image,
                        (self.player_choice.rect.centerx - self.player_choice.indicator_rect.centerx,
                         self.player_choice.rect.y - 25))
            # on affiche le viseur du joueur selectionné s'il a sorti une arme
            if self.player_choice.bool_equiped:
                self.player_choice.show_viseur(screen)


        # appliquer l'image du groupe de joueurs
        self.all_players.draw(screen)

    def spawn_player(self):
        # décide de l'équipe et l'équipe adverse
        if self.last_team == 0:
            new_player = Player(self, team=1)
            self.all_players_blue.add(new_player)
            new_player.equipe_adverse = self.all_players_red
            # témoin pour que le jeu alterne entre bleu et rouge
            self.last_team = 1
        else:
            new_player = Player(self, team=0)
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
            self.player_choice = tmp_list[(tmp_list.index(self.player_choice) + 1) % len(tmp_list)]
            print("joueur choisis :", self.player_choice.player_id)
        else:
            self.player_choice = None
