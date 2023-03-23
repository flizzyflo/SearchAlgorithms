RESOLUTION = WIDTH, HEIGHT = 800, 800

BLOCKSIZE: int = 8
FRAMERATE: int = 60
TITLE: str = "Search Algos Visualized"

WALL_COLOR: str = "white"
START_COLOR: str = "blue"
GOAL_COLOR: str = "red"
EMPTY_COLOR: str = "white"
VISITED_COLOR: str = "lightblue"
BACKGROUND_COLOR: str = "black"
SHORTEST_PATH_COLOR: str = "lightgreen"

WALL_BLOCK: int = 1
EMPTY_BLOCK: int = 0
START_BLOCK: int = 2
DESTINATION_BLOCK: int = 3
VISITED_BLOCK: int = 4
SHORTEST_PATH: int = 5

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
