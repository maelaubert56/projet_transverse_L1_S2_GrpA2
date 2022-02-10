import pygame
import DEFAULT
from game import Game
from menu import Menu
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

# on charge le jeu
game = Game()

# on charge le menu
menu = Menu()

# boucle principale du jeu
running = True
j = 0
is_playing = DEFAULT.DEBUG
menu_number = 0

while running:
    # verif de la mort subite
    if game.bool_ms:
        game.sea_level += 1

    if is_playing:
        game.update(screen=screen)
    else:
        menu.update(screen=screen,menu_number = menu_number)

    # montre la vie du perso selctionné, et l'ulilise comme indicateur de séléction
    if len(game.all_players) > 0:
        game.player_choice.show_life(screen)

    # mettre a jour l'ecran
    pygame.display.flip()

    # touches pressées par le joueur
    if game.player_choice:

        if game.pressed.get(pygame.K_RIGHT):
            if game.player_choice.bool_jetpack:
                game.player_choice.use_jetpack((5, 0))
            else:
                game.player_choice.move_right(screen)

        elif game.pressed.get(pygame.K_LEFT):
            if game.player_choice.bool_jetpack:
                game.player_choice.use_jetpack((-5, 0))
            else:
                game.player_choice.move_left(screen)

        elif game.pressed.get(pygame.K_SPACE) and game.player_choice.jetpack_equip:
            print("témoijnnn", game.player_choice.bool_jetpack)
            game.player_choice.fall_velocity = 0
            game.player_choice.use_jetpack((0, -5))

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
            # si on est in game
            if is_playing:
                # detection des touches du jeu

                # menu pause
                if event.key == pygame.K_ESCAPE:
                    menu_number = 2
                    is_playing = False
                elif event.key == pygame.K_RETURN:
                    game.start()

                # mort subite
                elif event.key == pygame.K_m:
                    game.bool_ms = True

                # touche changement de personnage
                elif event.key == pygame.K_c:
                    game.change_player_choice()

                # touche de tir /saut
                elif event.key == pygame.K_SPACE:

                    if game.player_choice is not None:

                        if game.player_choice.bool_equiped:
                            game.player_choice.launch_projectile()
                        # elif game.player_choice.bool_jetpack:
                        #     game.player_choice.jetpack_equip()
                        elif not game.player_choice.bool_jetpack:
                            game.player_choice.jumping = True

                # équiper une arme ou la ranger
                elif event.key == pygame.K_x:
                    if not game.player_choice.bool_equiped:
                        game.player_choice.equip_weapon(True)
                    else: game.player_choice.equip_weapon(False)
                # jetpack
                elif event.key == pygame.K_j:
                    game.player_choice.jetpack_equip()
                # detection des touches du joueur
                else:
                    game.pressed[event.key] = True
                    # game.player_choice.equip_weapon(False)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # detecter si on clique
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu.settings_rect.collidepoint(event.pos):
                menu_number = 1
            elif menu.return_rect.collidepoint(event.pos):
                menu_number = 0
            elif menu.credit_rect.collidepoint(event.pos):
                menu_number = 4
            elif menu.info_rect.collidepoint(event.pos):
                menu_number = 3
            elif menu.play_rect.collidepoint(event.pos):
                is_playing = True
                menu_number = 0
            elif menu.sound_rect.collidepoint(event.pos):
                if DEFAULT.music_level == 0:
                    DEFAULT.music_level = 10
                    pygame.mixer.music.set_volume(10)
                else:
                    DEFAULT.music_level = 0
                    pygame.mixer.music.set_volume(0)

            # fonction de debug pour placer le joueur au clic
            if len(game.all_players.sprites())!=0 and is_playing and DEFAULT.DEBUG:
                game.player_choice.rect.x = event.pos[0]
                game.player_choice.rect.y = event.pos[1]





    # fixer le nb de FPS
    clock.tick(DEFAULT.FPS)