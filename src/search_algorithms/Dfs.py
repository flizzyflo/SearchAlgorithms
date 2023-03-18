from src.search_algorithms.Algorithms_ABC import Algorithms


class Dfs(Algorithms):

    def is_wall(self, block_coordinates) -> bool:
        pass

    def is_valid_coordinate(self, block_coordinates) -> bool:
        pass

    def is_in_bounds(self, block_coordinates) -> bool:
        pass

    def no_way_exists(self) -> bool:
        pass

    def search_is_over(self) -> bool:
        pass

    def goal_detected(self, block_coordinates: tuple[int, int]) -> bool:
        pass

    def initialize_goal_coordinates(self, goal_coordinates: tuple[int, int]):
        pass

    def initialize_start_coordinates(self, start_coordinates: tuple[int, int]):
        pass

    def get_current_coordinates(self):
        pass

    def perform_search(self) -> None:
        pass

    ...