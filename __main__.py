#! /usr/bin/env python3
# coding: utf-8

# from labyrinth.labyrinth import Labyrinth
# from element.element import Element
# from game import game
from random import choice

from library.labyrinth.labyrinth import Labyrinth

from library.element.element import Element

import library.game_function.game_function as game_function


def main():
    """ create the background, the player and the other elements
    before running the game"""
    # set the size of one image in pixels
    size_img = (40, 40)
    # create the labyrinth and make a list of availabe position
    background = Labyrinth(size_img)
    available_positions = game_function.create_available_positions(background)
    # create MacGyver and the enemy and set the start position
    mac = Element("mac", (40, 40))
    bad_boy = Element("bad_boy", (560, 360))
    # remove the positions of mac and bad_boy in the list
    available_positions.remove(mac.position)
    available_positions.remove(bad_boy.position)
    # random choice for position of the 3 other elements
    needle = Element("needle", choice(available_positions))
    available_positions.remove(needle.position)
    tube = Element("tube", choice(available_positions))
    available_positions.remove(tube.position)
    ether = Element("ether", choice(available_positions))
    available_positions.remove(ether.position)
    # create of list of the elements of the game
    objects = [needle, tube, ether]
    # launch the game
    game_function.play_game(background, mac, bad_boy, objects, size_img)


if __name__ == "__main__":
    main()
