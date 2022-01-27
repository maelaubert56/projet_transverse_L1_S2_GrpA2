import pygame
import DEFAULT
from game import Game
from object_background import Object_background
# initialisation de pygame au lancement
pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60

# on crée la fenetre du jeu
pygame.display.set_caption(DEFAULT.window_name)
pygame.display.set_icon(pygame.image.load(DEFAULT.window_icon))

#screen = pygame.display.set_mode((0,0))

object_background = Object_background()

# on adapte la taille de la fenetre
screen = pygame.display.set_mode((object_background.rect.width+100,object_background.rect.height))


# on importe et redimmentionne l'arriere plan
background = pygame.image.load(DEFAULT.path_background)
background_rect = background.get_rect()
background_rect.width = DEFAULT.window_width
background = pygame.transform.scale(background,(background_rect.width+100,object_background.rect.height))

# on importe et redimmentionne la mer
sea = pygame.image.load(DEFAULT.path_sea)
sea_rect = sea.get_rect()
sea_rect.width = DEFAULT.window_width
sea = pygame.transform.scale(sea,(sea_rect.width+100,object_background.rect.height))

# on charge le jeu
game=Game()

# boucle principale du jeu
running = True
j = 0
i = 0

while running:
    j += 1
    if j == DEFAULT.sea_level_speed:
        j = 0
        i+=1
    #appliquer le terrain
    #screen.blit(background, (0, 0))
    screen.blit(sea, (0, screen.get_height() - 120 - i))
    screen.blit(object_background.image, (50, 0))
    screen.blit(sea, (0,screen.get_height()-100 - i))

    game.update(screen=screen)

    #mettre a jour l'ecran
    pygame.display.flip()

    # on recupere les evenements au clavier ou a la souris
    for event in pygame.event.get():
        # si on ferme la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

    #fixer le nb de FPS
    clock.tick(FPS)