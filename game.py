import pygame.sprite
import DEFAULT
from player import Player
from ground import Ground


class Game:
    def __init__(self):
        self.is_playing = int(DEFAULT.DEBUG is True)
        # joueurs et équipes
        self.all_players = pygame.sprite.Group()
        self.all_players_blue = pygame.sprite.Group()
        self.all_players_red = pygame.sprite.Group()
        self.liste_team = [self.all_players, self.all_players_blue, self.all_players_red]
        self.player_per_team = DEFAULT.player_per_team
        self.team_turn = 0 # tour de jeu (bleu en 1ers)

        # joueurs morts
        self.dead_players_blue = pygame.sprite.Group()
        self.dead_players_red = pygame.sprite.Group()
        # décors
        self.object_ground = Ground()
        self.sea_level = DEFAULT.sea_level
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
        self.sea_x_mov = 0
        # mort subite
        self.bool_ms = False
        # dictionnaire de touches
        self.pressed = {}
        # player sélectionné pour jouer
        self.player_choice = None
        # équipes
        self.last_team = 0

        # images gameover
        self.image_gameover = pygame.image.load(DEFAULT.path_bouton_gameover)
        self.image_gameover_rect = self.image_gameover.get_rect()
        self.image_gameover_rect.x = DEFAULT.window_width / 2
        self.image_gameover_rect.y = 300

        # image txt GameOver
        self.gameovertxt = pygame.image.load(DEFAULT.path_gameover)
        self.gameovertxt_rect = self.gameovertxt.get_rect()
        self.gameovertxt = pygame.transform.scale(self.gameovertxt, (1402 * 0.7, 999 * 0.7))
        self.gameovertxt_rect.x = 220
        self.gameovertxt_rect.y = 50

        # image RedWIns
        self.redwins = pygame.image.load(DEFAULT.path_redwins)
        self.redwins_rect = self.redwins.get_rect()
        self.redwins = pygame.transform.scale(self.redwins, (1402 * 0.7, 999 * 0.7))
        self.redwins_rect.x = 240
        self.redwins_rect.y = 100

        #image BlueWins
        self.bluewins = pygame.image.load(DEFAULT.path_bluewins)
        self.bluewins_rect = self.bluewins.get_rect()
        self.bluewins = pygame.transform.scale(self.bluewins, (1402 * 0.7, 999 * 0.7))
        self.bluewins_rect.x = 240
        self.bluewins_rect.y = 100

    # winners 0 bleu 1 rouge
    def start(self):
        self.is_playing = 1
        for i in range(0, DEFAULT.player_per_team*2):
            self.spawn_player()

    def gameover(self, screen):
        self.is_playing = -1
        screen.blit(self.image_gameover, self.image_gameover_rect)
        screen.blit(self.gameovertxt, self.gameovertxt_rect)
        if self.winers == 0 :
            screen.blit(self.bluewins, self.bluewins_rect)
        elif self.winers == 1 :
            screen.blit(self.redwins, self.redwins_rect)


    def update(self, screen):
        # appliquer le terrain
        screen.blit(self.background, (0, 0))
        # appliquer l'eau sur le terrain
        screen.blit(self.sea, (0, screen.get_height() - self.sea_level))
        screen.blit(self.object_ground.image, (0, 0))
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
                projectile.move(screen=screen)
        # si il y a des joueurs sur la map
        if len(self.all_players) > 0:
            # on affiche indicateur du joueur sélectionné
            screen.blit(self.player_choice.indicator_image,
                        (self.player_choice.rect.centerx - self.player_choice.indicator_rect.centerx,
                         self.player_choice.rect.y - 25))
            # on affiche le viseur du joueur sélectionné s'il a sorti une arme
            if self.player_choice.bool_equipped:
                self.player_choice.show_viseur(0, screen)

        # si une des deux équipe a perdu:
        if len(self.dead_players_red) == self.player_per_team:
            self.is_playing = -1
            self.winers = 0
        elif len(self.dead_players_blue) == self.player_per_team:
            self.is_playing = -1
            self.winers = 1

        # on fait monter l'eau (verif de la mort subite)
        if self.bool_ms:
            self.sea_level += 1

        # appliquer l'image du groupe de joueurs
        self.all_players.draw(screen)
        self.dead_players_red.draw(screen)
        self.dead_players_blue.draw(screen)

        # on update le 1er plan
        screen.blit(self.sea, (-self.sea_x_mov, screen.get_height() - self.sea_level + 20))

    def spawn_player(self):
        # décide de l'équipe et l'équipe adverse
        if self.last_team == 0:
            new_player = Player(self, team=1)
            self.all_players_blue.add(new_player)
            new_player.opposing_team = self.all_players_red
            # témoin pour que le jeu alterne entre bleu et rouge
            self.last_team = 1
        else:
            new_player = Player(self, team=0)
            self.all_players_red.add(new_player)
            new_player.opposing_team = self.all_players_blue
            # témoin pour que le jeu alterne entre bleu et rouge
            self.last_team = 0

        # ajoute le nouveau joueur dans la liste des joueurs
        self.all_players.add(new_player)
        # le focus est mis sur le nouveau player
        self.player_choice = new_player


    def change_player_choice(self):
        tmp_list = []

        if self.team_turn == 0:
            players = self.all_players_blue
        else:
            players = self.all_players_red

        for player in self.all_players:
            tmp_list.append(player)

        if len(tmp_list) != 0:
            self.player_choice = tmp_list[(tmp_list.index(self.player_choice) + 1) % len(tmp_list)]
            print("joueur choisis :", self.player_choice.player_id)
        else:
            self.player_choice = None

    def reset(self):
        for player in self.all_players:
            player.kill()
        for player in self.dead_players_blue:
            player.kill()
        for player in self.dead_players_red:
            player.kill()

        self.sea_level = DEFAULT.sea_level
        self.is_playing = 0
        self.bool_ms = 0
