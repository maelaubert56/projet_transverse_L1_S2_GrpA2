import pygame
import DEFAULT
from game import Game
from menu import Menu
from ground import Ground

# initialisation de pygame au lancement
pygame.init()

# définir une clock
clock = pygame.time.Clock()

# on crée la fenêtre du jeu
pygame.display.set_caption(DEFAULT.window_name)
pygame.display.set_icon(pygame.image.load(DEFAULT.window_icon))

pygame.mixer.music.load(DEFAULT.path_music)  # import du fichier
pygame.mixer.music.play()  # on joue le fichier
pygame.mixer.music.set_volume(DEFAULT.music_level)

object_ground = Ground()

# on adapte la taille de la fenêtre
screen = pygame.display.set_mode((object_ground.rect.width + 100, object_ground.rect.height))

# on charge le jeu
game = Game()

# on charge le menu
menu = Menu()

# boucle principale du jeu
running = True
j = 0
menu_number = 0

while running:
    # verif de la mort subite
    if game.bool_ms:
        game.sea_level += 1

    if game.is_playing == 1:
        game.update(screen=screen)
    elif game.is_playing == 0:
        menu.update(screen=screen, menu_number=menu_number)
    elif game.is_playing == -1:
        game.gameover(screen=screen)

    # mettre a jour l'écran
    pygame.display.flip()

    # touches pressées par le joueur
    if game.player_choice:
        """
        Possibilité d'optimiser le saut ici ?
        """
        if game.pressed.get(pygame.K_RIGHT):
            if game.player_choice.bool_jetpack:
                game.player_choice.use_jetpack((5, 0), screen)
                game.player_choice.state = "flying"
                if game.player_choice.state != "flying":
                    game.player_choice.state = "flying"
                    print("flying")
            else:
                game.player_choice.move_right(screen)

        elif game.pressed.get(pygame.K_LEFT):
            if game.player_choice.bool_jetpack:
                game.player_choice.use_jetpack((-5, 0), screen)
                if game.player_choice.state != "flying":
                    game.player_choice.state = "flying"
                    print("flying")
            else:
                game.player_choice.move_left(screen)

        if game.pressed.get(pygame.K_SPACE) and game.player_choice.bool_jetpack:
            game.player_choice.fall_velocity = -1
            game.player_choice.use_jetpack((0, -5), screen)
            if game.player_choice.state != "flying":
                game.player_choice.state = "flying"

        elif game.player_choice.bool_jetpack and game.player_choice.collision == False:
            game.player_choice.use_jetpack((0, 5), screen)
            if game.player_choice.state != "flying":
                game.player_choice.state = "flying"
        # ajustement de la visée
        if game.pressed.get(pygame.K_UP):
            if game.player_choice.bool_equipped:
                # game.player_choice.adjust_aim(1, screen=screen)
                game.player_choice.show_viseur(1, screen=screen)
        elif game.pressed.get(pygame.K_DOWN):
            if game.player_choice.bool_equipped:
                # game.player_choice.adjust_aim(-1, screen=screen)
                game.player_choice.show_viseur(-1, screen=screen)

    # on récupère les évènements au clavier ou a la souris
    """# !! possibilité de remplacer par un case ? pour plus d'optimisation"""
    for event in pygame.event.get():
        # si on ferme la fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # touches de jeu
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # si on est in game
            if game.is_playing:
                # detection des touches du jeu

                if event.key == pygame.K_ESCAPE:  # menue pause
                    menu_number = 2
                    is_playing = False

                elif event.key == pygame.K_RETURN:  # fait spawner un personnage
                    game.start()

                elif event.key == pygame.K_m:  # mort subite
                    game.bool_ms = True

                elif event.key == pygame.K_c:  # changement de personnage
                    game.change_player_choice()

                elif event.key == pygame.K_SPACE:  # touche de tir /saut
                    if game.player_choice is not None:
                        if game.player_choice.bool_equipped:
                            game.player_choice.launch_projectile()
                        # elif game.player_choice.bool_jetpack:
                        #     game.player_choice.jetpack_equip()
                        elif not game.player_choice.bool_jetpack:
                            game.player_choice.jumping = True
                            if game.player_choice.state != "jumping":
                                game.player_choice.state = "jumping"
                                print("jumping")

                elif event.key == pygame.K_x:  # équiper une arme ou la ranger
                    if not game.player_choice.bool_equipped:
                        game.player_choice.equip_weapon(var=True)

                        game.player_choice.show_viseur(0,screen=screen)

                        if game.player_choice.state != "aiming":
                            game.player_choice.state = "aiming"
                            print("aiming")
                    else:
                        game.player_choice.equip_weapon(var=False)

                # jetpack
                elif event.key == pygame.K_j:
                    game.player_choice.jetpack_equip()
                # detection des touches du joueur
                else:
                    game.pressed[event.key] = True
                    # game.player_choice.equip_weapon(False)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # détecter si on clique
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            if menu.settings_rect.collidepoint(event.pos) and menu_number in (0, 2):
                menu.previous_menu_number = menu_number
                menu_number = 1
            elif menu.return_rect.collidepoint(event.pos) and menu_number in (1, 3, 4):
                menu_number = menu.previous_menu_number
            elif menu.credit_rect.collidepoint(event.pos) and menu_number in (0, 2):
                menu.previous_menu_number = menu_number
                menu_number = 4
            elif menu.info_rect.collidepoint(event.pos) and menu_number in (0, 2):
                menu.previous_menu_number = menu_number
                menu_number = 3
            elif menu.play_rect.collidepoint(event.pos) and menu_number in (0, 2):
                is_playing = True
                menu_number = 0
            elif menu.sound_rect.collidepoint(event.pos) and menu_number == 1:
                if DEFAULT.music_level == 0:
                    DEFAULT.music_level = 10
                    pygame.mixer.music.set_volume(10)
                else:
                    DEFAULT.music_level = 0
                    pygame.mixer.music.set_volume(0)

            # fonction de debug pour placer le joueur au clic
            if len(game.all_players.sprites()) != 0 and game.is_playing and DEFAULT.DEBUG:
                game.player_choice.rect.x = event.pos[0]
                game.player_choice.rect.y = event.pos[1]

    # fixer le nb de FPS
    clock.tick(DEFAULT.FPS)