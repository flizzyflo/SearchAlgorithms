from src.map_structure.map_structure import MapStructure
from src.search_algorithms.algorithms_abstract_base_class import Algorithm
from src.settings.settings import BLOCKSIZE, VISITED_BLOCK


class Dfs(Algorithm):

    def __init__(self, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)
        self.stack = list()

    def initialize_goal_coordinates(self, goal_coordinates: tuple[int, int]):
        self.goal_coordinates = goal_coordinates

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]):
        self.start_coordinates = start_coordinates
        self.stack.append(start_coordinates)

    def perform_search(self) -> None:

        # goal was not found
        if not self.stack:
            self.no_way_found = True
            return

        # get next block to visit
        cur_x, cur_y = self.stack.pop()
        self.current_coordinates = (cur_x, cur_y)

        # block was already visited, will be skipped
        if self.current_coordinates in self.is_visited:
            return

        # goal was found.
        if self.current_coordinates == self.goal_coordinates:
            self.goal_found = True
            return

        # case way can exist and goal not detected. put neighbours to stack
        # blocksize is the step-length to take to get to the neighbour
        if self.is_valid_coordinate(block_coordinates=(cur_x, cur_y - BLOCKSIZE)):
            self.stack.append((cur_x, cur_y - BLOCKSIZE))
        if self.is_valid_coordinate(block_coordinates=(cur_x - BLOCKSIZE, cur_y)):
            self.stack.append((cur_x - BLOCKSIZE, cur_y))
        if self.is_valid_coordinate(block_coordinates=(cur_x, cur_y + BLOCKSIZE)):
            self.stack.append((cur_x, cur_y + BLOCKSIZE))
        if self.is_valid_coordinate(block_coordinates=(cur_x + BLOCKSIZE, cur_y)):
            self.stack.append((cur_x + BLOCKSIZE, cur_y))

        self.is_visited.add(self.current_coordinates)

        # change values within the map structure for colorizing.
        # if current position is start position, then it should not be colorized
        if self.current_coordinates == self.start_coordinates:
            pass
        else:
            self.map_structure.final_map[self.current_coordinates] = VISITED_BLOCK
