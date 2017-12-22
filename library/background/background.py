#! /usr/bin/env python3
# coding: utf-8

""" Module with class Labyrinth"""


class Background(dict):
    """game's background with wall, floor, a background for a counter
    and a list of available positions"""

    def __init__(self, map_file, wall, floor, counter_background, size_img):
        """create a background with
        map_file : str 'path/to/file.txt'
        wall: str 'path/to/image'
        floor : str 'path/to/image'
        counter_background : str 'path/to/image'
        size_img : tuple (x, y)"""

        # initialize a list of available positions
        self.available_positions = []
        # read the .txt with the background
        with open(map_file, "r") as background:
            # Initialize position
            position_x = 0
            position_y = 0
            # read character by character
            for elt in background.read():
                if elt == "\n":
                    # update next position
                    position_x = 0
                    position_y += size_img[1]
                else:
                    # get corresponding image
                    if elt == "O":
                        img = wall
                    else:
                        img = floor
                        # update available positions
                        self.available_positions.append(
                            (position_x, position_y))
                    # add key (x,y) and value img in background
                    self[(position_x, position_y)] = img
                    # update position
                    position_x += size_img[0]
        # add background for the counter:
        self[(0, (position_y + size_img[1]))] = counter_background
