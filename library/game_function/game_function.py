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


def move_player(player_position, background, key_event):
    """check if the new position is possible
    and move the player if it's ok"""
    # create a list of possible new position
    available_positions = create_list(background)
    # find new position and set the movement
    new_x = int(player_position[0]) / 40
    new_y = int(player_position[1]) / 40
    movement_x = 0
    movement_y = 0
    if key_event == K_LEFT:
        new_x -= 1
        movement_x = -40
    elif key_event == K_RIGHT:
        new_x += 1
        movement_x = 40
    elif key_event == K_UP:
        new_y -= 1
        movement_y = -40
    elif key_event == K_DOWN:
        new_y += 1
        movement_y = 40
    # check if the new position is possible and move if it's ok
    new_position = (new_x, new_y)
    if new_position in available_positions:
        player_position = player_position.move(
            movement_x, movement_y)
    return player_position


def launch(background, movable_elt, elements):
    """launch the game on  gui """
    # create a window
    pygame.init()
    window = pygame.display.set_mode((600, 600))
    # create an object Rect for the player
    player = pygame.image.load(movable_elt.path_to_img).convert_alpha()
    player_position = player.get_rect(topleft=(40, 40))
    # available_positions = create_list(background)
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
                player_position = move_player(
                    player_position, background, event.key)
        # paste all on the window and refresh it
        paste_background(window, background)
        paste_elements(window, elements)
        window.blit(player, player_position)
        pygame.display.flip()
