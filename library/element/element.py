#! /usr/bin/env python3
# coding: utf-8

# """ Module with class Element"""


class Element():
    """docstring for Element : Class object with 2 atrributes:
    position xy and path to the corresponding image of type"""
    def __init__(self, img, position):
        """create an element with postion and path to the image"""
        self.position = position
        self.img = img
