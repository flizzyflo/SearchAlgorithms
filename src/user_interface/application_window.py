import sys

import pygame as pg
import pygame.time

from src.map_structure.map_structure import MapStructure
from src.settings.settings import BLOCKSIZE, START_BLOCK, START_COLOR, VISITED_BLOCK, VISITED_COLOR, FRAMERATE, TITLE, \
    BACKGROUND_COLOR, WALL_COLOR, EMPTY_COLOR, EMPTY_BLOCK, END_BLOCK, GOAL_COLOR, WALL_BLOCK
from src.search_algorithms.algorithms_abstract_base_class import Algorithm


class ApplicationWindow:
    def __init__(self, *, width: int, height: int, search_algorithm: Algorithm, block_map: MapStructure):
        pg.init()

        self.width, self.height = width, height
        self.resolution = (self.width, self.height)
        self.screen: pygame.Surface = pg.display.set_mode(self.resolution)
        self.block_map = block_map
        self.block_map.surface = self.screen
        self.is_dragging: bool = False
        self.search_algorithm: Algorithm = search_algorithm
        self.search_started: bool = False
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.clock.tick(FRAMERATE)
        self.algorithm_initialized: bool = False
        self.found: bool = False
        self.no_way: bool = self.search_algorithm.no_way_exists()
        self.start_block_set: bool = False
        self.start_and_end_block_set: bool = False

        pygame.display.set_caption(TITLE)

    def search_is_over(self) -> bool:
        return self.search_algorithm.search_is_over()

    def draw(self):
        self.screen.fill(color=BACKGROUND_COLOR)

        for position in self.block_map.final_map:
            map_value = self.block_map.final_map[position]

            # wall element
            if map_value == WALL_BLOCK:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], BLOCKSIZE, BLOCKSIZE),
                                        color=WALL_COLOR,
                                        width=1)

            # start element
            elif map_value == START_BLOCK:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], BLOCKSIZE, BLOCKSIZE),
                                        color=START_COLOR,
                                        border_radius=1)

            # empty element
            elif map_value == EMPTY_BLOCK:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], BLOCKSIZE, BLOCKSIZE),
                                        color=EMPTY_COLOR)

            # goal value
            elif map_value == END_BLOCK:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], BLOCKSIZE, BLOCKSIZE),
                                        color=GOAL_COLOR)

            # visited element
            elif map_value == VISITED_BLOCK:
                rect = pygame.draw.rect(surface=self.screen,
                                        rect=(position[0], position[1], BLOCKSIZE, BLOCKSIZE),
                                        color=VISITED_COLOR)

            self.block_map.all_rectangles[(position[0], position[1])] = rect

    def check_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                self.search_started = True

            # left click for setting a wall
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.is_dragging = True
                x, y = pg.mouse.get_pos()
                x = (x // BLOCKSIZE) * BLOCKSIZE
                y = (y // BLOCKSIZE) * BLOCKSIZE
                clicked_block = self.block_map.final_map[(x, y)]

                # clicked block is wall, destroy wall
                if clicked_block == WALL_BLOCK:
                    self.block_map.final_map[(x, y)] = EMPTY_BLOCK

                # clicked block is already declared as start block, turn it into wall
                elif clicked_block == START_BLOCK:
                    self.start_block_set = False
                    self.start_and_end_block_set = False
                    self.block_map.final_map[(x, y)] = WALL_BLOCK

                # clicked block is declared as end block, turn it into wall
                elif clicked_block == END_BLOCK:
                    self.start_and_end_block_set = False
                    self.block_map.final_map[(x, y)] = WALL_BLOCK

                # empty block
                else:
                    self.block_map.final_map[(x, y)] = WALL_BLOCK

            # relevant for dragging mouse. checks if mousebutton is released
            if event.type == pg.MOUSEBUTTONUP:
                self.is_dragging = False

            # if mousebutton is dragging
            if event.type == pg.MOUSEMOTION and self.is_dragging:
                x, y = pg.mouse.get_pos()
                x = (x // BLOCKSIZE) * BLOCKSIZE
                y = (y // BLOCKSIZE) * BLOCKSIZE
                clicked_block = self.block_map.final_map[(x, y)]

                # clicked block is wall pass in dragging mode
                if clicked_block == WALL_BLOCK:
                    pass

                # clicked block is already declared as start / goal block, turn it into wall
                elif clicked_block == START_BLOCK:
                    self.start_block_set = False
                    self.start_and_end_block_set = False
                    self.block_map.final_map[(x, y)] = WALL_BLOCK

                # clicked block is declared as end block
                elif clicked_block == END_BLOCK:
                    self.start_and_end_block_set = False
                    self.block_map.final_map[(x, y)] = WALL_BLOCK

                # empty block, set up wall
                else:
                    self.block_map.final_map[(x, y)] = WALL_BLOCK

            # right click to set start and end point
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                x, y = pg.mouse.get_pos()
                x = (x // BLOCKSIZE) * BLOCKSIZE
                y = (y // BLOCKSIZE) * BLOCKSIZE
                clicked_block = self.block_map.final_map[(x, y)]

                # clicked block is declared as start block and will be turned into empty block
                if clicked_block == START_BLOCK:
                    self.block_map.final_map[(x, y)] = EMPTY_BLOCK
                    self.start_block_set = False

                # no start block is set
                elif clicked_block == EMPTY_BLOCK and not self.start_block_set:
                    self.block_map.final_map[(x, y)] = START_BLOCK
                    self.start_block_set = True

                # clicked block is empty block, start block is declared and end block is missing
                elif clicked_block == EMPTY_BLOCK and self.start_block_set and not self.start_and_end_block_set:
                    self.block_map.final_map[(x, y)] = END_BLOCK
                    self.start_and_end_block_set = True

                # clicked block is declared as end block
                elif clicked_block == END_BLOCK:
                    self.block_map.final_map[(x, y)] = EMPTY_BLOCK
                    self.start_and_end_block_set = False

    def update(self) -> None:
        pg.display.update()
        self.check_events()
        self.draw()

    def run(self) -> None:

        self.update()

        if self.search_started and not self.algorithm_initialized:
            start, end = self.block_map.get_start_end_points()

            self.search_algorithm.initialize_start_coordinates(start)
            self.search_algorithm.initialize_goal_coordinates(end)
            self.search_algorithm.perform_search()
            self.algorithm_initialized = True

        elif self.algorithm_initialized:
            self.search_algorithm.perform_search()

