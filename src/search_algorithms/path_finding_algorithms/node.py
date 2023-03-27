from typing import Self


class Node:

    all_nodes: dict[tuple[int, int], Self] = {}

    def __init__(self, *,
                 coordinates: tuple[int, int],
                 predecessor_coordinates: tuple[int, int] = None,
                 successor_coordinates: tuple[int, int] = None,
                 real_distance: int = 0,
                 estimated_distance: int = 0,
                 total_distance: int = 0):

        self.coordinates: tuple[int, int] = coordinates
        self.x, self.y = self.coordinates
        self.predecessor_coordinates: tuple[int, int] = predecessor_coordinates
        self.successor_coordinates: tuple[int, int] = successor_coordinates
        self.real_distance: int = real_distance  # distance cost of node
        self.estimated_distance: int = estimated_distance  # heuristic estimated cost of node
        self.total_distance: int = total_distance  # total cost of node (g + h)
        self.enqueued: bool = False
        Node.all_nodes[self.coordinates] = self

    def get_coordinates(self) -> tuple[int, int]:
        return self.coordinates

    def get_predecessor_coordinates(self) -> tuple[int, int]:
        return self.predecessor_coordinates

    def set_predecessor_coordinates_to(self, predecessor_coordinates: tuple[int, int]) -> None:
        self.predecessor_coordinates = predecessor_coordinates

    def get_successor_coordinates(self) -> tuple[int, int]:
        return self.successor_coordinates

    def set_successor_coordinates_to(self, successor_coordinates: tuple[int, int]) -> None:
        self.successor_coordinates = successor_coordinates

    def get_real_distance_travel_costs(self) -> int:
        return self.real_distance

    def set_real_distance_travel_costs_to(self, g_value: int) -> None:
        self.real_distance = g_value

    def get_heuristic_distance_travel_costs(self) -> int:
        return self.estimated_distance

    def set_heuristic_travel_costs_to(self, h_value: int) -> None:
        self.estimated_distance = h_value

    def set_total_travel_costs_to(self, f_value: int) -> None:
        self.total_distance = f_value

    def __repr__(self):
        return f"{self.coordinates} -> {self.predecessor_coordinates}"

    def __eq__(self, other: Self) -> bool:
        return self.total_distance == other.total_distance

    def __lt__(self, other: Self) -> bool:
        return self.total_distance < other.total_distance

    def __le__(self, other: Self) -> bool:
        return self.total_distance <= other.total_distance

    def __gt__(self, other: Self) -> bool:
        return self.total_distance > other.total_distance

    def __ge__(self, other: Self) -> bool:
        return self.total_distance >= other.total_distance

    def __iter__(self):
        return iter(self.get_coordinates())
