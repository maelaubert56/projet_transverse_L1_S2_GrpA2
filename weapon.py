import pygame
import DEFAULT
from ground import Ground
from math import sin, cos, sqrt
from time import sleep


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player_launcher, direction):
        super().__init__()
        self.dmg = 100
        # suriken
        self.player_launcher = player_launcher
        self.direction = direction
        self.image = pygame.image.load(DEFAULT.path_shuriken)
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.suriken_damages = 20
        # position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = player_launcher.rect.x + self.player_launcher.direction * player_launcher.rect.width, player_launcher.rect.y + 3
        self.angle = self.player_launcher.aim_angle
        self.angle_rota = 1
        self.middle_x, self.middle_y = self.rect.x + 0.5 * self.rect.width, self.rect.y + (self.rect.height / 2)
        # velocité de départ
        self.y_v = (self.player_launcher.viseur_rect.y - self.player_launcher.rect.y)/9.8 * self.player_launcher.puissance/10
        self.x_v = (self.player_launcher.viseur_rect.x - self.player_launcher.rect.x)/9.8 * self.player_launcher.puissance/10
        self.coeff_direc_y = 1
        self.coeff_direc_x = self.player_launcher.direction
        # image pour la rotation
        self.origin_img = self.image
        # explosions
        self.img_explo_current=0
        # trajectoire
        self.t_trajectory = 0
        # importation du background
        self.object_ground = Ground()

    def rotate(self):
        self.angle_rota += 7 * (self.x_v + self.y_v)
        self.image = pygame.transform.rotozoom(self.origin_img, self.angle_rota, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, screen):
        collision = pygame.sprite.collide_mask(self.object_ground, self)
        # passé dans l'explosion
        collision_player = pygame.sprite.spritecollide(self, self.player_launcher.game.all_players, False,
                                                       pygame.sprite.collide_mask)
        # si le projectile touche un objet
        if collision is not None:
            self.explosion(screen)
            self.kill()
        # si il touche le joueur
        elif len(collision_player) != 0:
            self.explosion(screen)
            self.kill()
        # verif limites de map
        elif self.rect.x > DEFAULT.window_width + 100 or self.rect.x < 0:
            self.kill()
        # sinon on fait la trajectoire
        else:
            self.rect.x += self.x_v
            # self.x_v /= 1.1
            self.rect.y += 9.8 * self.t_trajectory + self.y_v
            self.t_trajectory += 0.01
            self.rotate()

    def explosion(self, screen):
        """permet de créer un rayon de dégâts autour de l'impact de projectile"""
        # faire l'animation
        while self.img_explo_current != len(DEFAULT.tab_explo):
            screen.blit(DEFAULT.tab_explo[self.img_explo_current], (self.rect.x-self.rect.width, self.rect.y-self.rect.height))
            self.img_explo_current += 1
            # print("plusunnn :", self.img_explo_current)
            # sleep(0.1)

        # else :
        #     self.img_explo_current = 0
        # aps opti car on le fait juste avant
        collision_player = pygame.sprite.spritecollide(self, self.player_launcher.game.all_players, False,
                                                       pygame.sprite.collide_mask)
        for player in collision_player:
            player.take_damage(self.suriken_damages)
            player.vecteur(self.rect.x, self.rect.y)

    def grenade(self):
        collision = pygame.sprite.collide_mask(self.object_ground, self)
        # passé dans l'explosion
        collision_player = pygame.sprite.spritecollide(self, self.player_launcher.game.all_players, False,
                                                       pygame.sprite.collide_mask)
        # si le projectile touche un objet au dessus à droite
        if collision:
            if collision[1] > self.middle_y and collision[0] > self.middle_x:
                self.coeff_direc_y = -self.coeff_direc_y
                self.coeff_direc_x = -self.coeff_direc_x

            elif collision[1] > self.middle_y :
                self.coeff_direc_y = -self.coeff_direc_y
                # self.coeff_direc_x = -self.coeff_direc_x

            # en bas a droite
            elif collision[1] < self.middle_y and (9.8 * self.t_trajectory + self.y_v) < 0:
                self.coeff_direc_y = -self.coeff_direc_y
                self.coeff_direc_x = -self.coeff_direc_x

            # sinon on fait la trajectoire
        else:
            self.rect.x += self.x_v
            self.rect.y += (self.coeff_direc_y)*9.8 * self.t_trajectory + self.y_v
            self.t_trajectory += 0.01
            self.rotate()

        # verif limites de map
        if self.rect.x > DEFAULT.window_width + 100 or self.rect.x < 0:
            self.kill()
