import pygame
import DEFAULT
from ground import Ground


class Weapon(pygame.sprite.Sprite):

    def __init__(self, player_launcher):
        super().__init__()
        self.dmg = 100
        self.velocity = 10
        # suriken
        self.player_launcher = player_launcher
        self.direction = player_launcher.direction
        self.image = pygame.image.load('assets/weapons/shuriken.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.suriken_damages = 20
        # position
        self.rect = self.image.get_rect()
        if self.player_launcher.direction == 0:
            self.rect.x, self.rect.y = player_launcher.rect.x - self.player_launcher.rect.width, player_launcher.rect.y + 3
        else:
            self.rect.x, self.rect.y = player_launcher.rect.x + self.player_launcher.rect.width, player_launcher.rect.y + 3
        # image
        self.origin_img = self.image
        self.angle = 0

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
            if self.direction == 0:
                self.rect.x -= self.velocity
            else:
                self.rect.x += self.velocity
            self.rotate()
