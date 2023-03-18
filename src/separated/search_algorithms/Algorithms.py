import pygame
from queue import Queue
from src.separated.Map import Map
from abc import ABC


class Algorithms(ABC):

    def perform_search(self):
        ...

    def is_wall(self, block_coordinates) -> bool:
        ...

    def is_valid_coordinate(self, block_coordinates) -> bool:
        ...

    def is_in_bounds(self, block_coordinates) -> bool:
        ...

    def goal_detected(self, block_coordinates: tuple[int, int]) -> bool:
        ...

    def initialize_goal_coordinates(self, goal_coordinates: tuple[int, int]):
        ...

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]):
        ...

    def get_current_coordinates(self):
        ...