import pygame
import DEFAULT
from ground import Ground
from math import sin, cos
class Weapon(pygame.sprite.Sprite):
    def __init__(self, player_launcher, direction):
        super().__init__()
        self.dmg = 100
        self.velocity = 10
        # suriken
        self.player_launcher = player_launcher
        self.direction = direction
        self.image = pygame.image.load(DEFAULT.path_shuriken)
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.suriken_damages = 20
        # position
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = player_launcher.rect.x + self.player_launcher.direction * player_launcher.rect.width, player_launcher.rect.y + 3
        # image
        self.origin_img = self.image
        self.angle = self.player_launcher.aim_angle
        # trajectoire
        self.t_trajectory = 0

        #angle = [1.74, 1.4]
        #self.a = angle[self.direction]

        # importation du background
        self.object_ground = Ground()

    def rotate(self):
        self.angle += 7
        self.image = pygame.transform.rotozoom(self.origin_img, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        collision = pygame.sprite.collide_mask(self.object_ground, self)
        collision_player = pygame.sprite.spritecollide(self, self.player_launcher.game.all_players, False,
                                                       pygame.sprite.collide_mask)
        # si le projectile touche un objet
        if collision is not None:
            self.kill()
        # si il touche le joueur
        elif len(collision_player) != 0:
            for player in collision_player:
                player.take_damage(self.suriken_damages)
            self.kill()
        # verif limites de map
        elif self.rect.x > DEFAULT.window_width + 10 or self.rect.x < -10:
            self.kill()
        # sinon on fait la trajectoire
        else:
            v0, g = 5, 9.8
            self.angle = (3.1415)/4
            print(f"angle degré: {self.angle} ; ")
            # angle = [1.74, 1.4]
            # self.a = angle[self.player_launcher.direction]
            #self.angle = self.angle * 3.14/180 # trasnfo en radians
            print(f"angle radian: {self.angle} ; direction:{self.direction} ")
            self.rect.x += -v0 * cos(3.14-self.player_launcher.aim_angle/4)*self.direction
            self.rect.y += g * self.t_trajectory * self.t_trajectory - v0 * sin(3.14-self.angle)
            self.t_trajectory += 0.01
            self.rotate()

    def explosion(self):
        """permet de créer un rayon de dégat autour de l'impact de l'arme"""
        pass