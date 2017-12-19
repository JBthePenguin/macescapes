#! /usr/bin/env python3
# coding: utf-8

""" Module with class Labyrinth"""


class Background(dict):
    """docstring for Background : background with wall, floor
    a background for the counter and a list of available positions"""

    def __init__(self, map, wall, floor, counter_background, size_img):
        """create a background with the path of:
        map : path to file .txt
        wall: path to image .png
        floor : path to image .png
        counter_img : path to background of counter"""

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
