from src.map_structure.map_structure import MapStructure
from src.search_algorithms.path_finding_algorithms.path_finding_algorithm_abstract import PathfindingAlgorithm


class Djikstra(PathfindingAlgorithm):

    def __init__(self, map_structure: MapStructure) -> None:
        super().__init__(map_structure=map_structure)

    def perform_search(self) -> None:
        pass

    def initialize_destination_coordinates(self, goal_coordinates: tuple[int, int]) -> None:
        pass

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]) -> None:
        pass

