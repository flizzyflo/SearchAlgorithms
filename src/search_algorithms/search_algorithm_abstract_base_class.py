from abc import ABC, abstractmethod

from src.map_structure.map_structure import MapStructure
from src.search_algorithms.path_finding_algorithms.node import Node
from src.settings.settings import BlockColors


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
        self.blocksize: int = self.map_structure.get_blocksize()

    @abstractmethod
    def get_next_block(self) -> tuple[int, int] | Node:

        """
        This method is used to get the next block which should be investigated by the specific search
        algorithm selected.
        Returns
        -------
        Tuple of coordinates
        """

        ...

    @abstractmethod
    def perform_search(self, current_block_to_investigate: tuple[int, int] | Node) -> None:

        """
        Performs the specific implementation of the search algorithm. Takes the next
        block which should be investigated as an argument, either as tuple of its coordinates (Bfs, Dfs) or
        as Node object (A*, Djikstra)
        """

        ...

    def initialize_destination_coordinates(self, destination_coordinates: tuple[int, int]) -> None:

        """
        Initializes the destination coordinates into the search algorithm instance
        Parameters
        ----------
        destination_coordinates: tuple of coordinates of the specific destination marked within the UI

        Returns
        -------
        None
        """

        self.destination_coordinates = destination_coordinates

    @abstractmethod
    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]) -> None:

        """
        Initializes the start coordinates as a parameter of the search-algorithm instance.
        Also puts the start coordinates into the respective data structure of the algorithm to be able to start
        the algorithm.
        Parameters
        ----------
        start_coordinates: tuple of coordinates of the starting point for the search to be performed

        Returns
        -------
        None
        """
        ...

    def is_no_wall(self, block_coordinates: tuple[int, int]) -> bool:

        """
        Checks whether a coordinate passed in is a wall or not
        Returns
        -------
        True - No wall
        False - is Wall
        """

        try:
            return self.map_structure.final_map[block_coordinates] != BlockColors.black.value

        except KeyError as ke:
            # Key does not exist within final map -> out of bounds, cant be a wall, return false
            # will be catched by is_in_bounds method
            return False

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

        return (0 <= current_width <= self.width - self.blocksize) and (0 <= current_height <= self.height - self.blocksize)

    def no_way_exists(self) -> bool:

        """
        Checks if no way can be found. Returns either true or false
        Returns
        True - no way exists
        False - way exists
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
        True - block was visited
        False - block was not visited
        """

        return block_coordinates in self.is_visited

    def search_is_over(self) -> bool:

        """
        Wrapper function to check whether the search is over or not. Returns any true value out of
        goal_found or no_way_found methods. Since when one of them is true, the search is over.
        Returns
        True - search is over
        False - continue search
        -------

        """

        return any([self.destination_detected, self.no_way_found])

    def visited_this_block(self, *, block_coordinates: tuple[int, int]) -> None:

        """
        Adds the block coordinates passed in into the is_visited set
        """

        self.is_visited.add(block_coordinates)

    def is_destination(self, block_coordinates: tuple[int, int]) -> bool:

        """
        Checks whether the block passed in as argument is the destination or not

        Parameters
        ----------
        block_coordinates: Tuple of coordinates of the block to be inspected

        Returns
        ----------
        True - block is destination block
        False - block is not destination block
        """

        return block_coordinates == self.destination_coordinates

    def destination_found(self) -> bool:

        """
        Method to check the current status of whether the destination is already found or not.
        Returns
        -------
        True - destination is already found
        False - destination is not found

        """

        return self.destination_detected

    def change_block_color(self, block_coordinates: tuple[int, int], desired_block_color_value: int) -> None:

        """
        Method to change the block value stored in the map object. This is used to determine the color of the block
        Parameters
        ----------
        block_coordinates: passed in as tuple, coordinates of the block which color should be changed
        desired_block_color_value: block color as integer value

        Returns
        -------

        """

        if self.current_coordinates == self.start_coordinates:
            pass
        else:
            self.map_structure.final_map[block_coordinates] = desired_block_color_value
