""" Module with the class Labyrinth"""

import os
import pygame

main_dir = os.path.dirname(os.path.dirname(__file__))


class Labyrinth():
    """docstring for Labyrinth : Class with methods
    -   __init__()
    -   display"""

    def __init__(self):
        """ Function : initialise object with attribute
        -- background = {position xy : path towards the corresponding img}"""
        self.background = {}
        # get the right path
        path_to_file = os.path.join(main_dir, "maps", "default_map.txt")
        # open the file
        with open(path_to_file, "r") as f:
            # Initialize the position
            x = 0
            y = 0
            # read character by character
            for elt in f.read():
                if elt == "\n":
                    # update position
                    x = 0
                    y += 1
                else:
                    # associate corresponding image
                    if elt == "O":
                        path_to_img = os.path.join(main_dir, "img", "wall.png")
                    else:
                        path_to_img = os.path.join(
                            main_dir, "img", "floor.png")
                    # add key (x,y) and value (path to the file) in background
                    self.background[(x, y)] = path_to_img
                    # update position
                    x += 1

    def display(self):
        """ Function : display the background
        of the labyrinth on  a gui """
        pygame.init()
        # size of gui's window = 600 x 600 pixels
        window = pygame.display.set_mode((600, 600))
        # Initialise the position
        x = 0
        y = 0
        while y < 15:
            # take the right image
            img = pygame.image.load(self.background[(x, y)])
            # stick on the window
            window.blit(img, ((x * 40), (y * 40)))
            # update the position
            if x < 14:
                x += 1
            else:
                x = 0
                y += 1
        # refresh the display
        pygame.display.flip()
        # keep the display on ...
        gui_display = 1
        while gui_display:
            for event in pygame.event.get():
                # ... unless the window is closed
                if event.type == pygame.QUIT:
                    gui_display = None
