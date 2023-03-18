from abc import ABC, abstractmethod

from src.map_structure.map_structure import MapStructure
from src.settings.settings import WIDTH, HEIGHT


class Algorithms(ABC):

    def __init__(self, map_structure) -> None:
        self.is_visited: set[tuple[int, int]] = set()
        self.no_way_found: bool = False
        self.goal_found: bool = False
        self.current_coordinates: tuple[int, int] = None
        self.start_coordinates: tuple[int, int] = (0, 0)
        self.goal_coordinates: tuple[int, int] = (0, 0)
        self.map_structure: MapStructure = map_structure

    @abstractmethod
    def perform_search(self) -> None:
        """
        The Search algorithm itself to be implemented, like for exampe dfs or bfs.
        """

        ...

    @abstractmethod
    def initialize_goal_coordinates(self, goal_coordinates: tuple[int, int]) -> None:
        ...

    @abstractmethod
    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]) -> None:
        ...

    def is_wall(self, block_coordinates: tuple[int, int]) -> bool:
        """
        Checks whether a coordinate passed in is a wall or not and returns either true or false
        """

        try:
            return self.map_structure.final_map[block_coordinates] == 1
        except KeyError as ke:
            pass

    def is_valid_coordinate(self, block_coordinates: tuple[int, int]) -> bool:
        """
        Wrapper method. Returns true if coordinates are no wall and are in bounds.
        """

        return self.is_wall(block_coordinates=block_coordinates) is False and self.is_in_bounds(
            block_coordinates=block_coordinates)

    def is_in_bounds(self, block_coordinates: tuple[int, int]) -> bool:

        """
        Checks whether the coordinates are within the painted screen or not and return either true or false.
        """

        return (0, 0) < block_coordinates < (WIDTH, HEIGHT)

    def no_way_exists(self) -> bool:
        return self.no_way_found

    def search_is_over(self) -> bool:
        return any([self.goal_found, self.no_way_found])

    def goal_detected(self, block_coordinates: tuple[int, int]) -> bool:
        """
        Returns if the desired block is found
        """

        return block_coordinates == self.goal_coordinates

    def get_current_coordinates(self) -> tuple[int, int]:
        return self.start_coordinates
