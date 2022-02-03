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

# spawn 2 joueur pour éviter les bugs de touches
game.spawn_player()
game.spawn_player()

# boucle principale du jeu
running = True
j = 0
is_playing = False
menu_number = 0
while running:
    # verif de la mort subite
    if game.bool_ms:
        game.sea_level += 1

    if is_playing :
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
                if game.player_choice != None:
                    if game.player_choice.bool_equiped:
                        print("tir")
                        game.player_choice.launch_projectile()
                    else:
                        game.player_choice.jump(screen)
            # équiper une arme ou la ranger
            elif event.key == pygame.K_x:
                print("A")
                if game.player_choice.bool_equiped == False:
                    game.player_choice.equip_weapon(True)
                else: game.player_choice.equip_weapon(False)

            # detection des touches du joueur
            else:
                game.pressed[event.key] = True
                #game.player_choice.equip_weapon(False)


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        # detecter si on clique
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu.settings_rect.collidepoint(event.pos):
                menu_number = 1
            if menu.return_rect.collidepoint(event.pos):
                menu_number = 0
            if menu.play_rect.collidepoint(event.pos):
                is_playing = True
                menu_number = 0



    # fixer le nb de FPS
    clock.tick(DEFAULT.FPS)