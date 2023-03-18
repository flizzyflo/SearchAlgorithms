from queue import Queue



def breadth_first_search(*,
                         graph: dict[str | int, list[str | int]],
                         start_node: str | int,
                         destination_node: str | int) -> bool:

    """Uses Queue to go through graph. Graph should be passed in as adjacency list."""

    if destination_node not in graph.keys() or start_node not in graph.keys():
        return False

    queued_nodes = Queue()
    queued_nodes.put(start_node)  # insert the starting node into the queue to grab its neighbors during while loop
    visited_nodes = [start_node]  # keep track of the visited nodes

    while not queued_nodes.empty():
        # if queue is empty and not true is returned, there is no path between start and destination node

        current_node = queued_nodes.get()
        visited_nodes.append(current_node)

        if current_node == destination_node:
            return True

        for neighbor in graph[current_node]:
            # enque all neighbours of current node, since current node is not the destination node.
            # checking if nodes where visited, in this case enqueing does not happen.
            if neighbor not in visited_nodes:
                queued_nodes.put(neighbor)

    return False

