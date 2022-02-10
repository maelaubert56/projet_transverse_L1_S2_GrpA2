import pygame
import DEFAULT
from background_file import Background


class Weapon(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.dmg = 100
        self.velocity = 10
        # image
        self.player = player
        self.direction = player.direction
        self.image = pygame.image.load('assets/shuriken.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        # position
        self.rect = self.image.get_rect()
        if self.player.direction == 0:
            self.rect.x, self.rect.y = player.rect.x - self.player.rect.width, player.rect.y
        else:
            self.rect.x, self.rect.y = player.rect.x + self.player.rect.width, player.rect.y
        # image
        self.origin_img = self.image
        self.angle = 0

        # importation du background
        self.object_background = Background()

    def rotate(self):
        self.angle += 7
        self.image = pygame.transform.rotozoom(self.origin_img, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self):
        collision = pygame.sprite.collide_mask(self.object_background, self)
        collision_joueur = pygame.sprite.spritecollide(self, self.player.game.all_players, False,
                                                       pygame.sprite.collide_mask)
        print("collsion_joueur", collision_joueur)
        if collision is not None:
            self.kill()
            print("collision projectil terrain")
        elif len(collision_joueur) != 0:
            print("dégats sur l'ennemi")
            self.kill()
        if self.rect.x > DEFAULT.window_width or self.rect.x < 0:
            self.kill()
            print("sortie de la fenetre")
        if self.direction == 0:
            self.rect.x -= self.velocity
        else:
            self.rect.x += self.velocity
        self.rotate()

