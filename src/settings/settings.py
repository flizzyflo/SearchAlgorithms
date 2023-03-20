RESOLUTION = WIDTH, HEIGHT = 700, 700

BLOCKSIZE: int = 5
FRAMERATE: int = 60
TITLE: str = "Search Algos Visualized"

WALL_COLOR: str = "white"
START_COLOR: str = "blue"
GOAL_COLOR: str = "red"
EMPTY_COLOR: str = "white"
VISITED_COLOR: str = "lightblue"
BACKGROUND_COLOR: str = "black"

WALL_BLOCK: int = 1
EMPTY_BLOCK: int = 0
START_BLOCK: int = 2
END_BLOCK: int = 3
VISITED_BLOCK: int = 4

INFORMATION_FRAME_TEXT="""User-Manual:
\n1. Select the screen size or stick with default values.
\n2. Select the  search-algorithm
\n3. Select randomized walls or not
\n4. Initialize the program. When changing things before starting, you need to re-initialize.
\n5. Click 'Start' button. New window appears containing the program itself.
\n ------- You started the program, all information below are relevant for the search-algorithm window -------
\n6. Right mouse button: Set both, start (blue) and destination(red). Both are required to start.
\n7. Left mouse button: Add additional or delete existing walls.
\n8. Click any button on your keyboard to start the search algorithm."""
