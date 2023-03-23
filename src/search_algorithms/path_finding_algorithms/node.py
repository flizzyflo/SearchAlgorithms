from dataclasses import dataclass
from typing import Self


class Node:

    all_nodes: dict[tuple[int, int], Self] = {}

    def __init__(self, *,
                 coordinates: tuple[int, int],
                 predecessor_coordinates: tuple[int, int] = None,
                 g_value: int = 0,
                 h_value: int = 0,
                 f_value: int = 0):

        self.coordinates: tuple[int, int] = coordinates
        self.predecessor_coordinates: tuple[int, int] = predecessor_coordinates
        self.g_value: int = g_value  # distance cost of node
        self.h_value: int = h_value  # heuristic estimated cost of node
        self.f_value: int = f_value  # total cost of node (g + h)
        self.enqueued: bool = False
        Node.all_nodes[self.coordinates] = self

    def get_coordinates(self) -> tuple[int, int]:
        return self.coordinates

    def get_predecessor_coordinates(self) -> tuple[int, int]:
        return self.predecessor_coordinates

    def set_predecessor_coordinates(self, predecessor_coordinates: tuple[int, int]) -> None:
        self.predecessor_coordinates = predecessor_coordinates

    def get_real_distance_travel_costs(self) -> int:
        return self.g_value

    def set_real_distance_travel_costs_to(self, g_value: int) -> None:
        self.g_value = g_value

    def get_heuristic_distance_travel_costs(self) -> int:
        return self.h_value

    def set_heuristic_travel_costs_to(self, h_value: int) -> None:
        self.h_value = h_value

    def set_total_travel_costs_to(self, f_value: int) -> None:
        self.f_value = f_value

    def __repr__(self):
        return f"{self.coordinates} -> {self.predecessor_coordinates}"

    def __eq__(self, other: Self) -> bool:
        return self.f_value == other.f_value

    def __lt__(self, other: Self) -> bool:
        return self.f_value < other.f_value

    def __le__(self, other: Self) -> bool:
        return self.f_value <= other.f_value

    def __gt__(self, other: Self) -> bool:
        return self.f_value > other.f_value

    def __ge__(self, other: Self) -> bool:
        return self.f_value >= other.f_value

    def __iter__(self):
        return iter(self.get_coordinates())
