import pygame
import DEFAULT
from random import randint
from weapon import Weapon
from math import cos, sin, sqrt


class Player(pygame.sprite.Sprite):
    def __init__(self, game, team: int):
        super().__init__()
        self.game = game
        # attributs de jeu
        self.health = 100
        self.max_health = 100
        self.dead = False
        self.velocity = DEFAULT.players_velocity
        self.accel = 0.2
        self.fall_velocity = 3
        # saut
        self.jumping = False
        self.t_saut = 0
        self.is_falling = False
        self.direction = 1  # -1: gauche, 1: droite
        # équipe bleue pour 0 et 1 pour rouge
        self.team = team
        self.opposing_team = None
        # image et coordonnées
        self.image_left = pygame.transform.scale(pygame.image.load(DEFAULT.path_player_img_tab[self.team][self.direction]), (30, 30))
        self.image_right = pygame.transform.scale(pygame.image.load(DEFAULT.path_player_img_tab[self.team][self.direction]), (30, 30))
        self.image = self.image_right
        self.rect = self.image.get_rect()
        # indicateur du joueur contrôlé
        self.indicator_image = pygame.transform.scale(pygame.image.load(DEFAULT.path_player_indicator), (10, 10))
        self.indicator_rect = self.indicator_image.get_rect()
        # projectiles
        self.middle_x, self.middle_y = self.rect.x + 0.5*self.rect.width, self.rect.y + (self.rect.height / 2)
        self.viseur_image = pygame.transform.scale(pygame.image.load(DEFAULT.path_arrow), (20, 20))
        self.viseur_rect = self.viseur_image.get_rect()
        self.all_projectiles = pygame.sprite.Group()
        self.bool_equipped = False
        self.aim_angle = 0
        self.origin_img = self.viseur_image
        self.puissance = 0
        self.x_v=0
        self.y_v=0
        # le jetpack
        self.bool_jetpack = False
        self.jtpck_fuel=self.rect.height
        # débogage et masks
        self.rect.x = randint(10, DEFAULT.window_width - 100)
        self.rect.y = 50
        self.mask = pygame.mask.from_surface(self.image)
        # nom du personnage (numéro pour le moment pour debug)
        self.player_id = randint(0, 1000)

    def collision(self, screen):
        collision_terrain = pygame.sprite.collide_mask(self.game.object_ground, self)
        collision_joueur = None

        if self.opposing_team is not None:
            collision_joueur = pygame.sprite.spritecollide(self, self.opposing_team, False, pygame.sprite.collide_mask)
        if collision_terrain is not None:
            if DEFAULT.DEBUG:
                pygame.draw.circle(surface=screen, color=(250, 0, 0),
                                   center=(collision_terrain[0], collision_terrain[1]), radius=5)
            return collision_terrain

        elif collision_joueur is not None and len(collision_joueur) != 0:
            if DEFAULT.DEBUG:
                pygame.draw.circle(surface=screen, color=(0, 255, 0),
                                   center=(collision_joueur[0].rect.x - self.rect.width, collision_joueur[0].rect.y),
                                   radius=5)
            # retourne la position x y de l'ennemi pas le point de collision
            return collision_joueur[0].rect.x, collision_joueur[0].rect.y

        return False

    def fall(self, screen):
        collision = self.collision(screen)
        if self.rect.y <= (screen.get_height() - self.game.sea_level):
            # diff_y= 9.8 * self.t_saut + self.y_v
            # print(" diff y",diff_y)
            if collision is False: # or self!=self.game.player_choice:
                # trajectoire chute libre
                self.rect.x += self.x_v
                # self.x_v /= 1.1
                self.rect.y += 9.8 * self.t_saut + self.y_v
                self.t_saut += 0.01
                self.is_falling = True

            # si sprite joueur touche le sol et que le deplacmeent y va vers la haut
            elif collision[1] > self.middle_y and (9.8 * self.t_saut + self.y_v) < 0:
                # trajectoire chute libre
                self.rect.x += self.x_v
                print("passage1")
                # self.x_v /= 1.1
                self.rect.y += 9.8 * self.t_saut + self.y_v
                self.t_saut += 0.01
                self.is_falling = True

            elif (9.8 * self.t_saut + self.y_v)/1.5 < 9.8:
                # reset velocity de la chute et la vitesse de chute
                self.fall_velocity = 3
                # if self != self.game.player_choice:
                #     print("reset")
                self.y_v = 0
                self.x_v = 0

                self.t_saut = 0
                self.is_falling = False
                # self.state = "nothing"
            else:
                # reset velocity de la chute et la vitesse de chute
                self.fall_velocity = 3
                # if self != self.game.player_choice:
                #     print("reset")
                self.y_v = 0
                self.x_v = 0

                self.t_saut = 0
                self.is_falling = False
                # self.state = "nothing"
        else:
            if self.game.player_choice == self:
                # changement de personnage
                self.game.change_player_choice()
            # tuer le perso s'il touche l'eau
            self.die()

    def jump(self, screen):
        if self.jumping is False:
            self.t_saut = 0
        else:
            v0, g = 5, 5
            angle = [0, 1.4, 1.74]
            a = angle[self.direction]
            collision = self.collision(screen)
            # si la collision est fausse ou en bas au debut du mouvement
            if collision is False or (collision[1] > (self.rect.y + (self.rect.height / 2)) and self.t_saut == 0):
                self.rect.x += v0 * cos(a) * self.t_saut * 2.5
                self.rect.y -= (-0.5 * g * self.t_saut * self.t_saut + v0 * sin(a))
                self.t_saut += 0.1

            # si collision est avec la tête
            elif collision[1] < (self.rect.y + (self.rect.height / 2)) and self.t_saut >= 0.1:
                self.rect.y += 5
                self.jumping = False
                self.t_saut = 0

            elif collision:
                self.jumping = False
                self.t_saut = 0

    def show_life(self, surface):
        police = pygame.font.SysFont("monospace", 15)
        if self.team == 0:
            life_text = police.render(str(self.health), True, (0, 0, 255))
        else:
            life_text = police.render(str(self.health), True, (255, 0, 0))
        surface.blit(life_text, (self.rect.centerx - life_text.get_rect().centerx, self.rect.y - 15))

    def move_right(self, screen):
        self.direction = 1
        collision = self.collision(screen)
        # si la collision est à moins de la moitié du perso il peut monter
        if collision:
            if collision[1] > (self.rect.y + (
                    self.rect.height / 2)):  # si la collision (en y) est plus basse que la moitié du rect
                self.rect.x += self.velocity
                # translation de la différence entre le bas et le point de collision (vecteur de déplacement)
                self.rect.y = collision[1] - self.rect.height

            # débloque le perso bloqué
            elif collision[0] < self.rect.x + (
                    self.rect.height / 2):  # si la collision (en x) est plus à gauche que la moitié du rect
                self.rect.x += self.velocity

            self.aim_angle = 0

    def move_left(self, screen):
        self.direction = -1
        collision = self.collision(screen)
        # si la collision est à moins de la moitié du perso il peut monter
        if collision:
            if collision[1] > (self.rect.y + (
                    self.rect.height / 2)):  # si la collision (en y) est plus basse que la moitié du rect
                self.rect.x -= self.velocity
                # translation de la différence entre le bas et le point de collision (vecteur de déplacement)
                self.rect.y = collision[1] - self.rect.height

            # débloque le perso bloqué
            elif collision[0] > self.rect.x + (
                    self.rect.height / 2):  # si la collision (en x) est plus à droite que la moitié du rect
                self.rect.x -= self.velocity

            self.aim_angle = 0

    def equip_weapon(self, var=None):
        """la variable sert a ranger ou sortir l'arme"""
        if var is not None:
            if not self.bool_equipped:
                self.bool_equipped = True
                return 1
            self.bool_equipped = False
            return 0

    def launch_projectile(self):
        # nouveau projectile
        self.all_projectiles.add(Weapon(self, self.direction))
        self.puissance = 0
        self.game.turn_per_turn(1)

    def jetpack_equip(self):
        # changer l'image du personnage pour un jetpack expliqué
        if not self.bool_jetpack:
            # range l'arme
            self.bool_equipped = False
            # soirs jetpack
            self.bool_jetpack = True
        else:
            self.bool_jetpack = False

    def use_jetpack(self, direct=(0, 0), screen=None):
        collision = self.collision(screen)
        # si pas de collision ou collision avec les pieds
        if not collision or collision[1] > (self.rect.y + (self.rect.height / 2)):
            if self.jtpck_fuel:
                self.rect.x += direct[0]
                self.rect.y += direct[1]
                self.jtpck_fuel -= 1/5
                self.t_saut = 0
        # sinon si collision avec la tête
        elif collision[1] < (self.rect.y + (self.rect.height / 2) or self.jtpck_fuel):
            self.bool_jetpack = False
            self.rect.y -= 10
        else:
            self.bool_jetpack = False

    def take_damage(self, amount):
        if self.health - amount <= 0:
            self.health = 0
            self.die()
        else:
            self.health -= amount

    def die(self):
        self.dead = True
        self.image = pygame.image.load(DEFAULT.path_player_gravestone)
        if self.team == 0:
            self.game.dead_players_blue.add(self)
            self.game.all_players_blue.remove(self)
            self.game.all_players.remove(self)
        else:
            self.game.dead_players_red.add(self)
            self.game.all_players_red.remove(self)
            self.game.all_players.remove(self)

    def show_viseur(self, direction: int, screen):
        """adapte l'image de la cible avec une sécurité d'angle"""
        # bas a droite
        if self.direction == 1 and direction < 0 and 1 > self.aim_angle:
            self.aim_angle -= (direction / 50)
            self.aim_angle = self.aim_angle

        # haut a droite
        elif self.direction == 1 and direction > 0 and self.aim_angle > -1:
            self.aim_angle -= (direction / 50)
            self.aim_angle = self.aim_angle

        # bas à gauche
        elif self.direction == -1 and direction < 0 and 1 > self.aim_angle:
            self.aim_angle -= (direction / 50)
            self.aim_angle = self.aim_angle

        # haut a gauche
        elif self.direction == -1 and direction > 0 and self.aim_angle > -1:
            self.aim_angle -= (direction / 50)
            self.aim_angle = self.aim_angle

        # changement des coordonées de l'image du viseur
        self.viseur_rect.x = self.rect.height / 2 + (self.rect.x + 50 * self.direction * cos(self.aim_angle))
        self.viseur_rect.y = self.rect.width / 2 + (self.rect.y + 50 * sin(self.aim_angle))
        screen.blit(self.viseur_image, self.viseur_rect)

    def voir_jauge(self, screen):
        bar_color = (240, 10, 46)
        bar_position = [self.rect.x, self.rect.y+self.rect.height, self.puissance, 5]
        pygame.draw.rect(screen, bar_color, bar_position)

    def voir_jauge_jtpck(self, screen):
        bar_color = (110, 210, 100)
        bar_position = [self.rect.x+self.rect.width, self.rect.y, 5, self.jtpck_fuel]
        bar_color1 = (0, 0, 0)
        bar_position1 = [self.rect.x + self.rect.width, self.rect.y, 5, self.rect.height]
        pygame.draw.rect(screen, bar_color1, bar_position1)
        pygame.draw.rect(screen, bar_color, bar_position)

    def vecteur(self, x, y):
        self.x_v = (self.rect.x -x)
        self.y_v = (self.rect.y - y)/9.8
        self.y_v = -(self.y_v**2)
        print(" ajout de :",self.x_v,"et de :",self.y_v," en y")
        # (self.player_launcher.viseur_rect.x - self.player_launcher.rect.x) / 9.8 * self.player_launcher.puissance / 10
        # (self.player_launcher.viseur_rect.y - self.player_launcher.rect.y) / 9.8 * self.player_launcher.puissance / 10
        self.t_saut += 0.01