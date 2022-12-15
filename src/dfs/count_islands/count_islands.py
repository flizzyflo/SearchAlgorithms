
islands = [["W", "W", "L", "W", "W"],
           ["W", "L", "L", "L", "W"],
           ["W", "W", "W", "W", "W"],
           ["L", "W", "W", "L", "W"],
           ["W", "L", "L", "W", "W"]]


def get_island_count(graph: list[list[str]], sign_land: str) -> int:
    
    """Counts the amount of islands within the graph passed in as an argument."""
    
    visited_set = set()
    island_counter = 0
    for row in range(len(graph)):
        for column in range(len(graph[0])):
            
            if explore_island(graph, row, column, visited_set, sign_land) == True:
                island_counter += 1
               
    return island_counter


def explore_island(graph: list[list[str]], start_row: int, start_col: int, visited_set: set[str], sign_land: str) -> bool:

    """Explores the island as soon a an position with L is found. Ensures, that connected islands are 
    just counted once, since it sets all related nodes, which are land, to visited.
    Returns true if an island is unvisited and land, false if it was already visited"""

    if is_out_of_bounds(graph, start_row):  
        # checks for being within the bounds of the graph for the recursive call with different row.
        return False

    if is_out_of_bounds(graph, start_col):  
        # checks for being within the bounds of the graph for the recursive call with different col.
        return False

    if not is_land(graph, start_row, start_col, sign_land): 
        # checks if the current node passed in as argument is land.
        return False

    current_node_position = f"{start_row},{start_col}" 
    # forms an position-string to be compared and/or placed within the "is visited set"

    if is_visited(current_node_position, visited_set): 
        # checks if the current node was already visited. this means it and all of its adjacent land nodes have been already counted as island
        return False

    visited_set.add(f"{start_row},{start_col}")

    # recursive calls for the adjacent nodes arround the current node
    explore_island(graph, start_row + 1, start_col, visited_set, sign_land)
    explore_island(graph, start_row - 1, start_col, visited_set, sign_land)
    explore_island(graph, start_row, start_col + 1, visited_set, sign_land)
    explore_island(graph, start_row, start_col - 1, visited_set, sign_land)

    return True


def is_visited(node_position: str, visited_set: set[str]) -> bool:
    
    """Checks whether the node passed in as argument is already visited or not.
    Therefore, it checks if the node is present within the visited set."""
    
    return node_position in visited_set


def is_land(graph: list[list[str]], row: int, col: int, sign_land: str) -> bool:
    
    """Checks whether the node passed in as argument is concidered land or not.
    Therefore, it checks if the node value equals the sign for being land."""
    
    return graph[row][col] == sign_land


def is_out_of_bounds(graph: list[list[str]], positional_value: int) -> bool:
    
    """Checks whether the node passed in as argument is in bound of the graph or not."""
    
    return positional_value < 0 or positional_value >= len(graph)



print(get_island_count(islands,"L"))