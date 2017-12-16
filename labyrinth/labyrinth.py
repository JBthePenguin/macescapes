#! /usr/bin/env python3
# coding: utf-8

""" Module with class Labyrinth"""
import os.path
main_dir = os.path.dirname(os.path.dirname(__file__))


class Labyrinth(dict):
    """docstring for Labyrinth : Class
    object = {position xy : path towards the corresponding img}"""

    def __init__(self):
        """create a labyrinth"""
        # get the right path
        path_to_file = os.path.join(
            main_dir, "maps", "default_map.txt")
        # open the file
        with open(path_to_file, "r") as f:
            # Initialize the position
            x = 0
            y = 0
            # read character by character
            for elt in f.read():
                if elt == "\n":
                    # update position
                    x = 0
                    y += 1
                else:
                    if elt == "O":
                        path_to_img = os.path.join(
                            main_dir, "img", "wall.png")
                    else:
                        path_to_img = os.path.join(
                            main_dir, "img", "floor.png")
                    # add key (x,y) and value (path to the file) in background
                    self[(x, y)] = path_to_img
                    # update position
                    x += 1
