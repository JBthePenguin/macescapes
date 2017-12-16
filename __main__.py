#! /usr/bin/env python3
# coding: utf-8

# from modules.labyrinth import Labyrinth
# from modules import labyrinth
# import local_modules.labyrinth as labyrinth
from labyrinth.labyrinth import Labyrinth
from element.element import Element
from game import game
from random import choice


def main():
    """ create the background and the elements of gaming"""
    background = Labyrinth()
    # make a list of availabe position
    list_available_positions = []
    for position in background:
        if "floor" in background[position]:
            list_available_positions.append(position)
    # set starting position for each element
    mac = Element("mac", (1, 1))
    bad_boy = Element("bad_boy", (14, 9))
    # update the liste
    list_available_positions.remove(mac.position)
    list_available_positions.remove(bad_boy.position)
    # random choice for other elements
    needle = Element("needle", choice(list_available_positions))
    list_available_positions.remove(needle.position)
    tube = Element("tube", choice(list_available_positions))
    list_available_positions.remove(tube.position)
    ether = Element("ether", choice(list_available_positions))
    list_available_positions.remove(ether.position)
    elements = {mac, bad_boy, needle, tube, ether}
    game.display(background, elements)


if __name__ == "__main__":
    main()
