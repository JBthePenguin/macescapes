#! /usr/bin/env python3
# coding: utf-8

""" Module with the functions of the game"""

import pygame.display

import pygame.image

import pygame.event

from pygame.locals import *


def create_available_positions(background):
    """ create a list of available positions"""
    available_positions = []
    for position in background:
        if "floor" in background[position]:
            available_positions.append(position)
    return available_positions


def paste_background(window, background, size_img):
    """ paste the background on the window
    with the corresponding image for each position"""
    for key in background:
        img = pygame.image.load(background[key]).convert()
        x = key[0]
        y = key[1]
        window.blit(img, (x, y))


def paste_objects(window, objects):
    """ paste the differents elements on the window
    with the corresponding image"""
    for obj in objects:
        img = pygame.image.load(obj.path_to_img).convert_alpha()
        x = obj.position[0]
        y = obj.position[1]
        window.blit(img, (x, y))


def move_perso(perso_gui_position, background, key_event, size_img):
    """check if the new position is possible
    and move the player if it's ok"""
    # create a list of possible new position
    available_positions = create_available_positions(background)
    # find the diection of the movement
    new_position_x = perso_gui_position[0]
    new_position_y = perso_gui_position[1]
    movement_x = 0
    movement_y = 0
    if key_event == K_LEFT:
        new_position_x -= size_img[0]
        movement_x = (-size_img[0])
    elif key_event == K_RIGHT:
        new_position_x += size_img[0]
        movement_x = size_img[0]
    elif key_event == K_UP:
        new_position_y -= size_img[1]
        movement_y = -size_img[1]
    elif key_event == K_DOWN:
        new_position_y += size_img[1]
        movement_y = size_img[1]
    # check if the new position is possible and move if it's ok
    new_position = (new_position_x, new_position_y)
    if new_position in available_positions:
        perso_gui_position = perso_gui_position.move(
            movement_x, movement_y)
    return perso_gui_position


def check_win(perso_gui_position, enemy_position):
    """ check if the player rrive at end point"""
    if (perso_gui_position[0] == enemy_position[0]) and (
            perso_gui_position[1] == enemy_position[1]):
        return 0
    else:
        return 1


def play_game(background, perso, enemy, objects, size_img):
    """launch the game on  gui and play it"""
    # create a window
    pygame.init()
    window = pygame.display.set_mode((600, 660))
    # create an object Rect for the perso
    perso_gui = pygame.image.load(perso.path_to_img).convert_alpha()
    perso_gui_position = perso_gui.get_rect(topleft=perso.position)
    # create an object Surface for enemy
    enemy_gui = pygame.image.load(enemy.path_to_img).convert_alpha()
    # moving when the key reaims depressed
    pygame.key.set_repeat(400, 30)
    # keep the window open ...
    gui_display = 1
    while gui_display:
        for event in pygame.event.get():
            # ... unless the window is closed or game is over
            if event.type == QUIT:
                gui_display = 0
            # move the player in the correct direction
            elif event.type == KEYDOWN:
                perso_gui_position = move_perso(
                    perso_gui_position, background, event.key, size_img)
                gui_display = check_win(perso_gui_position, enemy.position)
        # paste all on the window and refresh it
        paste_background(window, background, size_img)
        paste_objects(window, objects)
        window.blit(enemy_gui, enemy.position)
        window.blit(perso_gui, perso_gui_position)
        pygame.display.flip()
