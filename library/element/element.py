#! /usr/bin/env python3
# coding: utf-8

# """ Module with class Element"""


class Element():
    """docstring for Element : element with
    a position, a path to the corresponding image and a feature"""
    def __init__(self, img, position, feature):
        """create an element with
        img :  path to the image
        postion: tuple (x, y)
        feature:  'player' or 'recoverable' or 'end' """
        self.img = img
        self.position = position
        self.feature = feature

    def find_movement(self, available_positions, direction, size_img):
        """check if movement in a direction is available,
        update the element position and return the movement.
        available_position : list
        direction : str 'left', 'right', 'up', 'down'
        size_img : tuple size in pixel of element image"""

        # set position before the movement
        new_position_x = self.position[0]
        new_position_y = self.position[1]
        movement_x = 0
        movement_y = 0

        # find the diection
        if direction == "left":
            # update position after movement
            new_position_x -= size_img[0]
            movement_x = (-size_img[0])
        elif direction == "right":
            new_position_x += size_img[0]
            movement_x = size_img[0]
        elif direction == "up":
            new_position_y -= size_img[1]
            movement_y = -size_img[1]
        elif direction == "down":
            new_position_y += size_img[1]
            movement_y = size_img[1]

        # check the new position ...
        new_position = (new_position_x, new_position_y)
        if new_position in available_positions:
            # update position
            self.position = new_position
            # return the movement
            return movement_x, movement_y
        else:
            return 0
