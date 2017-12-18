#! /usr/bin/env python3
# coding: utf-8

import os.path as path

""" Module with class Labyrinth"""

main_dir = path.dirname(
    path.dirname(
        path.dirname(__file__)))


class Labyrinth(dict):
    """docstring for Labyrinth : Class object =
    {position xy : path towards the corresponding img}"""
    def __init__(self, size_img):
        """create a labyrinth with florr and wall"""
        # get the right path to the map's file and open it
        path_to_file = path.join(
            main_dir, "maps", "default_map.txt")
        with open(path_to_file, "r") as f:
            # Initialize position
            x = 0
            y = 0
            # read character by character
            for elt in f.read():
                if elt == "\n":
                    # update next position
                    x = 0
                    y += size_img[1]
                else:
                    # get the right path to image
                    if elt == "O":
                        path_to_img = path.join(
                            main_dir, "img", "wall.png")
                    else:
                        path_to_img = path.join(
                            main_dir, "img", "floor.png")
                    # add key (x,y) and value (path to the file) in background
                    self[(x, y)] = path_to_img
                    # update position
                    x += size_img[0]
