import pygame
import DEFAULT


class Background(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # on importe l'arrière-plan et on redimensionne l'image
        self.image = pygame.image.load(DEFAULT.path_terrain)
        self.rect = self.image.get_rect()
        self.rect.width = DEFAULT.window_width
        self.rect.height = DEFAULT.window_width * self.rect.height / self.rect.width
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        self.mask = pygame.mask.from_surface(self.image)
