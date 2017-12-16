#! /usr/bin/env python3
# coding: utf-8

""" Module with function display"""
import pygame.display
import pygame.image
import pygame.event
from pygame.locals import QUIT


def display(background, elements):
    """ display the game on a gui """
    pygame.init()
    window = pygame.display.set_mode((600, 600))
    # BACKGROUND
    x = 0
    y = 0
    while y < 15:
        img = pygame.image.load(background[(x, y)]).convert()
        window.blit(img, ((x * 40), (y * 40)))
        if x < 14:
            x += 1
        else:
            x = 0
            y += 1
    # ELEMENTS
    for elt in elements:
        img = pygame.image.load(elt.path_to_img).convert_alpha()
        x = elt.position[0]
        y = elt.position[1]
        window.blit(img, ((x * 40), (y * 40)))
    # refresh the display
    pygame.display.flip()
    # keep the display on ...
    gui_display = 1
    while gui_display:
        for event in pygame.event.get():
            # ... unless the window is closed
            if event.type == QUIT:
                gui_display = None
