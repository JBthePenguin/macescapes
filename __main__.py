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


def main():
    """ create the background, the player and the other elements
    before, run the gui and play the game """

    # find the path to default_map.txt, and all images for :
    # background and the counter background
    # all elements : mac, bad_guy, needle tube, ether
    main_dir = os.path.dirname(__file__)
    path_to_map = main_dir + "/maps/default_map.txt"
    path_to_counter_background = main_dir + "/img/counter.png"
    path_to_wall = main_dir + "/img/wall.png"
    path_to_floor = main_dir + "/img/floor.png"
    path_to_mac = main_dir + "/img/mac.png"
    path_to_bad_guy = main_dir + "/img/bad_guy.png"
    path_to_needle = main_dir + "/img/needle.png"
    path_to_tube = main_dir + "/img/tube.png"
    path_to_ether = main_dir + "/img/ether.png"

    # set the size of image and window
    size_img = (45, 45)
    size_window = (675, 720)

    # create the labyrinth, MacGyver and the Bad Guy with start position
    labyrinth = Background(
        path_to_map, path_to_wall,
        path_to_floor, size_img, path_to_counter_background)
    mac = Element(path_to_mac, (45, 45), "player")
    bad_guy = Element(path_to_bad_guy, (630, 405), "end")

    # remove the positions of mac and bad_boy as avalaible position
    labyrinth.available_positions.remove(mac.position)
    labyrinth.available_positions.remove(bad_guy.position)

    # random choice for position and create the 3 other elements
    needle = Element(
        path_to_needle, choice(labyrinth.available_positions),
        "recoverable")
    labyrinth.available_positions.remove(needle.position)
    tube = Element(
        path_to_tube, choice(labyrinth.available_positions),
        "recoverable")
    labyrinth.available_positions.remove(tube.position)
    ether = Element(
        path_to_ether, choice(labyrinth.available_positions),
        "recoverable")
    labyrinth.available_positions.remove(ether.position)

    # create a list of game's elements except the player
    game_elements = [bad_guy, needle, tube, ether]

    # initialise available positions of the labyrinth
    labyrinth.__init__(
        path_to_map, path_to_wall,
        path_to_floor, size_img, path_to_counter_background)

    # !!!!! OPEN the gui !!!!!
    # create a window
    pygame.init()
    window = pygame.display.set_mode(size_window)
    # moving when the key reaims depressed
    pygame.key.set_repeat(400, 30)

    # create object Surface for each zone of background
    for key in labyrinth:
        img = pygame.image.load(labyrinth[key]).convert_alpha()
        labyrinth[key] = img

    # create an object Rect for the player
    mac_img = pygame.image.load(mac.img).convert_alpha()
    mac_rect = mac_img.get_rect(topleft=mac.position)

    # create object Surface for each other element
    for element in game_elements:
        element.img = pygame.image.load(element.img).convert_alpha()

    # initialize and create object Front for the counter:
    elements_recovered = 0
    count_font = pygame.font.SysFont('Comic Sans MS', 40)

    # keep the window open ...
    gui_display = 1
    while gui_display:
        for event in pygame.event.get():
            if event.type == QUIT:  # if window is closed
                gui_display = 0
            elif event.type == KEYDOWN:  # if the keyboard is used
                # find the direction
                if event.key == K_LEFT:
                    direction = "left"
                elif event.key == K_RIGHT:
                    direction = "right"
                elif event.key == K_UP:
                    direction = "up"
                elif event.key == K_DOWN:
                    direction = "down"
                # check if the movement is possible
                movement = mac.find_movement(
                    labyrinth.available_positions, direction, size_img)
                if movement != 0:
                    # move the player
                    mac_rect = mac_rect.move(movement)
                    # check the new position of player with other elements
                    for element in game_elements:
                        if (mac.position[0] == element.position[0]) and (
                                mac.position[1] == element.position[1]):
                            # check the type of element
                            if element.feature == "recoverable":
                                # update the counter
                                elements_recovered += 1
                                # put element in the background counter
                                x = size_window[0] - (
                                    size_img[0] * elements_recovered * 1.5)
                                y = size_window[1] - size_img[1]
                                element.position = (x, y)
                            else:
                                gui_display = 0  # !!!! WIN!!!
        # display on gui
        # paste all on the window and refresh it
        for key in labyrinth:
            window.blit(labyrinth[key], key)
        for element in game_elements:
            window.blit(element.img, element.position)
        counter = count_font.render(
            str(elements_recovered), False, (247, 9, 9))
        window.blit(counter, (375, 668))
        window.blit(mac_img, mac_rect)
        # refresh window
        pygame.display.flip()


if __name__ == "__main__":
    main()
