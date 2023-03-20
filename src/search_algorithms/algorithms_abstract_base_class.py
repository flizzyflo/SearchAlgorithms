from abc import ABC, abstractmethod

from src.map_structure.map_structure import MapStructure
from src.settings.settings import BLOCKSIZE, WALL_BLOCK


class Algorithm(ABC):

    def __init__(self, map_structure: MapStructure) -> None:
        self.is_visited: set[tuple[int, int]] = set()
        self.no_way_found: bool = False
        self.goal_found: bool = False
        self.current_coordinates: tuple[int, int] = None
        self.start_coordinates: tuple[int, int] = (0, 0)
        self.goal_coordinates: tuple[int, int] = (0, 0)
        self.map_structure: MapStructure = map_structure
        self.height = self.map_structure.get_heigth()
        self.width = self.map_structure.get_width()

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

    def is_no_wall(self, block_coordinates: tuple[int, int]) -> bool:
        """
        Checks whether a coordinate passed in is a wall or not and returns either true or false
        """

        try:
            return self.map_structure.final_map[block_coordinates] != WALL_BLOCK

        except KeyError as ke:
            False

    def is_valid_coordinate(self, block_coordinates: tuple[int, int]) -> bool:
        """
        Wrapper method. Returns true if coordinates are no wall and are in bounds.
        """

        return (self.is_no_wall(block_coordinates=block_coordinates)) and self.is_in_bounds(block_coordinates=block_coordinates)

    def is_in_bounds(self, block_coordinates: tuple[int, int]) -> bool:

        """
        Checks whether the coordinates are within or are border of the painted screen
        or not and return either true or false.
        """
        return (0 <= block_coordinates[0] <= self.width - BLOCKSIZE) and (0 <= block_coordinates[1] <= self.height - BLOCKSIZE)

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
