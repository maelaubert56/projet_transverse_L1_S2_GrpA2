import pygame
import DEFAULT
from game import Game
from background_file import Background

# initialisation de pygame au lancement
pygame.init()

# definir une clock
clock = pygame.time.Clock()

# on crée la fenetre du jeu
pygame.display.set_caption(DEFAULT.window_name)
pygame.display.set_icon(pygame.image.load(DEFAULT.window_icon))

pygame.mixer.music.load(DEFAULT.path_music)  # import du fichier
pygame.mixer.music.play()  # on joue le fichier
pygame.mixer.music.set_volume(DEFAULT.music_level)

object_background = Background()

# on adapte la taille de la fenetre
screen = pygame.display.set_mode((object_background.rect.width + 100, object_background.rect.height))

# on importe et redimmentionne l'arriere plan
background = pygame.image.load(DEFAULT.path_background)
background_rect = background.get_rect()
background_rect.width = DEFAULT.window_width
background = pygame.transform.scale(background, (background_rect.width + 100, object_background.rect.height))

# on importe et redimmentionne la mer
sea = pygame.image.load(DEFAULT.path_sea)
sea_rect = sea.get_rect()
sea_rect.width = DEFAULT.window_width
sea = pygame.transform.scale(sea, (sea_rect.width + 100, object_background.rect.height))

# on charge le jeu
game = Game()

# boucle principale du jeu
running = True
j = 0

# spawn 2 joueur pour éviter les bugs de touches
game.spawn_player()
game.spawn_player()

while running:

    # verif de la mort subite
    if game.bool_ms:
        game.sea_level += 1

    # appliquer le terrain
    screen.blit(background, (0, 0))
    # appliquer l'eau sur le terrain
    screen.blit(sea, (0, screen.get_height() - game.sea_level))
    screen.blit(object_background.image, (50, 0))
    screen.blit(sea, (0, screen.get_height() - game.sea_level + 20))

    game.update(screen=screen)
    # montre la vie du perso selctionné, et l'ulilise comme indicateur de séléction
    if len(game.all_players) > 0:
        game.player_choice.show_life(screen)

    # mettre a jour l'ecran
    pygame.display.flip()

    # touches pressées par le joueur
    if game.player_choice:
        if game.pressed.get(pygame.K_RIGHT):
            game.player_choice.move_right(screen)
        elif game.pressed.get(pygame.K_LEFT):
            game.player_choice.move_left(screen)

    # on recupere les evenements au clavier ou a la souris
    """# !! possibilité de remplacer par un case ? pour plus d'optimisation"""
    for event in pygame.event.get():
        # si on ferme la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # touches de jeu
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # detection des touches du jeu
            if event.key == pygame.K_RETURN:
                game.start()
            # mort subite
            elif event.key == pygame.K_m:
                game.bool_ms = True
            # touche changement de personnage
            elif event.key == pygame.K_c:
                game.change_player_choice()
            # touche de tir /saut
            elif event.key == pygame.K_SPACE:
                if game.player_choice:
                    if game.player_choice.bool_equiped:
                        game.player_choice.launch_projectile()
                    else:
                        game.player_choice.jump(screen)
            # équiper une arme ou la ranger
            elif event.key == pygame.K_x:
                print("A")
                game.player_choice.equip_weapon(True)

            # detection des touches du joueur
            else:
                game.pressed[event.key] = True
                #game.player_choice.equip_weapon(False)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    # fixer le nb de FPS
    clock.tick(DEFAULT.FPS)
