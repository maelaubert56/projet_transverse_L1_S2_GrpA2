import pygame
import DEFAULT
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,game,i):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = 5
        self.fall_velocity = 5
        self.image = pygame.image.load(DEFAULT.path_player)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        if DEFAULT.DEBUG : self.rect.x = i
        else : self.rect.x = 50 + random.randint(0,DEFAULT.window_width-100)
        self.rect.y = -100
        self.mask = pygame.mask.from_surface(self.image)

    def fall(self,screen):
        collision_terrain = pygame.sprite.collide_mask(self.game.object_background,self)

        if self.rect.y <= (screen.get_height() - self.game.sea_level):
            if collision_terrain !=None :
                pygame.draw.circle(surface=screen, color=(255, 0, 0), center=(collision_terrain[0]+50,collision_terrain[1]), radius=5)
            else:
                self.rect.y += self.fall_velocity
        else:
            pygame.draw.circle(surface=screen, color=(255, 0, 255),center=(self.rect.x+15,self.rect.y+30), radius=5)


