import random

import pygame

from src.settings.settings import *


class MapStructure:

    def __init__(self, *, width: int, height: int, randomized_walls: bool = False):
        self.surface: pygame.Surface = None
        self.final_map: dict[tuple[int, int], int] = {}
        self.all_rectangles: dict[tuple[int, int], pygame.Rect] = {}
        self.width = width
        self.height = height
        self.initialize_input_map()
        if randomized_walls:
            self.create_random_walls()

    def get_height(self) -> int:

        """
        Returns the current height of the map where the search is performed

        Returns
        -------
        Screen height as integer
        """

        return self.height

    def get_width(self) -> int:

        """
        Returns the current width of the map where the search is performed

        Returns
        -------
        Screen width as integer
        """
        return self.width

    def initialize_input_map(self) -> None:

        """
        Initializes the search map as map with empty blocks.
        Each coordinate is initialized as empty block.
        Returns
        -------
        None
        """

        # initializes an empty map. zero is an empty block
        # range is divided to calculate the number of blocks for both, height and width
        for i in range((self.height + BLOCKSIZE) // BLOCKSIZE):
            for j in range((self.width + BLOCKSIZE) // BLOCKSIZE):
                # coordinates are the key, value is the type of block, here initialized as empty block
                self.final_map[(j * BLOCKSIZE, i * BLOCKSIZE)] = EMPTY_BLOCK

    def create_random_walls(self) -> None:

        """
        Randomized walls are created on the map if selected.
        Returns
        -------
        None
        """

        for coordinate in self.final_map.keys():
            if random.randint(1, 20) % 3 == 0:
                self.final_map[coordinate] = WALL_BLOCK

    def get_final_map(self) -> dict[tuple[int, int], int]:

        """
        Returns the final map. Final map contains coordinates for all blocks within height x width and
        the respective value per coordinate.

        Returns
        -------
        final map as dictionary with tuples of integer pairs dict[tuple[int, int]]
        """

        return self.final_map

    def get_start_destination_points(self) -> tuple[tuple[int, int], tuple[int, int]]:

        """
        Gets the start and end point coordinates from the final map.
        Returns
        -------
        Start and endpoint coordinates as tuple containing the tuples of coordinates
        -> tuple[tuple[int, int], tuple[int, int]]
        """

        # returns both, start and end point
        start = [position for position in self.final_map.keys() if self.final_map[position] == START_BLOCK]
        destination = [position for position in self.final_map.keys() if self.final_map[position] == DESTINATION_BLOCK]
        return start[0], destination[0]
