from src.map_structure.map_structure import MapStructure
from src.search_algorithms.search_algorithm_abstract_base_class import SearchAlgorithm
from src.settings.settings import BLOCKSIZE, VISITED_BLOCK


class Dfs(SearchAlgorithm):

    def __init__(self, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)
        self.stack = list()

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]):
        self.start_coordinates = start_coordinates
        self.stack.append(start_coordinates)

    def perform_search(self) -> None:

        # goal was not found
        if not self.stack:
            self.no_way_found = True
            return

        # get next block to visit
        current_block_x, current_block_y = self.stack.pop()
        self.current_coordinates = (current_block_x, current_block_y)

        # check block was already visited, will be skipped
        if self.already_visited_block(block_coordinates=self.current_coordinates):
            return

        # goal was found.
        if self.is_destination(block_coordinates=self.current_coordinates):
            self.destination_detected = True
            return

        # case way can exist and goal not detected. put neighbours to stack
        # blocksize is the step-length to take to get to the neighbour

        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y - BLOCKSIZE)):
            self.stack.append((current_block_x, current_block_y - BLOCKSIZE))

        if self.is_valid_coordinate(block_coordinates=(current_block_x - BLOCKSIZE, current_block_y)):
            self.stack.append((current_block_x - BLOCKSIZE, current_block_y))

        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y + BLOCKSIZE)):
            self.stack.append((current_block_x, current_block_y + BLOCKSIZE))

        if self.is_valid_coordinate(block_coordinates=(current_block_x + BLOCKSIZE, current_block_y)):
            self.stack.append((current_block_x + BLOCKSIZE, current_block_y))

        self.visited_this_block(block_coordinates=self.current_coordinates)

        # change values within the map structure for colorizing.
        # if current position is start position, then it should not be colorized
        if self.current_coordinates == self.start_coordinates:
            pass

        else:
            # change map value to 'visited' to change color
            self.map_structure.final_map[self.current_coordinates] = VISITED_BLOCK
