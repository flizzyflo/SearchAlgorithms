import pygame
from src.separated.Settings.settings import *

class Map:

    def __init__(self):
        self.surface: pygame.Surface = None
        self.final_map: dict[tuple[int, int], int] = {}
        self.initialize_input_map()
        self.start_count = 0
        self.all_rectangles: dict[tuple[int, int], pygame.Rect] = {}

    def initialize_input_map(self):

        for i in range((HEIGHT + BLOCKSIZE) // BLOCKSIZE):
            for j in range((WIDTH + BLOCKSIZE) // BLOCKSIZE):

                self.final_map[(j * BLOCKSIZE, i * BLOCKSIZE)] = 0

    def get_final_map(self) -> dict[tuple[int, int], int]:
        return self.final_map

    def get_start_end_points(self) -> list[tuple[int, int]]:
        # returns both, start and end point
        return [position for position in self.final_map if self.final_map[position] == 2]

    def increase_start_count(self) -> None:
        if self.start_count + 1 < 3:
            self.start_count += 1

    def decrease_start_count(self) -> None:
        if self.start_count - 1 >= 0:
            self.start_count -= 1

