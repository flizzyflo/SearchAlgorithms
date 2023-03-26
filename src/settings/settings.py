from enum import Enum

RESOLUTION = WIDTH, HEIGHT = 600, 600

BLOCKSIZE: int = 10
FRAMERATE: int = 60
TITLE: str = "Search- & pathfinding algorithms visualized"


class BlockColors(Enum):
    black = 1  # background color
    white = 0  # empty block
    purple = 2  # start block
    red = 3  # destination block
    lightblue = 4  # visited block
    green = 5  # shortest path
    blue = 6  # selected block
    DARK_RED = 5
    yellow = 8  # current block


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
