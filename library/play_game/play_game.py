#! /usr/bin/env python3
# coding: utf-8

""" Module with function play_game
configuring to use with module pygame.locals"""

# import from third party module : pygame.locals
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN


def play_game(
        event, player, player_rect, elements, elements_recovered,
        constructed_elt, available_positions,
        counter_position, start_position):
    """find the direction, move the player if necessary,
    found element if there is one at the new position,
    if it's the end point, check if the player win or lose
    before return all with update
    event : event from pygame with type KEYDOWN
    player : class Element
    player_rect : class Rect
    elements : list of objects with class Element
    elements_recovered : int
    constructed_elt : class Element
    available_position : list
    counter_position : tuple
    start_position : tuple"""

    # initialise movement and element_founded
    movement, element_founded = 0, 0
    # find the direction ...
    if event.key == K_LEFT:
        # ... and test the movement
        movement = player.check_movement(available_positions, "left")
    elif event.key == K_RIGHT:
        movement = player.check_movement(available_positions, "right")
    elif event.key == K_UP:
        movement = player.check_movement(available_positions, "up")
    elif event.key == K_DOWN:
        movement = player.check_movement(available_positions, "down")
    if movement != 0:
        # move the player
        player_rect = player_rect.move(movement)
        # check the new position of player with other elements
        element_founded = player.check_position(
            elements, elements_recovered, counter_position)
    if element_founded != 0:
        if element_founded.feature == "recoverable":
            # update the counter
            elements_recovered += 1
            if elements_recovered == 3:
                # put poison if all elements are recovered
                elements.append(constructed_elt)
        elif element_founded.feature == "end":
            # the player arrive on end point
            if elements_recovered == 3:
                # WIN
                elements = []
                elements_recovered = "escapes!!!"
            else:
                # LOSE
                elements = [elements[0]]
                elements_recovered = "stays in prison!!!"
                player_rect = player.img.get_rect(topleft=start_position)
    return player, player_rect, elements, elements_recovered
