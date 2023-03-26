from src.map_structure.map_structure import MapStructure
from src.search_algorithms.path_finding_algorithms.path_finding_algorithm_abstract import PathfindingAlgorithm
from src.search_algorithms.path_finding_algorithms.node import Node
from queue import PriorityQueue

from src.settings.settings import BlockColors


class AStarPathfinding(PathfindingAlgorithm):

    """
    Class to find path between two points using the A* algorithm.
    """

    def __init__(self, *, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)

        # store node and f-value in ordered way, minimum value first
        self.open_list: PriorityQueue = PriorityQueue()
        # closed list is stored in 'is visited' set (is inherited)

    def get_next_block(self) -> tuple[int, int] | Node:
        return self.open_list.get()

    def perform_search(self, next_block: tuple[int, int] | Node) -> None:

        if self.open_list.empty():
            self.no_way_found = True

        current_node: Node = next_block
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

        # grab right neighbour
        if self.is_valid_coordinate(block_coordinates=(current_block_x + self.blocksize, current_block_y)):
            neighbour_block = (current_block_x + self.blocksize, current_block_y)

            if not self.already_visited_block(block_coordinates=neighbour_block) and (neighbour_block != self.destination_coordinates):
                self.map_structure.final_map[neighbour_block] = BlockColors.blue.value

            self.evaluate_successor_node(successor_coordinates=neighbour_block)

        # grab left neighbour
        if self.is_valid_coordinate(block_coordinates=(current_block_x - self.blocksize, current_block_y)):
            neighbour_block = (current_block_x - self.blocksize, current_block_y)

            if not self.already_visited_block(block_coordinates=neighbour_block) and (neighbour_block != self.destination_coordinates):
                self.map_structure.final_map[neighbour_block] = BlockColors.blue.value

            self.evaluate_successor_node(successor_coordinates=neighbour_block)

        # grab lower neighbour
        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y - self.blocksize)):
            neighbour_block = (current_block_x, current_block_y - self.blocksize)

            if not self.already_visited_block(block_coordinates=neighbour_block) and (neighbour_block != self.destination_coordinates):
                self.map_structure.final_map[neighbour_block] = BlockColors.blue.value

            self.evaluate_successor_node(successor_coordinates=neighbour_block)

        # grab upper neighbour
        if self.is_valid_coordinate(block_coordinates=(current_block_x, current_block_y + self.blocksize)):
            neighbour_block = (current_block_x, current_block_y + self.blocksize)

            if not self.already_visited_block(block_coordinates=neighbour_block) and (neighbour_block != self.destination_coordinates):
                self.map_structure.final_map[neighbour_block] = BlockColors.blue.value

            self.evaluate_successor_node(successor_coordinates=neighbour_block)

        current_node.enqueued = True

        # colorization of blocks as visited, but keeping the start block in its color
        if self.current_coordinates == self.start_coordinates:
            pass

        else:
            self.map_structure.final_map[self.current_coordinates] = BlockColors.lightblue.value

    def evaluate_successor_node(self, successor_coordinates: tuple[int, int]) -> None:

        # successor node passed in as argument already visited, skip node (stored in 'closed list')
        if self.already_visited_block(block_coordinates=successor_coordinates):
            return

        # create successor node object, keeping track of the coordinates and predecessor coordinates
        successor_node = Node(coordinates=successor_coordinates,
                              predecessor_coordinates=self.current_coordinates)

        # calculate costs for distance from current node to successor node
        real_distance_travel_costs = Node.all_nodes[self.current_coordinates].get_real_distance_travel_costs() + 1

        # successor is visited and distance value stored
        # from current coordinate is higher than distance already stored, pass this and keep
        # already stored value, since it is shorter
        if successor_node.enqueued and real_distance_travel_costs >= successor_node.get_real_distance_travel_costs():
            return

        # set up real_distance_travel_cost from current node to successor node
        successor_node.set_real_distance_travel_costs_to(g_value=real_distance_travel_costs)

        # calculate estimated distance from successor node to destination node based on heuristic
        heuristic_travel_costs = self.calculate_heuristic_distance(successor_coordinates=successor_coordinates)
        successor_node.set_heuristic_travel_costs_to(h_value=heuristic_travel_costs)

        # sum up real costs from current node to successor and estimated cost from successor to destination
        total_travel_cost = real_distance_travel_costs + heuristic_travel_costs

        # successor node is already stored in open list, but total travel costs need to be updated
        # better path is found for this block
        if successor_node in self.open_list.queue:
            successor_node.set_total_travel_costs_to(f_value=total_travel_cost)

        else:
            # node not listed, insert it into list
            successor_node.set_total_travel_costs_to(f_value=total_travel_cost)
            self.open_list.put(successor_node)

        # store information about being enqueued
        successor_node.enqueued = True

    def calculate_heuristic_distance(self, successor_coordinates: tuple[int, int]) -> int:

        # same x position, difference in y is the heuristic
        if successor_coordinates[0] == self.destination_coordinates[0]:
            return abs(self.destination_coordinates[1] - successor_coordinates[1])

        # same y position, difference in x is the heuristic
        elif successor_coordinates[1] == self.destination_coordinates[1]:
            return abs(self.destination_coordinates[0] - successor_coordinates[0])

        # heuristic needed, calculate side length with pythagoras as approximation for distance
        else:
            return self.calculate_pythagoras(a=(successor_coordinates[0] - self.destination_coordinates[0]),
                                             b=(successor_coordinates[1] - self.destination_coordinates[1]))

    def calculate_pythagoras(self, a: int, b: int) -> int:
        a: int = a ** 2
        b: int = b ** 2
        return int((a + b) ** 0.5)

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]) -> None:

        start_node = Node(coordinates=start_coordinates,
                          predecessor_coordinates=None)

        self.open_list.put(start_node)
        self.start_coordinates = start_node.coordinates
        start_node.enqueued = True

    def backtrack_path(self, current_coordinates: tuple[int, int], node_list: list = list()) -> list[tuple[int, int]]:

        node_list.append(current_coordinates)

        # checks if current node is starting node, which has no predecessor. thus, backtracking is finished, return list
        if Node.all_nodes[current_coordinates].get_predecessor_coordinates() is None:
            return node_list

        return self.backtrack_path(current_coordinates=Node.all_nodes[current_coordinates].get_predecessor_coordinates(),
                                   node_list=node_list)
