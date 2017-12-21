#! /usr/bin/env python3
# coding: utf-8

""" Module with class Element"""


class Element():
    """docstring for Element : element with
    a position, a path to the corresponding image and a feature"""

    def __init__(self, img, position, feature, size_img):
        """create an element with
        img :  path to the image
        position: tuple (x, y)
        feature:  'player' or 'recoverable' or 'end'
        size_img : tuple (x, y)"""
        self.img = img
        self.position = position
        self.feature = feature
        self.size_img = size_img

    def check_movement(self, available_positions, direction):
        """check if movement in a direction is available,
        update the element position and return the movement.
        available_position : list
        direction : str 'left', 'right', 'up', 'down'"""
        # set position before the movement
        new_position_x = self.position[0]
        new_position_y = self.position[1]
        movement_x = 0
        movement_y = 0
        # find the diection
        if direction == "left":
            # update position after movement
            new_position_x -= self.size_img[0]
            movement_x = (-self.size_img[0])
        elif direction == "right":
            new_position_x += self.size_img[0]
            movement_x = self.size_img[0]
        elif direction == "up":
            new_position_y -= self.size_img[1]
            movement_y = -self.size_img[1]
        elif direction == "down":
            new_position_y += self.size_img[1]
            movement_y = self.size_img[1]
        # check the new position ...
        new_position = (new_position_x, new_position_y)
        if new_position in available_positions:
            # update position
            self.position = new_position
            # return the movement
            return movement_x, movement_y
        else:
            return 0

    def check_position(self, elements, elements_recovered, counter_position):
        """check if an element (self) is in the same position of an
        other element, update the number of elements recovered if is
        an recoverable element and put it in the counter before return it.
        elements : list of game's elements except self
        elements_recovered : int
        counter_position : tuple (x, y)"""
        # check the new position of player with other elements
        for element in elements:
            if (self.position[0] == element.position[0]) and (
                    self.position[1] == element.position[1]):
                # check the type of element
                if element.feature == "recoverable":
                    # put element in the background counter
                    x = counter_position[0] + self.size_img[0] + (
                        1.5 * elements_recovered * self.size_img[0])
                    y = counter_position[1]
                    element.position = (x, y)
                return element
        return 0
