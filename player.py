import pygame
import DEFAULT
from random import randint
from weapon import Weapon
from math import cos, sin


class Player(pygame.sprite.Sprite):
    def __init__(self, game, team: int):
        super().__init__()
        self.game = game
        # attributs de jeu
        self.health = 100
        self.max_health = 100
        self.velocity = DEFAULT.players_velocity
        self.accel = 0.2
        self.fall_velocity = 3
        # saut
        self.jumping = False
        self.t_saut = 0
        # equipes bleu pour 0 et 1 pour rouge
        self.team = team
        self.equipe_adverse = None
        # image et coordonées
        self.image = pygame.image.load(DEFAULT.img_team[self.team])
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        # projectiles
        self.all_projectiles = pygame.sprite.Group()
        self.direction = 0  # 0: gauche, 1: droite
        self.bool_equiped = False
        # le jetpack s'acitve si et seulement si on on a pas l'arme
        # debogage et masks
        self.rect.x = randint(10, DEFAULT.window_width - 100)
        self.rect.y = 50
        self.mask = pygame.mask.from_surface(self.image)

    def collision(self, screen):
        collision_terrain = pygame.sprite.collide_mask(self.game.object_background, self)
        collision_joueur = None
        if self.equipe_adverse is not None:
            # print(" ennemis et tt :", len(self.equipe_adverse), "bloods", len(self.game.all_players_red), " crips ", len(self.game.all_players_blue))
            collision_joueur = pygame.sprite.spritecollide(self, self.equipe_adverse, False, pygame.sprite.collide_mask)
        if collision_terrain is not None:
            if DEFAULT.DEBUG:
                pygame.draw.circle(surface=screen, color=(255, 0, 0),
                                   center=(collision_terrain[0] + 50, collision_terrain[1]), radius=5)
            return collision_terrain

        elif collision_joueur is not None and len(collision_joueur) != 0 :
                """if DEFAULT.DEBUG:
                pygame.draw.circle(surface=screen, color=(0, 255, 0),
                                   center=(collision_joueur[0] + 50, collision_joueur[1]), radius=5)"""
                print("collision :", collision_joueur)
                return self.rect.x, self.rect.y #collision_joueur.rect.x, collision_joueur.rect.y
        return False

    def fall(self, screen):
        collision = self.collision(screen)
        if self.rect.y <= (screen.get_height() - self.game.sea_level):
            if (not collision):
                # trajectoire chute libre
                self.rect.y += self.fall_velocity
                self.fall_velocity = self.fall_velocity + self.accel
            else:
                # reset velocity de la chute et la vitesse de chute
                self.fall_velocity = 3
                # témoin de collision
                if DEFAULT.DEBUG:
                    pygame.draw.circle(surface=screen, color=(255, 0, 0),
                                       center=(collision[0] + 50, collision[1]), radius=5)
        else:
            if self.game.player_choice == self:
                # changement de personnage
                self.game.change_player_choice()
            # tuer le perso s'il touche l'eau
            self.kill()

    def show_life(self, surface):
        police = pygame.font.SysFont("monospace", 15)
        image_texte = police.render(str(self.health), True, (250, 0, 0))
        surface.blit(image_texte, (self.rect.x + 5, self.rect.y - 20))

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
            elif collision[0] < self.rect.x - self.rect.width:
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
            elif collision[0] > self.rect.x - self.rect.width:
                self.rect.x -= self.velocity

    def jump(self, screen):
        if self.jumping is False:
            self.t_saut=0
        else:
            # v0, g= 6.3 * 10, 19
            v0, g = 10, 10
            x0, y0 = self.rect.x, self.rect.y
            if self.direction == 1:
                a = 1.4
            else:
                a = 1.74

            self.t_saut += 0.1
            collision = self.collision(screen)
            print(collision)
            print(self.rect)
            if collision is False or (collision[0]<self.rect.x+30 and self.t_saut<=0.2):
                self.rect.x = x0 + v0 * cos(a) * self.t_saut
                self.rect.y = y0 - (-0.5 * g * self.t_saut * self.t_saut + v0 * sin(a) * self.t_saut)
                # print("t=",round(t,2),"x=",self.rect.x,"y=",self.rect.y)

            else:

                self.jumping = False
                self.t_saut = 0

    def equip_weapon(self, var=None):
        """la variable sert a ranger ou sortir l'arme"""
        if var is not None:
            if not self.bool_equiped:
                self.bool_equiped = True
                return 1
            self.bool_equiped = False
            return 0

    def launch_projectile(self):
        # nouveau projectile
        self.all_projectiles.add(Weapon(self))

    def use_jetpack(self):
        self.rect.y -= 1