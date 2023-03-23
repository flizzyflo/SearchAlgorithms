from src.map_structure.map_structure import MapStructure
from src.settings.settings import BLOCKSIZE, VISITED_BLOCK
from src.search_algorithms.search_algorithm_abstract_base_class import SearchAlgorithm
from queue import Queue


class Bfs(SearchAlgorithm):

    def __init__(self, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)
        self.block_queue = Queue()

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]) -> None:
        self.start_coordinates = start_coordinates
        self.block_queue.put(self.start_coordinates)

    def perform_search(self) -> None:

        # goal was not found
        if self.block_queue.empty():
            self.no_way_found = True

        # get next block to visit
        current_block_x, current_block_y = self.block_queue.get()
        self.current_coordinates = (current_block_x, current_block_y)

        if self.already_visited_block(block_coordinates=self.current_coordinates ):
            return

        # case: goal reached
        if self.is_destination(block_coordinates=self.current_coordinates):
            self.destination_detected = True
            return

        # current coordinate is not visible / existing
        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y)) is False:
            return

        # check any adjacent coordinate. blocksize is the step-length to take to get to the neighbour
        if self.is_valid_coordinate(block_coordinates=(current_block_x + BLOCKSIZE, current_block_y)):
            neighbour = (current_block_x + BLOCKSIZE, current_block_y)
            self.block_queue.put(neighbour)

        if self.is_valid_coordinate(block_coordinates=(current_block_x - BLOCKSIZE, current_block_y)):
            neighbour = (current_block_x - BLOCKSIZE, current_block_y)
            self.block_queue.put(neighbour)

        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y - BLOCKSIZE)):
            neighbour = (current_block_x, current_block_y - BLOCKSIZE)
            self.block_queue.put(neighbour)

        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y + BLOCKSIZE)):
            neighbour = (current_block_x, current_block_y + BLOCKSIZE)
            self.block_queue.put(neighbour)

        self.visited_this_block(block_coordinates=self.current_coordinates)

        if self.current_coordinates == self.start_coordinates:
            pass
        else:
            # change map value to 'visited' to change color
            self.map_structure.final_map[self.current_coordinates] = VISITED_BLOCK
