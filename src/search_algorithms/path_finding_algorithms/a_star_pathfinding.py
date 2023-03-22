from src.map_structure.map_structure import MapStructure
from src.search_algorithms.path_finding_algorithms.path_finding_algorithm_abstract import PathfindingAlgorithm
from src.search_algorithms.path_finding_algorithms.node import Node
from queue import PriorityQueue
import time

from src.settings.settings import VISITED_BLOCK, BLOCKSIZE, SHORTEST_PATH


class AStarPathfinding(PathfindingAlgorithm):

    def __init__(self, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)
        self.open_list: PriorityQueue = PriorityQueue() # store node and f-value in ordered way
        # closed list is stored in 'is visited' set

    def perform_search(self) -> None:

        if self.open_list.empty():
            self.no_way_found = True

        current_node: Node = self.open_list.get()
        current_block_x, current_block_y = current_node.coordinates
        self.current_coordinates = (current_block_x, current_block_y)

        # invalid block
        if not self.is_valid_coordinate(block_coordinates=self.current_coordinates):
            return

        # case current block is destination block
        if self.is_destination(block_coordinates=self.current_coordinates):
            self.destination_detected = True
            return

        # case block was already visited, skip this block
        if self.already_visited_block(block_coordinates=self.current_coordinates):
            return

        # current block is set as visited
        self.visited_this_block(block_coordinates=self.current_coordinates)

        if self.is_valid_coordinate(block_coordinates=(current_block_x + BLOCKSIZE, current_block_y)):
            self.expand_node(successor_coordinates=(current_block_x + BLOCKSIZE, current_block_y))

        if self.is_valid_coordinate(block_coordinates=(current_block_x - BLOCKSIZE, current_block_y)):
            self.expand_node(successor_coordinates=(current_block_x - BLOCKSIZE, current_block_y))

        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y - BLOCKSIZE)):
            self.expand_node(successor_coordinates=(current_block_x, current_block_y - BLOCKSIZE))

        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y + BLOCKSIZE)):
            self.expand_node(successor_coordinates=(current_block_x, current_block_y + BLOCKSIZE))

        current_node.enqueued = True

        # colorization of blocks as visited, but keeping the start block in its color
        if self.current_coordinates == self.start_coordinates:
            pass

        else:
            self.map_structure.final_map[self.current_coordinates] = VISITED_BLOCK

    def expand_node(self, successor_coordinates: tuple[int, int]) -> None:

        time.sleep(0.00)
        # successor node already visited, skip ('closed list')
        if self.already_visited_block(block_coordinates=successor_coordinates):
            return

        successor_node = Node(coordinates=successor_coordinates,
                              predecessor_coordinates=self.current_coordinates,
                              g_value=Node.all_nodes[self.current_coordinates].get_g_value() + 1,
                              h_value=self.get_heuristic_distance(successor_coordinates=successor_coordinates))

        temp_g = Node.all_nodes[self.current_coordinates].get_g_value() + 1

        # successor is visited and distance value from this current coordinate is higher than distnace already stored
        if successor_node.enqueued and temp_g > successor_node.get_g_value():
            return

        successor_node.set_predecessor_coordinates(predecessor_coordinates=self.current_coordinates)
        successor_node.set_g_value(g_value=temp_g)

        # f_val is total cost of track
        f_val = temp_g + self.get_heuristic_distance(successor_coordinates=successor_coordinates)
        #successor_node.set_f_val_to(f_value=f_val)

        if successor_node in self.open_list.queue:
            successor_node.set_f_val_to(f_value=f_val)
        else:
            successor_node.set_f_val_to(f_value=f_val)
            self.open_list.put(successor_node)

        successor_node.enqueued = True

    def get_heuristic_distance(self, successor_coordinates: tuple[int, int]) -> int:

        # same x position, difference in y is the heuristic
        if successor_coordinates[0] == self.destination_coordinates[0]:
            return abs(self.destination_coordinates[1] - successor_coordinates[1])

        # same y position, difference in x is the heuristic
        elif successor_coordinates[1] == self.destination_coordinates[1]:
            return abs(self.destination_coordinates[0] - successor_coordinates[0])

        # heuristic needed, calculate side length with pythagoras
        else:
            return self.calculate_pythagoras(a=(successor_coordinates[0] - self.destination_coordinates[0]) ** 2,
                                             b=(successor_coordinates[1] - self.destination_coordinates[1]) ** 2)

    def calculate_pythagoras(self, a: int, b: int) -> int:
        return int((a + b) ** 0.5)

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]) -> None:
        start_node = Node(coordinates=start_coordinates,
                          predecessor_coordinates=None,
                          g_value=0,
                          h_value=0,
                          f_value=0)
        self.open_list.put(start_node)
        start_node.enqueued = True
        self.start_coordinates = start_node.coordinates

    def backtrack_from_destination_to_start(self, current_coordinates: tuple[int, int], node_list: list = list()) -> list[tuple[int, int]]:
        node_list.append(current_coordinates)
        while True:

            if Node.all_nodes[current_coordinates].get_predecessor_coordinates() is None:
                return node_list

            return self.backtrack_from_destination_to_start(current_coordinates=Node.all_nodes[current_coordinates].get_predecessor_coordinates(),
                                                            node_list=node_list)

    def paint_blocks(self, blocks_to_be_painted: list[tuple[int, int]]):
        for block in blocks_to_be_painted:
            self.map_structure.final_map[block] = SHORTEST_PATH
