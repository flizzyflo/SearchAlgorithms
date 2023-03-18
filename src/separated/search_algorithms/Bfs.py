
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
        self.no_way: bool = False
        self.visited: set[tuple[int, int]] = set()

    def search_is_over(self) -> bool:
        return any([self.goal_found, self.no_way])

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]):
        self.start_coordinates = start_coordinates
        self.queue.put(self.start_coordinates)

    def initialize_goal_coordinates(self, goal_coordinates: tuple[int, int]):
        self.goal_coordinates = goal_coordinates

    def no_way_exists(self) -> bool:
        return self.no_way

    def perform_search(self):
        cur_x, cur_y = self.queue.get()
        self.current_coordinates = (cur_x, cur_y)

        if self.queue.empty():
            self.no_way = True

        if self.current_coordinates in self.visited:
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
            self.queue.put((cur_x + BLOCKSIZE, cur_y))
        if self.is_valid_coordinate(block_coordinates=(cur_x - BLOCKSIZE, cur_y)):
            self.queue.put((cur_x - BLOCKSIZE, cur_y))
        if self.is_valid_coordinate(block_coordinates=(cur_x, cur_y - BLOCKSIZE)):
            self.queue.put((cur_x, cur_y - BLOCKSIZE))
        if self.is_valid_coordinate(block_coordinates=(cur_x, cur_y + BLOCKSIZE)):
            self.queue.put((cur_x, cur_y + BLOCKSIZE))

        self.visited.add(self.current_coordinates)

        if self.current_coordinates == self.start_coordinates:
            pass
        else:
            self.map.final_map[self.current_coordinates] = 3

    def get_current_coordinates(self) -> tuple[int, int]:
        return self.current_coordinates

    def goal_detected(self, block_coordinates: tuple[int, int]) -> bool:
        return block_coordinates == self.goal_coordinates

    def is_valid_coordinate(self, block_coordinates) -> bool:
        return self.is_wall(block_coordinates=block_coordinates) is False and self.is_in_bounds(
            block_coordinates=block_coordinates)

    def is_wall(self, block_coordinates) -> bool:
        try:
            return self.map.final_map[block_coordinates] == 1
        except KeyError as ke:

            pass

    def is_in_bounds(self, block_coordinates) -> bool:
        return (0, 0) < block_coordinates < (WIDTH, HEIGHT)
