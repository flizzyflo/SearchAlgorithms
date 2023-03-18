import pygame
from queue import Queue
from src.separated.Map import Map
from abc import ABC, abstractmethod


class Algorithms(ABC):

    @abstractmethod
    def perform_search(self) -> None:

        """
        The Search algorithm itself to be implemented, like for exampe dfs or bfs.
        """

        ...

    @abstractmethod
    def is_wall(self, block_coordinates) -> bool:

        """
        Checks whether a coordinate passed in is a wall or not and returns either true or false
        """

        ...

    @abstractmethod
    def is_valid_coordinate(self, block_coordinates) -> bool:

        """
        Wrapper method. Returns true if coordinates are no wall and are in bounds.
        """

        ...

    @abstractmethod
    def is_in_bounds(self, block_coordinates) -> bool:

        """Checks whether the coordinates are within the painted screen or not and return either true or false"""

        ...

    @abstractmethod
    def no_way_exists(self) -> bool:
        ...

    @abstractmethod
    def goal_detected(self, block_coordinates: tuple[int, int]) -> bool:

        """
        Returns if the desired block is found
        """

        ...

    @abstractmethod
    def initialize_goal_coordinates(self, goal_coordinates: tuple[int, int]):
        ...

    @abstractmethod
    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]):
        ...

    @abstractmethod
    def get_current_coordinates(self):
        ...
