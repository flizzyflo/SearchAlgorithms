
def depth_first_search(graph: dict[str|int, list[str|int]], start_node: str|int, destination_node: str|int) -> bool:

    """Depth first search uses a stack to implement the search algorithm. Every neighbour of the current node
    will be pushed to the stack. If the current node is node the destination node, the topmost stack element 
    is looked at and the process repeats for that stack element. This is solved in iterative way."""

    stack = [start_node]
    visited_nodes = [start_node]

    if destination_node not in graph.keys() or start_node not in graph.keys():
        return False

    while len(stack) > 0:

        current_node = stack.pop()
        
        if current_node == destination_node:
            return True

        # every neighbor is put on top of the stack if it was not already visited.
        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                stack.append(neighbor)

    # Stack is empty, destination node not found. Return False    
    return False


global visited
visited: set[str|int] = set()

def depth_first_search_rec(graph: dict[str|int, list[str|int]], src: int|str, dst: int|str) -> bool:
    
    """Depth first search uses a stack to implement the search algorithm. Every neighbour of the current node
    will be pushed to the stack. If the current node is node the destination node, the topmost stack element 
    is looked at and the process repeats for that stack element. This is solved in recursive way."""
    
    # visited set to track the visited nodes and avoid infinite loops
    global visited

    # recursive base case
    if src == dst:
        return True
    
    for neighbor in graph[src]:

        # neighbor is visited, so retrun false, since all its neighbors are visited as well
        if neighbor in visited:
            return False

        visited.add(neighbor)

        if depth_first_search_rec(graph, neighbor, dst):
            return True
    
    # destination node not found.
    return False

  