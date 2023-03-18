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

    def draw(self) -> None:

        for position in self.final_map:
            map_value = self.final_map[position]

            # wall element
            if map_value == 1:
                rect = pygame.draw.rect(surface=self.surface,
                                        rect=(position[0], position[1], BLOCKSIZE, BLOCKSIZE),
                                        color=WALL_COLOR,
                                        width=1)

            # start / goal element
            elif map_value == 2:
                rect = pygame.draw.rect(surface=self.surface,
                                        rect=(position[0], position[1], BLOCKSIZE, BLOCKSIZE),
                                        color=START_GOAL_COLOR,
                                        border_radius=1)

            # empty element
            elif map_value == 0:
                rect = pygame.draw.rect(surface=self.surface,
                                        rect=(position[0], position[1], BLOCKSIZE, BLOCKSIZE),
                                        color=EMPTY_COLOR)

            elif map_value == 3:
                rect = pygame.draw.rect(surface=self.surface,
                                        rect=(position[0], position[1], BLOCKSIZE, BLOCKSIZE),
                                        color="yellow")

            self.all_rectangles[(position[0], position[1])] = rect
