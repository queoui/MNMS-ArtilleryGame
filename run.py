from constants import *
from player import Player
from missile import Missile
from target import Target
from background import Background
from menu import Menu
from timer import Timer

#initialize pygame, display, clock and target sprites
pygame.init()
display = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()
targetSprites = pygame.sprite.Group()
playerSprites = pygame.sprite.Group()


#background music
pygame.mixer.init()
pygame.mixer.music.load(MUSIC_FILE_PATH)
pygame.mixer.music.set_volume(MUSIC_VOLUME_PERCENTAGE)
pygame.mixer.music.play(-1) # -1 to repeat song endlessly


#tank instance
player = Player(400, 300, 75, 75)
player_missile = []

#Add a target sprite with random size
shootingTarget = Target()
targetSprites.add(shootingTarget)

playerSprites.add(player)

#set up background object and skip menu background
game_background = Background(BACKGROUND_IMAGES_FILE_PATHS)
game_background.increment_level_background()

timer = Timer()

menu = Menu()
game_state = None
game_run = True

while game_run:
    if game_state == START_GAME:
        if not timer.is_running():
            timer.start_timer()

        display.blit(game_background.image,game_background.loc)

        #Display the current score of the player
        player.display_score(display)

        #get mouse click position
        mouse_x , mouse_y = pygame.mouse.get_pos()

        #check for events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT

            #bullet clicks    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_missile.append(Missile(player.rect.x, player.rect.y, player))

        #updates player movement
        player.update_player()


        #display tank, bullets and targets
        playerSprites.draw(display)
        targetSprites.draw(display)
        for missile in player_missile:
            missile.display(display, player)
            points = shootingTarget.update(missile, player)
            if points is not None:
                player.update_score(points)
            if len(targetSprites.sprites()) == 0:
                shootingTarget = Target()
                targetSprites.add(shootingTarget)


        timer.update_timer(display)

    elif game_state == LEADER_BOARD:
        print("game state:", game_state)
        game_state = None

    elif game_state == EXIT_GAME:
        game_run = False

    else:
        display.blit(menu.image, menu.rect)
        menu.draw()
        game_state = menu.check_button_click()

        #check for events in game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.QUIT

    clock.tick(60)
    pygame.display.update()
