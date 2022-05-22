import pygame
DEBUG = True

# paramètres de la fenêtre
window_name = "projet transverse"
window_icon = "assets/logo_efrei.png"
window_width = 1300
FPS = 60

# images décors
path_terrain = "assets/terrains/terrain_island_1.png"
path_background = "assets/backgrounds/background_sky_1.png"
path_sea = "assets/backgrounds/sea.png"
path_title = "assets/affichages/title.png"
path_credits = "assets/affichages/credits.png"
path_gameover = "assets/affichages/gameover.png"
path_bluewins = "assets/affichages/bluewins.png"
path_redwins = "assets/affichages/redwins.png"


# images boutons
path_settings = "assets/UI/gear.png"
path_return = "assets/UI/return.png"
path_play = "assets/UI/right.png"
path_credit = "assets/UI/medal2.png"
path_info = "assets/UI/question.png"
path_sound_on = "assets/UI/musicOn.png"
path_sound_off = "assets/UI/musicOff.png"
path_quit_game = "assets/UI/home.png"

# images armes
pygame.transform.scale(pygame.image.load("assets/weapons/shuriken.png"), (100, 100))
path_shuriken = "assets/weapons/shuriken.png"
image_explo = pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/explosion.png"), (100, 100))
image_explo1 = pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/explosion1.png"), (100, 100))
image_explo2 = pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/explosion2.png"), (100, 100))
image_explo3 = pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/explosion3.png"), (100, 100))

tab_explo = [image_explo, image_explo1, image_explo2, image_explo3,
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 1.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 2.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 3.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 4.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 5.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 6.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 7.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 8.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 9.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 10.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 11.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 12.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 13.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 14.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 15.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 16.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 17.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 18.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 19.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 20.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 21.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 22.png"), (100, 100)),
             pygame.transform.scale(pygame.image.load("assets/weapons/ExplosionV2/Calque 23.png"), (100, 100)),
             ]

# son
path_music = "assets/sounds/music_theme_1.wav"
music_level = 0  # 10 pour activer, 0 pour couper

# player
players_velocity = 3
path_player_indicator = "assets/ui/arrowDown.png"
player_per_team = 3

path_player = "assets/player/player.png"
path_player_fall = "assets/player/player_fall.png"
path_player_bazooka = "assets/player/player_bazooka.png"
path_player_jetpack = "assets/player/player_jetpack.png"
path_player_jump = "assets/player/player_jump.png"
path_player_gravestone = "assets/player/player_gravestone.png"

# miscellaneous
path_arrow = "assets/weapons/Rond_rouge.png"
path_bouton_gameover = "assets/UI/home.png"

# équipes
teams_name = ("bleu", "rouge")
path_player_img_bleu = ["assets/player/knight_bleu.png", "assets/player/knight_bleu2.png"]
path_player_img_vert = ["assets/player/knight_vert.png", "assets/player/knight_vert2.png"]
path_player_img_tab = [path_player_img_bleu, path_player_img_vert]
# paramètre de la mer
sea_level = 100
