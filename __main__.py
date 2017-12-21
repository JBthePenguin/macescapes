#! /usr/bin/env python3
# coding: utf-8

""" Play the game """

import os.path
from random import choice
from time import sleep
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
    path_to_poison = main_dir + "/img/poison.png"

    # set the size of image and window, the position of counter
    size_img = (45, 45)
    size_window = (675, 720)
    counter_position = (365, 675)

    # create the labyrinth, MacGyver and the Bad Guy with start position
    labyrinth = Background(
        path_to_map, path_to_wall,
        path_to_floor, path_to_counter_background, size_img)
    start_point = (45, 45)
    mac = Element(path_to_mac, start_point, "player", size_img)
    bad_guy = Element(path_to_bad_guy, (630, 405), "end", size_img)
    # create the poison : appear in counter when all elements are founded
    poison = Element(path_to_poison, (
        (size_window[0] - size_img[0]), (
            size_window[1] - size_img[1])), "", size_img)
    # remove the positions of mac and bad_boy as avalaible position
    labyrinth.available_positions.remove(mac.position)
    labyrinth.available_positions.remove(bad_guy.position)

    # random choice for position and create the 3 other elements
    needle = Element(
        path_to_needle, choice(labyrinth.available_positions),
        "recoverable", size_img)
    labyrinth.available_positions.remove(needle.position)
    tube = Element(
        path_to_tube, choice(labyrinth.available_positions),
        "recoverable", size_img)
    labyrinth.available_positions.remove(tube.position)
    ether = Element(
        path_to_ether, choice(labyrinth.available_positions),
        "recoverable", size_img)
    labyrinth.available_positions.remove(ether.position)

    # create a list of game's elements except the player and the poison
    game_elements = [bad_guy, needle, tube, ether]

    # initialise available positions of the labyrinth
    labyrinth.__init__(
        path_to_map, path_to_wall,
        path_to_floor, path_to_counter_background, size_img)

    # !!!!! OPEN the gui and play the game!!!!!
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
    mac.img = pygame.image.load(mac.img).convert_alpha()
    mac_rect = mac.img.get_rect(topleft=start_point)

    # create object Surface for poison
    poison.img = pygame.image.load(poison.img).convert_alpha()

    # create object Surface for each other element
    for element in game_elements:
        element.img = pygame.image.load(element.img).convert_alpha()

    # initialize and create object Front for the counter:
    elements_recovered = 0
    count_font = pygame.font.SysFont('Comic Sans MS', 30)

    # keep the window open ...
    gui_display = 1
    while gui_display:
        for event in pygame.event.get():
            if event.type == QUIT:  # if window is closed
                gui_display = 0
            elif event.type == KEYDOWN:  # if the keyboard is used
                movement = 0
                # find the direction
                if event.key == K_LEFT:
                    # test the movement
                    movement = mac.check_movement(
                        labyrinth.available_positions, "left")
                elif event.key == K_RIGHT:
                    movement = mac.check_movement(
                        labyrinth.available_positions, "right")
                elif event.key == K_UP:
                    movement = mac.check_movement(
                        labyrinth.available_positions, "up")
                elif event.key == K_DOWN:
                    movement = mac.check_movement(
                        labyrinth.available_positions, "down")
                if movement != 0:
                    # move the player
                    mac_rect = mac_rect.move(movement)
                    # check the new position of player with other elements
                    element_founded = mac.check_position(
                        game_elements, elements_recovered,
                        counter_position)
                    if element_founded != 0:
                        if element_founded.feature == "recoverable":
                            elements_recovered += 1
                            if elements_recovered == 3:
                                # put poison if all elements are recovered
                                game_elements.append(poison)
                        elif element_founded.feature == "end":
                            # the player arrive on end point
                            if elements_recovered == 3:
                                # WIN
                                game_elements = []
                                elements_recovered = "escapes!!!"
                            else:
                                # LOSE
                                game_elements = [bad_guy]
                                elements_recovered = "stays in prison!!!"
                                mac_rect = mac.img.get_rect(
                                    topleft=start_point)
        # paste all on the window and refresh it
        for key in labyrinth:
            window.blit(labyrinth[key], key)
        for element in game_elements:
            window.blit(element.img, element.position)
        counter = count_font.render(
            str(elements_recovered), False, (247, 9, 9))
        window.blit(counter, counter_position)
        window.blit(mac.img, mac_rect)
        # refresh window
        pygame.display.flip()
        if (elements_recovered == "escapes!!!") or (
                elements_recovered == "stays in prison!!!"):
            # close window if player on end point
            gui_display = 0
            sleep(2)


if __name__ == "__main__":
    main()
