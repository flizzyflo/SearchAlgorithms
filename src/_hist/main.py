from src._hist.bfs.breadth_first_search import breadth_first_search
from src._hist.dfs.depth_first_search import depth_first_search, depth_first_search_rec

graph = {
        "a": ["b", "c"],
        "b": ["a", "d"],
        "c": ["a"],
        "d": ["e"],
        "e": [],
        "f": ["b"]
        }

print(breadth_first_search(graph= graph, 
                           start_node= "a", 
                           destination_node= "e"))

print(depth_first_search(graph= graph, 
                         start_node= "a", 
                         destination_node= "e"))


print(depth_first_search_rec(graph, "a", "e"))