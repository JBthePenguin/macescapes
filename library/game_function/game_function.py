#! /usr/bin/env python3
# coding: utf-8

""" Module with the functions of the game"""

import pygame.display

import pygame.image

import pygame.event

from pygame.locals import *


def create_list(background):
    """ create a list of available positions"""
    available_positions = []
    for position in background:
        if "floor" in background[position]:
            available_positions.append(position)
    return available_positions


def paste_background(window, background):
    """ paste the background on the window
    with the corresponding image for each position"""
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


def paste_elements(window, elements):
    """ paste the differents elements on the window
    with the corresponding image"""
    for element in elements:
        img = pygame.image.load(element.path_to_img).convert_alpha()
        x = element.position[0] * 40
        y = element.position[1] * 40
        window.blit(img, (x, y))


def launch(background, movable_elt, elements, available_positions):
    """launch the game on  gui """
    # create a window
    pygame.init()
    window = pygame.display.set_mode((600, 600))
    # create an object Rect for the player
    player = pygame.image.load(movable_elt.path_to_img).convert_alpha()
    player_position = player.get_rect(topleft=(40, 40))
    # moving when the key reaims depressed
    pygame.key.set_repeat(400, 30)
    # keep the window open ...
    gui_display = 1
    while gui_display:
        for event in pygame.event.get():
            # ... unless the window is closed
            if event.type == QUIT:
                gui_display = 0
            # move the player in the correct direction
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    player_position = player_position.move(-40, 0)
                elif event.key == K_RIGHT:
                    player_position = player_position.move(40, 0)
                elif event.key == K_UP:
                    player_position = player_position.move(0, -40)
                elif event.key == K_DOWN:
                    player_position = player_position.move(0, 40)
        # paste all on the window and refresh it
        paste_background(window, background)
        paste_elements(window, elements)
        window.blit(player, player_position)
        pygame.display.flip()
