import pygame as pg
import pygame.time

from src.map_structure.map_structure import MapStructure
from src.search_algorithms.depth_first_search import Dfs
from src.search_algorithms.search_algorithm_abstract_base_class import SearchAlgorithm
from src.settings.settings import FRAMERATE, TITLE, BlockColors


class ApplicationWindow:
    def __init__(self, *, width: int, height: int, search_algorithm: SearchAlgorithm, block_map: MapStructure):
        pg.init()

        self.width, self.height = width, height
        self.resolution = (self.width, self.height)
        self.screen: pygame.Surface = pg.display.set_mode(self.resolution)
        self.block_map = block_map
        self.block_map.surface = self.screen
        self.is_dragging: bool = False
        self.search_algorithm: SearchAlgorithm = search_algorithm
        self.search_started: bool = False
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.clock.tick(FRAMERATE)
        self.algorithm_initialized: bool = False
        self.no_way: bool = self.search_algorithm.no_way_exists()
        self.start_block_set: bool = False
        self.start_and_end_block_set: bool = False
        self.blocksize: int = self.block_map.get_blocksize()

        pygame.display.set_caption(TITLE)

    def search_is_over(self) -> bool:
        return self.search_algorithm.search_is_over()

    def draw(self):

        self.screen.fill(color=BlockColors.black.value)

        for position in self.block_map.final_map:
            block_value = self.block_map.final_map[position]

            # wall element
            if block_value == BlockColors.black.value:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], self.blocksize, self.blocksize),
                                        color=BlockColors.white.name,
                                        width=1)

            # start element
            elif block_value == BlockColors.purple.value:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], self.blocksize, self.blocksize),
                                        color=BlockColors.purple.name,
                                        border_radius=1)

            # empty element
            elif block_value == BlockColors.white.value:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], self.blocksize, self.blocksize),
                                        color=BlockColors.white.name)

            # goal value
            elif block_value == BlockColors.red.value:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], self.blocksize, self.blocksize),
                                        color=BlockColors.red.name)

            # visited element
            elif block_value == BlockColors.lightblue.value:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], self.blocksize, self.blocksize),
                                        color=BlockColors.lightblue.name)

            # selected block for next search iteration, stored in datastructure
            elif block_value == BlockColors.blue.value:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], self.blocksize, self.blocksize),
                                        color=BlockColors.blue.name)

            # current visited block, which is investigated
            elif block_value == BlockColors.yellow.value:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], self.blocksize, self.blocksize),
                                        color=BlockColors.yellow.name)

            # turn all blocks red in case no way exists
            elif block_value == BlockColors.DARK_RED.value:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], self.blocksize, self.blocksize),
                                        color=BlockColors.DARK_RED.name)

            # paint the shortest path blocks
            elif self.search_algorithm.destination_detected and block_value == BlockColors.green.value:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], self.blocksize, self.blocksize),
                                        color=BlockColors.green.name)

        # store rectangle-objects per coordinate; not necessary right now
        self.block_map.all_rectangles[(position[0], position[1])] = rect

    def check_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()

            if event.type == pg.KEYDOWN:
                self.search_started = True

            # left click for setting a wall
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.is_dragging = True
                x, y = pg.mouse.get_pos()
                x = (x // self.blocksize) * self.blocksize
                y = (y // self.blocksize) * self.blocksize
                clicked_block = self.block_map.final_map[(x, y)]

                # clicked block is wall, destroy wall
                if clicked_block == BlockColors.black.value:
                    self.block_map.final_map[(x, y)] = BlockColors.white.value

                # clicked block is already declared as start block, turn it into wall
                elif clicked_block == BlockColors.purple.value:
                    self.start_block_set = False
                    self.start_and_end_block_set = False
                    self.block_map.final_map[(x, y)] = BlockColors.black.value

                # clicked block is declared as end block, turn it into wall
                elif clicked_block == BlockColors.red.value:
                    self.start_and_end_block_set = False
                    self.block_map.final_map[(x, y)] = BlockColors.black.value

                # empty block
                else:
                    self.block_map.final_map[(x, y)] = BlockColors.black.value

            # relevant for dragging mouse. checks if mousebutton is released
            if event.type == pg.MOUSEBUTTONUP:
                self.is_dragging = False

            # if mousebutton is dragging
            if event.type == pg.MOUSEMOTION and self.is_dragging:

                x, y = pg.mouse.get_pos()
                # normalize click position to fit the coordinate keys
                x = (x // self.blocksize) * self.blocksize
                y = (y // self.blocksize) * self.blocksize
                clicked_block = self.block_map.final_map[(x, y)]

                # clicked block is wall pass in dragging mode
                if clicked_block == BlockColors.black.value:
                    pass

                # clicked block is already declared as start / goal block, turn it into wall
                elif clicked_block == BlockColors.purple.value:
                    self.start_block_set = False
                    self.start_and_end_block_set = False
                    self.block_map.final_map[(x, y)] = BlockColors.black.value

                # clicked block is declared as end block
                elif clicked_block == BlockColors.red.value:
                    self.start_and_end_block_set = False
                    self.block_map.final_map[(x, y)] = BlockColors.black.value

                # empty block, set up wall
                else:
                    self.block_map.final_map[(x, y)] = BlockColors.black.value

            # right click to set start and end point
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                x, y = pg.mouse.get_pos()
                # normalize click position to fit the coordinate keys
                x = (x // self.blocksize) * self.blocksize
                y = (y // self.blocksize) * self.blocksize
                clicked_block = self.block_map.final_map[(x, y)]

                # clicked block is declared as start block and will be turned into empty block
                if clicked_block == BlockColors.purple.value:
                    self.block_map.final_map[(x, y)] = BlockColors.white.value
                    self.start_block_set = False

                # no start block is set
                elif clicked_block == BlockColors.white.value and not self.start_block_set:
                    self.block_map.final_map[(x, y)] = BlockColors.purple.value
                    self.start_block_set = True

                # clicked block is empty block, start block is declared and end block is missing
                elif clicked_block == BlockColors.white.value and self.start_block_set and not self.start_and_end_block_set:
                    self.block_map.final_map[(x, y)] = BlockColors.red.value
                    self.start_and_end_block_set = True

                # clicked block is declared as end block
                elif clicked_block == BlockColors.red.value:
                    self.block_map.final_map[(x, y)] = BlockColors.white.value
                    self.start_and_end_block_set = False

    def update(self) -> None:
        pg.display.update()
        self.check_events()
        self.draw()

    def run(self) -> None:

        self.update()

        if self.search_started and not self.algorithm_initialized:
            start, end = self.block_map.get_start_destination_points()
            self.search_algorithm.initialize_start_coordinates(start)
            self.search_algorithm.initialize_destination_coordinates(end)
            if isinstance(self.search_algorithm, Dfs):
                next_block = None
            else:
                next_block = self.search_algorithm.get_next_block()
            self.search_algorithm.perform_search(next_block=next_block)
            self.algorithm_initialized = True

        elif self.algorithm_initialized:
            next_block = self.search_algorithm.get_next_block()
            self.search_algorithm.perform_search(next_block= next_block)

    def show_no_way(self) -> None:
        self.block_map.end_search_bc_no_way()
