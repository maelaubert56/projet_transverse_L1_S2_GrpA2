import pygame
import DEFAULT

# initialisation de pygame au lancement
pygame.init()


# on crée la fenetre du jeu
pygame.display.set_caption(DEFAULT.window_name)
pygame.display.set_icon(pygame.image.load(DEFAULT.window_icon))


# on importe l'arriere plan et on redimendionne l'image
terrain = pygame.image.load(DEFAULT.path_terrain)
terrain_rect = terrain.get_rect()
terrain_rect.width = DEFAULT.window_width
terrain_rect.height = DEFAULT.window_width * terrain_rect.height/ terrain_rect.width
terrain = pygame.transform.scale(terrain,(terrain_rect.width,terrain_rect.height))

# on adapte la taille de la fenetre
screen = pygame.display.set_mode((terrain_rect.width+100,terrain_rect.height))

# on importe et redimmentionne l'arriere plan
background = pygame.image.load(DEFAULT.path_background)
background_rect = background.get_rect()
background_rect.width = DEFAULT.window_width
background = pygame.transform.scale(background,(background_rect.width+100,terrain_rect.height))

# on importe et redimmentionne la mer
sea = pygame.image.load(DEFAULT.path_sea)
sea_rect = sea.get_rect()
sea_rect.width = DEFAULT.window_width
sea = pygame.transform.scale(sea,(sea_rect.width+100,terrain_rect.height))

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
    screen.blit(background, (0, 0))
    screen.blit(sea, (0, screen.get_height() - 120 - i))
    screen.blit(terrain, (50, 0))
    screen.blit(sea, (0,screen.get_height()-100 - i))


    #mettre a jour l'ecran
    pygame.display.flip()

    # on recupere les evenements au clavier ou a la souris
    for event in pygame.event.get():
        # si on ferme la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")