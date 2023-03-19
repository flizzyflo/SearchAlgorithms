import sys

from src.map_structure.map_structure import MapStructure
from src.search_algorithms.depth_first_search import Dfs
from src.user_interface.application_window import ApplicationWindow
from src.search_algorithms.breadth_first_search import Bfs


def initialize_program(desired_algorithm: str) -> ApplicationWindow:
    m = MapStructure(randomized_walls=False)

    if desired_algorithm == "b":
        search_algo = Bfs(map_structure=m)

    elif desired_algorithm == "d":
        search_algo = Dfs(map_structure=m)

    w = ApplicationWindow(block_map=m,
                          search_algorithm=search_algo)

    return w

if __name__ == '__main__':

    a = initialize_program("d")

    while True:

        if a.search_is_over():
            b = input("Again? (y/n) ")

            if b == "y":
                print("Select your algorithm: ")
                desired_algorithm = input("Bfs: b, Dfs: d ")
                while desired_algorithm not in ["b", "d"]:
                    print("Please enter a valid input.")
                    desired_algorithm = input("Bfs: b, Dfs: d ")
                a = initialize_program(desired_algorithm)

            elif b == "n":
                sys.exit()

        else:
            a.run()
