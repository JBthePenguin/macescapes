#! /usr/bin/env python3
# coding: utf-8

""" imports all necessary modules, get all paths to images,
set default size image and start/end positions
and launch the game : main() """

# pylint: disable=no-name-in-module

# import from standard modules
from os.path import dirname as path_dirname
from random import choice
from time import sleep
# import from third party module : pygame
from pygame import init as pg_init
from pygame.display import set_mode as pg_set_mode
from pygame.key import set_repeat as pg_set_repeat
from pygame.display import flip as pg_flip
from pygame.image import load as pg_load
from pygame.event import get as pg_get
from pygame.font import SysFont as pg_SysFont
from pygame.locals import QUIT, KEYDOWN
# import from local modules
from library.background.background import Background
from library.element.element import Element
from library.play_game.play_game import play_game

# find the path to default_map.txt, and all images for :
# background and the counter background
# all elements : mac, bad_guy, needle tube, ether
MAIN_DIR = path_dirname(__file__)
PATH_TO_MAP = MAIN_DIR + "/maps/default_map.txt"
PATH_TO_COUNTER_BG = MAIN_DIR + "/img/counter.png"
PATH_TO_WALL = MAIN_DIR + "/img/wall.png"
PATH_TO_FLOOR = MAIN_DIR + "/img/floor.png"
PATH_TO_MAC = MAIN_DIR + "/img/mac.png"
PATH_TO_BAD_GUY = MAIN_DIR + "/img/bad_guy.png"
PATH_TO_NEEDLE = MAIN_DIR + "/img/needle.png"
PATH_TO_TUBE = MAIN_DIR + "/img/tube.png"
PATH_TO_ETHER = MAIN_DIR + "/img/ether.png"
PATH_TO_POISON = MAIN_DIR + "/img/poison.png"

# set the size of image, start and end points
SIZE_IMG = (45, 45)
START_POINT = (45, 45)
END_POINT = (630, 405)


def main():
    """ create all the variables before run the gui
    and play the game with module pygame"""

    # !! create all the variables necessary for the game !!
    # create the labyrinth, MacGyver and the Bad Guy with default positions
    labyrinth = Background(
        PATH_TO_MAP, PATH_TO_WALL, PATH_TO_FLOOR, SIZE_IMG)
    mac = Element(PATH_TO_MAC, START_POINT, "player", SIZE_IMG)
    bad_guy = Element(PATH_TO_BAD_GUY, END_POINT, "end", SIZE_IMG)
    # remove the positions of mac and bad_guy in avalaible positions
    labyrinth.available_positions.remove(mac.position)
    labyrinth.available_positions.remove(bad_guy.position)
    # random choice for position and create the 3 other elements
    needle = Element(
        PATH_TO_NEEDLE, choice(labyrinth.available_positions),
        "recoverable", SIZE_IMG)
    labyrinth.available_positions.remove(needle.position)
    tube = Element(
        PATH_TO_TUBE, choice(labyrinth.available_positions),
        "recoverable", SIZE_IMG)
    labyrinth.available_positions.remove(tube.position)
    ether = Element(
        PATH_TO_ETHER, choice(labyrinth.available_positions),
        "recoverable", SIZE_IMG)
    labyrinth.available_positions.remove(ether.position)
    # create the poison : appear in counter when all elements are founded
    poison = Element(PATH_TO_POISON, (
        (labyrinth.size_window[0] - SIZE_IMG[0]), (
            labyrinth.size_window[1] - SIZE_IMG[1])), "", SIZE_IMG)
    # create a list of game's elements
    game_elements = [mac, bad_guy, needle, tube, ether, poison]
    # initialise available positions of the labyrinth
    labyrinth.__init__(PATH_TO_MAP, PATH_TO_WALL, PATH_TO_FLOOR, SIZE_IMG)
    # add the background for counter
    labyrinth[(0, labyrinth.counter_position[1])] = PATH_TO_COUNTER_BG
    # !! create the gui !!
    # create a window
    pg_init()
    window = pg_set_mode(labyrinth.size_window)
    # set moving when the key reaims depressed
    pg_set_repeat(400, 30)
    # create object Surface for each zone of background
    for key in labyrinth:
        labyrinth[key] = pg_load(labyrinth[key]).convert_alpha()
    # create object Surface for each element
    for element in game_elements:
        element.img = pg_load(element.img).convert_alpha()
    # create an object Rect for the player
    mac_rect = mac.img.get_rect(topleft=START_POINT)
    # !! play the game !!
    # initialize the counter and the list of elements:
    game_elements.remove(mac)
    game_elements.remove(poison)
    counter_elts_founded = 0
    # keep the window open ...
    gui_display = 1
    while gui_display:
        for event in pg_get():
            if event.type == QUIT:  # if window is closed
                gui_display = 0
            elif event.type == KEYDOWN:  # if the keyboard is used
                mac, mac_rect, game_elements, counter_elts_founded = play_game(
                    event, mac, mac_rect, game_elements, counter_elts_founded,
                    labyrinth)
                if counter_elts_founded == 3:
                    # put poison if all elements are recovered
                    game_elements.append(poison)
                # put the player at start position if he lose
                elif counter_elts_founded == "stays in prison!!!":
                    mac_rect = mac.img.get_rect(topleft=START_POINT)
        # paste all on the window
        # background
        for key in labyrinth:
            window.blit(labyrinth[key], key)
        # game's elements
        for element in game_elements:
            window.blit(element.img, element.position)
        # counter
        window.blit(pg_SysFont('Comic Sans MS', 30).render(
            str(counter_elts_founded), False, (
                247, 9, 9)), labyrinth.counter_position)
        # player
        window.blit(mac.img, mac_rect)
        # refresh window
        pg_flip()
        if counter_elts_founded.__class__ is "".__class__:
            # close window if player on end point
            gui_display = 0
            sleep(2)


if __name__ == "__main__":
    main()
