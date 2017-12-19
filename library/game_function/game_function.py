#! /usr/bin/env python3
# coding: utf-8

""" Module with the functions of the game"""


def move_player(
        player_position, available_positions, direction, size_img):
    """check if the new position is an available position
    and move the player if it's yes"""

    # set position before the movement
    new_position_x = player_position[0]
    new_position_y = player_position[1]
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
        # and move the player if it's ok
        player_position = player_position.move(
            movement_x, movement_y)
    return player_position


def check_position(
        perso_position, objects, objects_recovered,
        size_img, size_window):
    """check the position with objects"""

    for obj in objects:
        # if the same position
        if (perso_position[0] == obj.position[0]) and (
                perso_position[1] == obj.position[1]):
            # update objects_recovered
            objects_recovered += 1
            # put the revovered object in the counter background
            x = size_window[0] - (size_img[0] * objects_recovered * 1.5)
            y = size_window[1] - size_img[1]
            obj.position = (x, y)
    return (objects, objects_recovered)


def check_win(perso_position, enemy_position):
    """ check if the player arrive at the finish point"""

    if (perso_position[0] == enemy_position[0]) and (
            perso_position[1] == enemy_position[1]):
        return 0
    else:
        return 1
