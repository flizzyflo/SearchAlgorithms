
from queue import Queue

from src.map_structure.map_structure import MapStructure
from src.search_algorithms.search_algorithm_abstract_base_class import SearchAlgorithm
from src.settings.settings import BlockColors


class Bfs(SearchAlgorithm):

    def __init__(self, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)
        self.block_queue = Queue()

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]) -> None:
        self.start_coordinates = start_coordinates
        self.block_queue.put(self.start_coordinates)

    def get_next_block(self) -> tuple[int, int]:
        return self.block_queue.get()

    def perform_search(self, current_block_to_investigate: tuple[int, int]) -> None:

        # goal was not found
        if self.block_queue.empty():
            self.no_way_found = True

        # get next block to visit
        current_block_x, current_block_y = current_block_to_investigate
        self.current_coordinates = (current_block_x, current_block_y)

        if self.already_visited_block(block_coordinates=self.current_coordinates):
            return

        # case: goal reached
        if self.is_destination(block_coordinates=self.current_coordinates):
            self.destination_detected = True
            return

        # current coordinate is not visible / existing
        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y)) is False:
            return

        # check any adjacent coordinate. blocksize is the step-length to take to get to the neighbour
        if self.is_valid_coordinate(block_coordinates=(current_block_x + self.blocksize, current_block_y)):
            neighbour = (current_block_x + self.blocksize, current_block_y)
            if not self.already_visited_block(block_coordinates=neighbour):
                self.change_block_color(block_coordinates=neighbour,
                                        desired_block_color_value=BlockColors.blue.value)
                self.block_queue.put(neighbour)

        if self.is_valid_coordinate(block_coordinates=(current_block_x - self.blocksize, current_block_y)):
            neighbour = (current_block_x - self.blocksize, current_block_y)
            if not self.already_visited_block(block_coordinates=neighbour):
                self.change_block_color(block_coordinates=neighbour,
                                        desired_block_color_value=BlockColors.blue.value)
                self.block_queue.put(neighbour)

        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y - self.blocksize)):
            neighbour = (current_block_x, current_block_y - self.blocksize)
            if not self.already_visited_block(block_coordinates=neighbour):
                self.change_block_color(block_coordinates=neighbour,
                                        desired_block_color_value=BlockColors.blue.value)
                self.block_queue.put(neighbour)

        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y + self.blocksize)):
            neighbour = (current_block_x, current_block_y + self.blocksize)
            if not self.already_visited_block(block_coordinates=neighbour):
                self.change_block_color(block_coordinates=neighbour,
                                        desired_block_color_value=BlockColors.blue.value)
                self.block_queue.put(neighbour)

        self.visited_this_block(block_coordinates=self.current_coordinates)

        self.change_block_color(block_coordinates=self.current_coordinates,
                                desired_block_color_value=BlockColors.lightblue.value)
        self.change_block_color(block_coordinates=self.destination_coordinates,
                                desired_block_color_value=BlockColors.red.value)


