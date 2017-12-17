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
    # create the labyrinth and make a list of availabe position
    background = Labyrinth()
    available_positions = game_function.create_list(background)
    # create the player (mac) and the end of the game (bad_boy)
    mac = Element("mac", (1, 1))
    bad_boy = Element("bad_boy", (14, 9))
    # create a new list before placing other elements
    new_list = available_positions
    # remove the positions of mac and bad_boy in the new list
    new_list.remove(mac.position)
    new_list.remove(bad_boy.position)
    # random choice for position of the 3 other elements
    needle = Element("needle", choice(available_positions))
    new_list.remove(needle.position)
    tube = Element("tube", choice(available_positions))
    new_list.remove(tube.position)
    ether = Element("ether", choice(available_positions))
    new_list.remove(ether.position)
    # create of list of the elements of the game
    elements = [bad_boy, needle, tube, ether]
    # launch the game
    game_function.launch(background, mac, elements, available_positions)


if __name__ == "__main__":
    main()
