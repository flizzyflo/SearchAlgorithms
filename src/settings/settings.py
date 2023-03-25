RESOLUTION = WIDTH, HEIGHT = 600, 600

BLOCKSIZE: int = 10
FRAMERATE: int = 60
TITLE: str = "Search- & pathfinding algorithms visualized"

WALL_BORDER_COLOR: str = "white"
START_COLOR: str = "orange"
GOAL_COLOR: str = "red"
EMPTY_COLOR: str = "white"
VISITED_COLOR: str = "lightblue"
BACKGROUND_COLOR: str = "black"  # wall color as well, since walls are small squaires which are transparent
SHORTEST_PATH_COLOR: str = "green"
SELECTED_BLOCK_COLOR: str = "blue"

WALL_BLOCK: int = 1
EMPTY_BLOCK: int = 0
START_BLOCK: int = 2
DESTINATION_BLOCK: int = 3
VISITED_BLOCK: int = 4
SHORTEST_PATH: int = 5
SELECTED_BLOCK: int = 6

INFORMATION_FRAME_TEXT = """User-Manual:
\n1. Set screen size
\n2. Select algorithm
\n3. Disable/enable randomized walls
\n4. Initialize the program. Reinitialize when something is changed before start
\n5. 'Start' - New window appears containing the program itself.
\n\n ------- Controls -------
\n6. Right mouse button: Set both start (blue) and destination (red). Both are required to start. Clicking the same
block again removes the block
\n7. Left mouse button: Add additional wall. Clicking an existing wall will remove it.
\n8. Press enter to start"""
