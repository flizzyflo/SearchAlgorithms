
from src.separated.Settings.settings import BLOCKSIZE, HEIGHT, WIDTH
from src.separated.search_algorithms.Algorithms import Algorithms
from queue import Queue


class Bfs(Algorithms):

    def __init__(self, map) -> None:
        self.queue = Queue()
        self.map = map
        self.start_coordinates: tuple[int, int] = (0, 0)
        self.goal_coordinates: tuple[int, int] = (0, 0)
        self.current_coordinates: tuple[int, int] = self.start_coordinates
        self.goal_found: bool = False

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]):
        self.start_coordinates = start_coordinates
        self.queue.put(self.start_coordinates)

    def initialize_goal_coordinates(self, goal_coordinates: tuple[int, int]):
        self.goal_coordinates = goal_coordinates

    def perform_search(self):
        cur_x, cur_y = self.queue.get()
        self.current_coordinates = (cur_x, cur_y)

       # case: goal reached
        if self.goal_detected(block_coordinates=self.current_coordinates):
            self.goal_found = True
            return

        # current coordinate is not visible / existing
        if not self.is_valid_coordinate(block_coordinates=(cur_x, cur_y)):
            return

        # check any adjacent coordinate
        if self.is_valid_coordinate(block_coordinates=(cur_x + BLOCKSIZE, cur_y)):
            self.queue.put((cur_x + BLOCKSIZE, cur_y))
        if self.is_valid_coordinate(block_coordinates=(cur_x - BLOCKSIZE, cur_y)):
            self.queue.put((cur_x - BLOCKSIZE, cur_y))
        if self.is_valid_coordinate(block_coordinates=(cur_x, cur_y - BLOCKSIZE)):
            self.queue.put((cur_x, cur_y - BLOCKSIZE))
        if self.is_valid_coordinate(block_coordinates=(cur_x, cur_y + BLOCKSIZE)):
            self.queue.put((cur_x, cur_y + BLOCKSIZE))

        self.map.final_map[self.current_coordinates] = 3

    def get_current_coordinates(self) -> tuple[int, int]:
        return self.current_coordinates

    def goal_detected(self, block_coordinates: tuple[int, int]) -> bool:
        return block_coordinates == self.goal_coordinates

    def is_valid_coordinate(self, block_coordinates) -> bool:
        return self.is_wall(block_coordinates=block_coordinates) is False and self.is_in_bounds(
            block_coordinates=block_coordinates)

    def is_wall(self, block_coordinates) -> bool:
        return self.map.final_map[block_coordinates] == 1

    def is_in_bounds(self, block_coordinates) -> bool:
        return (0, 0) < block_coordinates < (WIDTH, HEIGHT)
