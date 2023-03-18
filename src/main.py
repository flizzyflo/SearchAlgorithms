from src.Map.Map import Map
from src.UserInterface.UserInterface import Window
from src.search_algorithms.Bfs import Bfs

if __name__ == '__main__':

    m = Map()
    b = Bfs(map=m)

    w = Window(block_map=m,
               search_algorithm=b)

    while True:
        w.run()


