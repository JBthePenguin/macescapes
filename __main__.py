#! /usr/bin/env python3
# coding: utf-8

import os.path
from random import choice
import pygame.display
import pygame.image
import pygame.event
import pygame.font
from pygame.locals import *
from library.background.background import Background
from library.element.element import Element
import library.game_function.game_function as game_function


def main():
    """ create the background, the player and the other elements
    before running the game"""

    # find the path to default_map.txt, and all images for :
    # images for background and the counter background
    # all elements : mac, bad_guy, needle tube, ether
    main_dir = os.path.dirname(__file__)
    path_to_map = os.path.join(main_dir, "maps", "default_map.txt")
    path_to_counter_background = os.path.join(main_dir, "img", "counter.png")
    path_to_wall = os.path.join(main_dir, "img", "wall.png")
    path_to_floor = os.path.join(main_dir, "img", "floor.png")
    path_to_mac = os.path.join(main_dir, "img", "mac.png")
    path_to_bad_guy = os.path.join(main_dir, "img", "bad_guy.png")
    path_to_needle = os.path.join(main_dir, "img", "needle.png")
    path_to_tube = os.path.join(main_dir, "img", "tube.png")
    path_to_ether = os.path.join(main_dir, "img", "ether.png")

    # set the size of image and window
    size_img = (45, 45)
    size_window = (675, 720)

    # create the labyrinth, MacGyver and the Bad Guy with start position
    labyrinth = Background(
        path_to_map, path_to_wall,
        path_to_floor, size_img, path_to_counter_background)
    mac = Element(path_to_mac, (45, 45))
    bad_guy = Element(path_to_bad_guy, (630, 405))

    # remove the positions of mac and bad_boy as avalaible position
    labyrinth.available_positions.remove(mac.position)
    labyrinth.available_positions.remove(bad_guy.position)

    # random choice for position of the 3 other elements
    needle = Element(path_to_needle, choice(labyrinth.available_positions))
    labyrinth.available_positions.remove(needle.position)
    tube = Element(path_to_tube, choice(labyrinth.available_positions))
    labyrinth.available_positions.remove(tube.position)
    ether = Element(path_to_ether, choice(labyrinth.available_positions))
    labyrinth.available_positions.remove(ether.position)

    # create a list of objects and initialise avalaible position
    objects = [needle, tube, ether]
    labyrinth.__init__(
        path_to_map, path_to_wall,
        path_to_floor, size_img, path_to_counter_background)

    # !!!!! OPEN the gui !!!!!
    pygame.init()
    window = pygame.display.set_mode(size_window)

    # create object Surface for each zone of background
    for key in labyrinth:
        img = pygame.image.load(labyrinth[key]).convert_alpha()
        labyrinth[key] = img

    # create an object Rect for the player
    player = pygame.image.load(mac.img).convert_alpha()
    player_position = player.get_rect(topleft=mac.position)

    # create object Surface bad_guy and for each object
    end_point = pygame.image.load(bad_guy.img).convert_alpha()
    for obj in objects:
            obj.img = pygame.image.load(obj.img).convert_alpha()

    # create a the counter of objects recovered:
    objects_recovered = 0
    count_font = pygame.font.SysFont('Comic Sans MS', 50)

    # moving when the key reaims depressed
    pygame.key.set_repeat(400, 30)

    # keep the window open ...
    gui_display = 1
    while gui_display:
        for event in pygame.event.get():
            if event.type == QUIT:  # close window
                gui_display = 0

            elif event.type == KEYDOWN:  # find the direction
                if event.key == K_LEFT:
                    direction = "left"
                elif event.key == K_RIGHT:
                    direction = "right"
                elif event.key == K_UP:
                    direction = "up"
                elif event.key == K_DOWN:
                    direction = "down"

                # move the player in the correct direction
                player_position = game_function.move_player(
                    player_position, labyrinth.available_positions,
                    direction, size_img)

                # check the position with objects and update it
                objects, objects_recovered = game_function.check_position(
                    player_position, objects, objects_recovered,
                    size_img, size_window)
                gui_display = game_function.check_win(
                    player_position, bad_guy.position)

        # display on gui
        # paste all on the window and refresh it
        # background
        for key in labyrinth:
            window.blit(labyrinth[key], key)
        # objects
        for obj in objects:
            window.blit(obj.img, obj.position)
        # counter
        counter = count_font.render(
            str(objects_recovered), False, (247, 9, 9))
        window.blit(counter, (375, 682))
        # finish point
        window.blit(end_point, bad_guy.position)
        # player
        window.blit(player, player_position)
        # refresh window
        pygame.display.flip()


if __name__ == "__main__":
    main()
