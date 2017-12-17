#! /usr/bin/env python3
# coding: utf-8

import os.path as path

""" Module with class Element"""

main_dir = path.dirname(
    path.dirname(
        path.dirname(__file__)))


class Element():
    """docstring for Element : Class object with 2 atrributes:
    position xy and path to the corresponding image of type"""
    def __init__(self, type_name, position):
        """create an element with 2 parameters:
        type of the element and the starting position"""
        self.position = position
        img = type_name + ".png"
        self.path_to_img = path.join(main_dir, "img", img)
