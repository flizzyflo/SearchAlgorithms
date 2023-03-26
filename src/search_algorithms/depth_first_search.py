from src.map_structure.map_structure import MapStructure
from src.search_algorithms.search_algorithm_abstract_base_class import SearchAlgorithm
from src.settings.settings import BlockColors


class Dfs(SearchAlgorithm):

    def __init__(self, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)
        self.stack = list()

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]):
        self.start_coordinates = start_coordinates
        self.stack.append(start_coordinates)

    def get_next_block(self) -> tuple[int, int]:
        return self.stack.pop()

    def perform_search(self, next_block: tuple[int, int] = None) -> None:

        # goal was not found
        if not self.stack:
            self.no_way_found = True
            return

        # get next block to visit
        if next_block is None:
            current_block_x, current_block_y = self.get_next_block()

        else:
            current_block_x, current_block_y = next_block
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

        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y - self.blocksize)):
            neighbour_block = (current_block_x, current_block_y - self.blocksize)
            if not self.already_visited_block(block_coordinates=neighbour_block):
                self.change_block_color(block_coordinates=neighbour_block,
                                        desired_block_color=BlockColors.blue.value)
                self.stack.append(neighbour_block)

        if self.is_valid_coordinate(block_coordinates=(current_block_x - self.blocksize, current_block_y)):
            neighbour_block = (current_block_x - self.blocksize, current_block_y)
            if not self.already_visited_block(block_coordinates=neighbour_block):
                self.change_block_color(block_coordinates=neighbour_block,
                                        desired_block_color=BlockColors.blue.value)
                self.stack.append(neighbour_block)

        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y + self.blocksize)):
            neighbour_block = (current_block_x, current_block_y + self.blocksize)
            if not self.already_visited_block(block_coordinates=neighbour_block):
                self.change_block_color(block_coordinates=neighbour_block,
                                        desired_block_color=BlockColors.blue.value)
                self.stack.append(neighbour_block)

        if self.is_valid_coordinate(block_coordinates=(current_block_x + self.blocksize, current_block_y)):
            neighbour_block = (current_block_x + self.blocksize, current_block_y)
            if not self.already_visited_block(block_coordinates=neighbour_block):
                self.change_block_color(block_coordinates=neighbour_block,
                                        desired_block_color=BlockColors.blue.value)
                self.stack.append(neighbour_block)

        self.visited_this_block(block_coordinates=self.current_coordinates)

        self.change_block_color(block_coordinates=self.current_coordinates,
                                desired_block_color=BlockColors.lightblue.value)
        self.change_block_color(block_coordinates=self.destination_coordinates,
                                desired_block_color=BlockColors.red.value)
