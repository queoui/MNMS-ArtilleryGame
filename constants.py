import os
import pygame
import sys
import random

DISPLAY_SIZE = (800, 600)
TIMER_SECONDS = 100

MUSIC_VOLUME_PERCENTAGE = .03
MUSIC_FILE_PATH = 'resources/Disco_Heavy.mp3'


MAIN_DIR = os.path.dirname(__file__)
IMAGES_DIR = os.path.join(MAIN_DIR, "resources/images")
TANKS_DIR = os.path.join(MAIN_DIR, "resources/images/tanks")

TARGET_IMAGE = os.path.join(IMAGES_DIR, "target.png")
TANK_LEFT = os.path.join(TANKS_DIR, "tank_left.png")
TANK_UP =os.path.join(TANKS_DIR, "tank_up.png")
TANK_RIGHT = os.path.join(TANKS_DIR, "tank_right.png")
TANK_DOWN = os.path.join(TANKS_DIR, "tank_down.png")

#static variable holding the list of background image file paths
#with the first being the main menu image and the rest being the images for the
#levels in ascending order.
MENU_BACKGROUND = os.path.join(IMAGES_DIR, 'Menu-Background-Resized.jpg')
HEX_BACKGROUND = os.path.join(IMAGES_DIR, 'Hex-Background-Resized.jpg')
BACKGROUND_IMAGES_FILE_PATHS = [MENU_BACKGROUND, HEX_BACKGROUND]

RED_VIOLET = (202, 22, 142)
CLAIRVOYANT = (100, 14, 110)

START_GAME = "Start Game"
LEADER_BOARD = "Leader Board"
EXIT_GAME = "Exit Game"