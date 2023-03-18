

islands = [["W", "W", "L", "W", "W"],
           ["W", "L", "L", "L", "W"],
           ["W", "W", "L", "W", "W"],
           ["L", "W", "W", "L", "L"],
           ["W", "L", "L", "W", "W"]]

islands = [["W", "W", "W", "W", "W", "W", "W", "W"],
           ["W", "L", "L", "L", "L", "L", "L", "W"],
           ["W", "W", "W", "W", "W", "W", "W", "W"],
           ["L", "W", "W", "L", "L", "W", "W", "W"],
           ["W", "L", "L", "W", "W", "W", "W", "W"],
           ["W", "W", "W", "W", "W", "W", "W", "W"],
           ["W", "W", "W", "W", "L", "L", "W", "W"],
           ["W", "W", "W", "W", "W", "W", "W", "W"]]


def get_island_size(graph: list[list[str]], get_max_island: bool = True) -> int:
    
    islands: list[set[str]] = [ ]

    for row in range(len(graph)):
        for column in range(len(graph[0])):

            visited_set: set[str] = set()
            explore_island(graph= graph, 
                           row= row,
                           column= column,
                           visited_nodes = visited_set)

            if len(visited_set) > 0:
                islands.append(visited_set)
    
    if get_max_island:
        return len(max(islands, key= len))
    
    else:
        return len(min(islands, key= len))


def explore_island(graph: list[list[str]], row: int, column: int, visited_nodes: set[str, str]) -> None:
    
    """Explores the island. Checks adjacent positions of the current position."""

    current_node = f"{row}, {column}"
    if current_node in visited_nodes:
        return

    elif is_out_of_bounds(graph= graph, 
                          position= row):
        return
    
    elif is_out_of_bounds(graph= graph, 
                          position= column):
        return

    elif is_water(graph= graph, 
                  row= row, 
                  column= column):
        # no land
        return

    visited_nodes.add(current_node)

    explore_island(graph= graph, row= row + 1, column= column, visited_nodes= visited_nodes)
    explore_island(graph= graph, row= row - 1, column= column, visited_nodes= visited_nodes)
    explore_island(graph= graph, row= row, column= column + 1, visited_nodes= visited_nodes)
    explore_island(graph= graph, row= row, column= column - 1, visited_nodes= visited_nodes)

    return


def is_out_of_bounds(graph: list[list[str]], position: int) -> bool:
    
    """Checks whether a position is out of bounds of the island graph. Returns True if is out of bounds, false else."""
    
    return position < 0 or position >= len(graph) 


def is_water(graph: list[list[str]], row: int, column: int) -> bool:
    
    """Checks whether the current position of row x column is water and returns true or false if it is land."""
    
    return graph[row][column] == "W"


print(get_island_size(graph= islands, get_max_island= True))