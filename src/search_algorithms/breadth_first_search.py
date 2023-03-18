from src.map_structure.map_structure import MapStructure
from src.settings.settings import BLOCKSIZE, HEIGHT, WIDTH
from src.search_algorithms.algorithms_abstract_base_class import Algorithms
from queue import Queue


class Bfs(Algorithms):

    def __init__(self, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)
        self.block_queue = Queue()

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]) -> None:
        self.start_coordinates = start_coordinates
        self.block_queue.put(self.start_coordinates)

    def initialize_goal_coordinates(self, goal_coordinates: tuple[int, int]) -> None:
        self.goal_coordinates = goal_coordinates

    def perform_search(self) -> None:

        if self.block_queue.empty():
            self.no_way_found = True

        cur_x, cur_y = self.block_queue.get()
        self.current_coordinates = (cur_x, cur_y)


        if self.current_coordinates in self.is_visited:
            return

       # case: goal reached
        if self.goal_detected(block_coordinates=self.current_coordinates):
            self.goal_found = True
            return

        # current coordinate is not visible / existing
        if not self.is_valid_coordinate(block_coordinates=(cur_x, cur_y)):
            return

        # check any adjacent coordinate
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
            self.map_structure.final_map[self.current_coordinates] = 3
