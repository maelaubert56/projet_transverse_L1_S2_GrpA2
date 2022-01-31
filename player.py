import time

import pygame
import DEFAULT
import random
from weapon import Weapon
from math import cos,sin


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        # attrributs de jeu
        self.health = 100
        self.max_health = 100
        self.velocity = DEFAULT.players_velocity
        self.accel = 0.2
        self.fall_velocity = 3
        # image et cordonées
        self.image = pygame.image.load(DEFAULT.path_player)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        # projectiles
        self.all_projectiles = pygame.sprite.Group()
        self.direction = 0 # 0: gauche, 1: droite
        # debuggage et masks
        self.rect.x = 50 + random.randint(0, DEFAULT.window_width - 100)
        self.rect.y = -100
        self.mask = pygame.mask.from_surface(self.image)

    def collision(self, screen):
        collision_terrain = pygame.sprite.collide_mask(self.game.object_background, self)
        # collision_joueur = pygame.sprite.collide_mask(self.game.object_player, self)
        if collision_terrain is not None:
            if DEFAULT.DEBUG: pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(collision_terrain[0] + 50, collision_terrain[1]), radius=5)
            return collision_terrain
        return False

    def fall(self, screen):
        collision = self.collision(screen)
        if self.rect.y <= (screen.get_height() - self.game.sea_level):
            if collision is False:
                # trajectoire chute libre
                self.rect.y += self.fall_velocity
                self.fall_velocity = self.fall_velocity + self.accel
            else:
                # reset velocity de la chute et la vitesse de chute
                self.fall_velocity = 3
                # témoin de collision
                if DEFAULT.DEBUG : pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(collision[0] + 50, collision[1]), radius=5)
        else:
            # tuer le perso s'il touche l'eau
            self.kill()

    def show_life(self, surface):
        police = pygame.font.SysFont("monospace", 15)
        image_texte = police.render(str(self.health), 1, (250, 0, 0))
        surface.blit(image_texte, (self.rect.x + 10, self.rect.y - 20))


    def move_right(self, screen):
        self.direction = 1
        collision = self.collision(screen)
        # si la collision est à moins de la moitié du perso il peut monter
        if collision:
            if collision[1] > (self.rect.y + (self.rect.height / 2)):
                self.rect.x += self.velocity
                # translation de la différence entre le bas et le point de collision (vecteur de déplacement)
                self.rect.y = collision[1] - self.rect.height
            # débloque le perso bloqué
            elif collision[0] < self.rect.x-self.rect.width:
                self.rect.x += self.velocity

    def move_left(self, screen):
        self.direction = 0
        collision = self.collision(screen)
        # si la collision est à moins de la moitié du perso il peut monter
        if collision:
            if collision[1] > (self.rect.y + (self.rect.height / 2)):
                self.rect.x -= self.velocity
                # translation de la différence entre le bas et le point de collision (vecteur de déplacement)
                self.rect.y = collision[1] - self.rect.height
            # débloque le perso bloqué
            elif collision[0] > self.rect.x-self.rect.width:
                self.rect.x -= self.velocity


    def jump(self,screen):
        v0, g, t, jumping = 6.3*10, 19, 0, False
        x0, y0 = self.rect.x, self.rect.y
        if self.direction == 1 : a = 1.31
        else : a = 1.83

        while t < 1:
            t += 1/1000
            collision = self.collision(screen)
            if collision==False or jumping == False or t<= 0.2:
                self.rect.x = x0 + v0 * cos(a) * t
                self.rect.y = y0 -(-0.5 * g * t*t + v0 * sin(a) * t)
                jumping = True
                #print("t=",round(t,2),"x=",self.rect.x,"y=",self.rect.y)

            else:
                jumping = False
                t=1




    def launch_projectile(self):
        # nouveau projectile
        self.all_projectiles.add(Weapon(self))


