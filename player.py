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
        self.dead = False
        self.velocity = DEFAULT.players_velocity
        self.accel = 0.2
        self.fall_velocity = 3
        # ↓ état actuel du joueur,peut contenir : "nothing", "falling", "flying", "jumping", "dead", "walking", "aiming"
        self.state = "nothing"
        # saut
        self.jumping = False
        self.t_saut = 0
        self.is_falling = False
        # équipe bleue pour 0 et 1 pour rouge
        self.team = team
        self.opposing_team = None
        # image et coordonnées
        self.image = pygame.image.load(DEFAULT.path_player_img_tab[self.team])
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        # indicateur du joueur contrôlé
        self.indicator_image = pygame.image.load(DEFAULT.path_player_indicator)
        self.indicator_image = pygame.transform.scale(self.indicator_image, (10, 10))
        self.indicator_rect = self.indicator_image.get_rect()
        # projectiles
        self.viseur_image = pygame.image.load(DEFAULT.path_arrow)
        self.viseur_rect = self.viseur_image.get_rect()
        self.all_projectiles = pygame.sprite.Group()
        self.direction = 0  # 0: gauche, 1: droite
        self.bool_equipped = False
        self.aim_angle = self.direction * 90
        self.origin_img = self.viseur_image
        # le jetpack
        self.bool_jetpack = False
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
            if collision is False:
                # trajectoire chute libre
                self.rect.y += self.fall_velocity
                if self.fall_velocity < 20:
                    self.fall_velocity = self.fall_velocity + self.accel
                self.is_falling = True
                self.state = "falling"
            else:
                # reset velocity de la chute et la vitesse de chute
                self.fall_velocity = 3
                self.is_falling = False
                self.state = "nothing"
        else:
            if self.game.player_choice == self:
                # changement de personnage
                self.game.change_player_choice()
            # tuer le perso s'il touche l'eau
            self.kill()

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
                self.state = "walking_right"
            # débloque le perso bloqué
            elif collision[0] < self.rect.x + (
                    self.rect.height / 2):  # si la collision (en x) est plus à gauche que la moitié du rect
                self.rect.x += self.velocity
                self.state = "walking_right"
            self.aim_angle = 0

    def move_left(self, screen):
        self.direction = 0
        collision = self.collision(screen)
        # si la collision est à moins de la moitié du perso il peut monter
        if collision:
            if collision[1] > (self.rect.y + (
                    self.rect.height / 2)):  # si la collision (en y) est plus basse que la moitié du rect
                self.rect.x -= self.velocity
                # translation de la différence entre le bas et le point de collision (vecteur de déplacement)
                self.rect.y = collision[1] - self.rect.height
                self.state = "walking_left"
            # débloque le perso bloqué
            elif collision[0] > self.rect.x + (
                    self.rect.height / 2):  # si la collision (en x) est plus à droite que la moitié du rect
                self.rect.x -= self.velocity
                self.state = "walking_left"
            self.aim_angle = 0

    def jump(self, screen):
        if self.jumping is False:
            self.t_saut = 0
        else:
            v0, g = 5, 5
            angle = [1.74, 1.4]
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

            """ pas besoins de cette condition : ?
            # si collision avec la tête au debut du mouvement
            elif collision[1] < (self.rect.y + (self.rect.height / 2)) and self.t_saut == 0:
                self.jumping = False
                self.t_saut = 0
            """

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
        self.all_projectiles.add(Weapon(self))

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
        # si pas de collision ou collision avec la tête
        if not collision or collision[1] > (self.rect.y + (self.rect.height / 2)):
            self.rect.y += direct[1]
            self.rect.x += direct[0]
        elif collision[1] < (self.rect.y + (self.rect.height / 2)):
            self.bool_jetpack = False
            self.rect.y -= 10
        else:
            self.bool_jetpack = False

    def take_damage(self, amount):
        if self.health - amount <= 0:
            self.health = 0
            print("Le joueur", self.player_id, "est mort. (lancement de l'animation de mort, puis .kill() du player)")
            self.die()
        else:
            self.health -= amount

    def die(self):
        self.state = "dead"
        self.dead = True
        self.image = pygame.image.load(DEFAULT.path_player_gravestone)

    def adjust_aim(self, direction: int):
        """
        ajuste la visée vers le haut si direct >0 sinon vers le bas (+- 1 px)
        :param direction: int , reçois un positif pour monter, négatif pour descendre
        :return:
        """
        # aller vers le haut si pas déja trop haut
        if (direction > 0 and (self.aim_angle != 90)) or (direction < 0 and (self.aim_angle != -90)):
            self.aim_angle += direction
            if self.direction == 0:
                self.viseur_image = pygame.transform.rotozoom(self.origin_img, -self.aim_angle, 1)
                #temp = (self.rect.center[0]-self.rect.width,self.rect.center[1])
                self.rect = self.image.get_rect(center=self.rect.center)
            else:

                self.viseur_image = pygame.transform.rotozoom(self.origin_img, self.aim_angle, 1)
                #temp = (self.rect.center[0]+self.rect.width, self.rect.center[1])
                self.rect = self.image.get_rect(center=self.rect.center)


    def show_viseur(self, screen):
        """À placer dans le fichier "weapon" ? """
        self.viseur_rect.x, self.viseur_rect.y = self.rect.x + 15, self.rect.y + 10
        if self.direction == 1:
            screen.blit(self.viseur_image, self.viseur_rect)
        else:
            screen.blit(pygame.transform.rotate(self.viseur_image, 180),
                        (self.viseur_rect.x - self.viseur_rect.width, self.viseur_rect.y))
