from src.separated.Map.Map import Map
from src.separated.UserInterface.UserInterface import Window
from src.separated.search_algorithms.Bfs import Bfs

if __name__ == '__main__':

    m = Map()
    b = Bfs(map=m)

    w = Window(block_map=m,
               search_algorithm=b)

    while True:
        w.run()


