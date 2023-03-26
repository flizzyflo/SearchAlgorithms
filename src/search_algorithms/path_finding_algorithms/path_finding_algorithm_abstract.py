from src.map_structure.map_structure import MapStructure
from src.search_algorithms.search_algorithm_abstract_base_class import SearchAlgorithm
from abc import ABC, abstractmethod


class PathfindingAlgorithm(SearchAlgorithm, ABC):
    def __init__(self, *, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)

    @abstractmethod
    def backtrack_path(self, current_coordinates: tuple[int, int], node_list: list = list()) -> list[tuple[int, int]]:
        pass
