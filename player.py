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

        # attributs du joueur
        self.health = 100
        self.max_health = 100
        self.velocity = DEFAULT.players_velocity
        self.accel = 0.2
        self.fall_velocity = 3

        # image et cordonées
        self.image_normal = pygame.image.load(DEFAULT.path_player)
        self.image = self.image_normal
        self.image_normal = [pygame.transform.flip(self.image_normal, True, False), self.image_normal]
        self.image_chute = pygame.image.load("assets/player/adventurer/adventurer-fall-00.png")
        #self.image = pygame.transform.scale(self.image, (30, 30)) # pour le "knight", mettre (30,30)
        self.rect = self.image.get_rect()
        self.direction = 1 # par defaut, le joueur regarde à droite (1)
        self.temps_de_chute = 0 # utilisé pour savoir depuis combien de temps le joueur est en chute libre

        # projectiles
        self.all_projectiles = pygame.sprite.Group()

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
                # image de chute si la chute dure assez longtemps
                if self.temps_de_chute > 30:
                    self.image = self.image_chute
                else : self.image = self.image_normal[self.direction]
                self.temps_de_chute += 1
            else:
                # reset de la vitesse de chute et du temps de chute
                self.fall_velocity = 3
                self.temps_de_chute = 0
                # image normale dans la bonne direction
                self.image = self.image_normal[self.direction]
                # témoin de collision
                if DEFAULT.DEBUG : pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(collision[0] + 50, collision[1]), radius=5)
        else:
            # tuer le perso s'il touche l'eau
            self.kill()
            # on change le focus sur un autre joueur
            self.game.change_player_choice()

    def show_life(self, surface):
        police = pygame.font.SysFont("monospace", 15)
        image_texte = police.render(str(self.health), 1, (250, 0, 0))
        surface.blit(image_texte, (self.rect.x + 10, self.rect.y - 20))


    def move_right(self, screen):
        self.direction = 1
        self.image = self.image_normal[self.direction]
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
        self.image = self.image_normal[self.direction]
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
        v0, g, t, jumping = 6.3*12, 19, 0, False
        x0, y0 = self.rect.x, self.rect.y
        if self.direction == 1 : a = 1.15
        else : a = 2

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


