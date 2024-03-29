import random

import pygame

from src.settings.settings import *


class MapStructure:

    def __init__(self, *, width: int, height: int, blocksize: int, randomized_walls: bool = False):
        self.surface: pygame.Surface = None
        self.final_map: dict[tuple[int, int], int] = {}
        self.all_rectangles: dict[tuple[int, int], pygame.Rect] = {}
        self.width: int = width
        self.height: int = height
        self.blocksize: int = blocksize
        self.initialize_input_map()
        if randomized_walls:
            self.create_random_walls()

    def get_blocksize(self) -> int:
        return self.blocksize

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
        for i in range((self.height + self.blocksize) // self.blocksize):
            for j in range((self.width + self.blocksize) // self.blocksize):
                # coordinates are the key, value is the type of block, here initialized as empty block
                self.final_map[(j * self.blocksize, i * self.blocksize)] = BlockColors.white.value

    def create_random_walls(self) -> None:

        """
        Randomized walls are created on the map if selected.
        Returns
        -------
        None
        """

        for coordinate in self.final_map.keys():
            if random.randint(1, 20) % 3 == 0:
                self.final_map[coordinate] = BlockColors.black.value

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
        start = [position for position in self.final_map.keys() if self.final_map[position] == BlockColors.purple.value]
        destination = [position for position in self.final_map.keys() if self.final_map[position] == BlockColors.red.value]
        return start[0], destination[0]

    def set_blocks_to_shortest_path(self, blocks_to_be_painted: list[tuple[int, int]]) -> None:
        start, destination = self.get_start_destination_points()
        for block in blocks_to_be_painted:
            if block == start or block == destination:
                continue
            self.final_map[block] = BlockColors.green.value

    def clear_selected_next_blocks(self) -> None:
        for block, block_status in self.final_map.items():
            if block_status == BlockColors.blue.value:
                self.final_map[block] = BlockColors.white.value

    def end_search_bc_no_way(self):
        for block, block_value in self.final_map.items():
            if block_value == BlockColors.red.value or block_value == BlockColors.purple.value:
                continue
            self.final_map[block] = BlockColors.DARK_RED.value
