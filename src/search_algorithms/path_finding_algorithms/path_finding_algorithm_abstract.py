from src.map_structure.map_structure import MapStructure
from src.search_algorithms.search_algorithm_abstract_base_class import SearchAlgorithm
from abc import ABC, abstractmethod


class PathfindingAlgorithm(SearchAlgorithm, ABC):
    def __init__(self, map_structure: MapStructure) -> None:
        super().__init__(map_structure= map_structure)

    @abstractmethod
    def perform_search(self) -> None:
        pass

    @abstractmethod
    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]) -> None:
        pass

