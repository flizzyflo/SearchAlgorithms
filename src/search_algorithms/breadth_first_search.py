from src.map_structure.map_structure import MapStructure
from src.settings.settings import BLOCKSIZE, VISITED_BLOCK
from src.search_algorithms.algorithms_abstract_base_class import Algorithm
from queue import Queue


class Bfs(Algorithm):

    def __init__(self, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)
        self.block_queue = Queue()

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]) -> None:
        self.start_coordinates = start_coordinates
        self.block_queue.put(self.start_coordinates)

    def initialize_goal_coordinates(self, goal_coordinates: tuple[int, int]) -> None:
        self.goal_coordinates = goal_coordinates

    def perform_search(self) -> None:

        # goal was not found
        if self.block_queue.empty():
            self.no_way_found = True

        # get next block to visit
        cur_x, cur_y = self.block_queue.get()
        self.current_coordinates = (cur_x, cur_y)

        if self.current_coordinates in self.is_visited:
            return

        # case: goal reached
        if self.goal_detected(block_coordinates=self.current_coordinates):
            self.goal_found = True
            return

        # current coordinate is not visible / existing
        if self.is_valid_coordinate(block_coordinates=(cur_x, cur_y)) is False:
            return

        # check any adjacent coordinate. blocksize is the step-length to take to get to the neighbour
        if self.is_valid_coordinate(block_coordinates=(cur_x + BLOCKSIZE, cur_y)):
            self.block_queue.put((cur_x + BLOCKSIZE, cur_y))
        if self.is_valid_coordinate(block_coordinates=(cur_x - BLOCKSIZE, cur_y)):
            self.block_queue.put((cur_x - BLOCKSIZE, cur_y))
        if self.is_valid_coordinate(block_coordinates=(cur_x, cur_y - BLOCKSIZE)):
            self.block_queue.put((cur_x, cur_y - BLOCKSIZE))
        if self.is_valid_coordinate(block_coordinates=(cur_x, cur_y + BLOCKSIZE)):
            self.block_queue.put((cur_x, cur_y + BLOCKSIZE))

        self.is_visited.add(self.current_coordinates)

        if self.current_coordinates == self.start_coordinates:
            pass
        else:
            self.map_structure.final_map[self.current_coordinates] = VISITED_BLOCK
