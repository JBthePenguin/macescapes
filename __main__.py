#! /usr/bin/env python3
# coding: utf-8

# from modules.labyrinth import Labyrinth
# from modules import labyrinth
# import local_modules.labyrinth as labyrinth
from labyrinth import labyrinth


def main():
    """ main function """
    gaming_map = labyrinth.Labyrinth()
    gaming_map.display()


if __name__ == "__main__":
    main()
