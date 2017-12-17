#! /usr/bin/env python3
# coding: utf-8

import os.path as path
""" Module with class Element"""
main_dir = path.dirname(
    path.dirname(
        path.dirname(__file__)))


class Element():
    """Object a type"""
    def __init__(self, type_name, position):
        """create an element with a position and a path to image"""
        self.position = position
        img = type_name + ".png"
        self.path_to_img = path.join(main_dir, "img", img)
