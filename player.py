import pygame
import DEFAULT
import random
from math import sqrt


class Player(pygame.sprite.Sprite):
    def __init__(self, game, i):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = 5
        self.fall_velocity = 5
        self.image = pygame.image.load(DEFAULT.path_player)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()

        if DEFAULT.DEBUG:
            self.rect.x = i
        else:
            self.rect.x = 50 + random.randint(0, DEFAULT.window_width - 100)
        self.rect.y = -100
        self.mask = pygame.mask.from_surface(self.image)

    def collision(self, screen):
        collision_terrain = pygame.sprite.collide_mask(self.game.object_background, self)
        # collision_joueur = pygame.sprite.collide_mask(self.game.object_player, self)

        if collision_terrain is not None:
            pygame.draw.circle(surface=screen, color=(255, 0, 0),
                               center=(collision_terrain[0] + 50, collision_terrain[1]), radius=5)

            return collision_terrain
        return False

    def fall(self, screen):
        collision = self.collision(screen)
        if self.rect.y <= (screen.get_height() - self.game.sea_level):
            if collision is False:
                self.rect.y += self.fall_velocity
            else:
                pygame.draw.circle(surface=screen, color=(255, 0, 0),
                                   center=(collision[0] + 50, collision[1]), radius=5)
        else:
            # tuer le perso
            self.kill(self)

    def show_life(self, surface):
        police = pygame.font.SysFont("monospace", 15)
        image_texte = police.render(str(self.health), 1, (250, 0, 0))
        surface.blit(image_texte, (self.rect.x + 10, self.rect.y - 20))

    def move_right(self, screen):
        collision = self.collision(screen)
        print("collision :", collision)
        # si la collision est à moins de la moitié du perso il peut monter
        """if collision:
            if collision[1] > (self.rect.y - self.rect.y / 2):
                self.rect.x += self.velocity
                # translation de la différence entre le bas et le point de collision (vecteur de déplacement)
                self.rect.y -= sqrt(self.rect.y ** 2 + collision[1] ** 2)"""

        #self.rect.x += self.velocity

    def move_left(self, screen):
        self.rect.x -= self.velocity
