import pygame
import random
from src.settings.settings import *


class MapStructure:

    def __init__(self, randomized_walls: bool = False):
        self.surface: pygame.Surface = None
        self.final_map: dict[tuple[int, int], int] = {}
        self.all_rectangles: dict[tuple[int, int], pygame.Rect] = {}

        self.initialize_input_map()
        if randomized_walls:
            self.create_random_walls()

    def initialize_input_map(self) -> None:
        # initializes an empty map. zero is an empty block
        for i in range((HEIGHT + BLOCKSIZE) // BLOCKSIZE):
            for j in range((WIDTH + BLOCKSIZE) // BLOCKSIZE):
                self.final_map[(j * BLOCKSIZE, i * BLOCKSIZE)] = EMPTY_BLOCK

    def create_random_walls(self) -> None:
        for key, value in self.final_map.items():
            if random.randint(1, 20) % 3 == 0:
                self.final_map[key] = WALL_BLOCK

    def get_final_map(self) -> dict[tuple[int, int], int]:
        return self.final_map

    def get_start_end_points(self) -> list[tuple[int, int]]:
        # returns both, start and end point
        start = [position for position in self.final_map if self.final_map[position] == START_BLOCK]
        end = [position for position in self.final_map if self.final_map[position] == END_BLOCK]
        return start[0], end[0]
