#! /usr/bin/env python3
# coding: utf-8

""" Module with class Labyrinth"""


class Background(dict):
    """docstring for Background : background with wall, floor
    a background for a counter and a list of available positions"""

    def __init__(self, map, wall, floor, size_img, counter_background):
        """create a background with the path to:
        map : file .txt
        wall: image .png
        floor : image .png
        size_img : size of one image in pixel (x, y)
        counter_background : image .png
        """

        # initialize a property : list of available positions
        self.available_positions = []

        # read the .txt with the background
        with open(map, "r") as f:
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
                    # get corresponding image
                    if elt == "O":
                        img = wall
                    else:
                        img = floor
                        # update available positions
                        self.available_positions.append((x, y))
                    # add key (x,y) and value img in background
                    self[(x, y)] = img
                    # update position
                    x += size_img[0]

        # add background for the counter:
        self[(0, (y + size_img[1]))] = counter_background
