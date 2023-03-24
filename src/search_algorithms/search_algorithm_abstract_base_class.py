from abc import ABC, abstractmethod

from src.map_structure.map_structure import MapStructure
from src.settings.settings import BLOCKSIZE, WALL_BLOCK


class SearchAlgorithm(ABC):

    def __init__(self, map_structure: MapStructure) -> None:
        self.is_visited: set[tuple[int, int]] = set()
        self.no_way_found: bool = False
        self.destination_detected: bool = False
        self.current_coordinates: tuple[int, int] = None
        self.start_coordinates: tuple[int, int] = (0, 0)
        self.destination_coordinates: tuple[int, int] = (0, 0)
        self.map_structure: MapStructure = map_structure
        self.height = self.map_structure.get_height()
        self.width = self.map_structure.get_width()

    @abstractmethod
    def perform_search(self) -> None:
        """
        Performs the specific implementation of the search algorithm
        """

        ...

    def initialize_destination_coordinates(self, goal_coordinates: tuple[int, int]) -> None:
        self.destination_coordinates = goal_coordinates

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
            # Key does not exist within final map -> out of bounds, cant be a wall, return false
            # will be catched by is_in_bounds method
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

        current_width: int = block_coordinates[0]
        current_height: int = block_coordinates[1]

        return (0 <= current_width <= self.width - BLOCKSIZE) and (0 <= current_height <= self.height - BLOCKSIZE)

    def no_way_exists(self) -> bool:

        """
        Checks if no way can be found. Returns either true or false
        Returns
        true - no way exists
        false - way exists
        -------
        """

        return self.no_way_found

    def already_visited_block(self, block_coordinates: tuple[int, int]) -> bool:

        """
        Returns whether a block is already visited or not
        Parameters
        ----------
        block_coordinates - tuple of x and y coordinate of the respective block

        Returns
        -------
        true - block was visited
        false - block was not visited
        """

        return block_coordinates in self.is_visited

    def search_is_over(self) -> bool:

        """
        Wrapper function to check whether the search is over or not. Returns any true value out of
        goal_found or no_way_found methods. Since when one of them is true, the search is over.
        Returns
        true - search is over
        false - continue search
        -------

        """

        return any([self.destination_detected, self.no_way_found])

    def visited_this_block(self, block_coordinates: tuple[int, int]) -> None:

        """
        Adds the block coordinates passed in into the is_visited set
        """

        self.is_visited.add(block_coordinates)

    def is_destination(self, block_coordinates: tuple[int, int]) -> bool:
        """
        Returns if the desired destination block is found
        """

        return block_coordinates == self.destination_coordinates

    def destination_found(self) -> bool:
        return self.destination_detected
