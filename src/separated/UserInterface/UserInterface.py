import sys

import pygame as pg
import pygame.time

from src.separated.Map.Map import Map
from src.separated.Settings.settings import *
from src.separated.search_algorithms.Bfs import Bfs


class Window:
    def __init__(self, search_algorithm, block_map: Map):
        pg.init()
        self.screen = pg.display.set_mode(RESOLUTION)

        self.height, self.width = RESOLUTION
        self.block_map = block_map
        self.block_map.surface = self.screen
        self.is_dragging = False
        self.search_algorithm = search_algorithm
        self.start = False
        self.clock = pygame.time.Clock()
        self.clock.tick(FRAMERATE)

    def draw(self):
        self.screen.fill(color=BACKGROUND_COLOR)

    def check_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                self.start = True
                print(self.start)

            # left click
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.is_dragging = True
                x, y = pg.mouse.get_pos()
                x = (x // BLOCKSIZE) * BLOCKSIZE
                y = (y // BLOCKSIZE) * BLOCKSIZE
                clicked_block = self.block_map.final_map[(x, y)]

                # clicked block is wall, destroy wall
                if clicked_block == 1:
                    self.block_map.final_map[(x, y)] = 0

                # clicked block is already declared as start block, turn it into wall
                elif clicked_block == 2:
                    self.block_map.decrease_start_count()
                    self.block_map.final_map[(x, y)] = 1

                # empty block
                else:
                    self.block_map.final_map[(x, y)] = 1

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
                if clicked_block == 1:
                    pass

                # clicked block is already declared as start / goal block, turn it into wall
                elif clicked_block == 2:
                    self.block_map.decrease_start_count()
                    self.block_map.final_map[(x, y)] = 1

                # empty block, set up wall
                else:
                    self.block_map.final_map[(x, y)] = 1

            # right click
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                print(tuple(self.block_map.get_start_end_points()))
                x, y = pg.mouse.get_pos()
                x = (x // BLOCKSIZE) * BLOCKSIZE
                y = (y // BLOCKSIZE) * BLOCKSIZE
                clicked_block = self.block_map.final_map[(x, y)]

                # clicked block is start / end block
                if clicked_block == 2:
                    self.block_map.final_map[(x, y)] = 0
                    self.block_map.decrease_start_count()

                # clicked block is empty block
                elif clicked_block == 0 and self.block_map.start_count < 2:
                    self.block_map.final_map[(x, y)] = 2
                    self.block_map.increase_start_count()

    def update(self):
        pg.display.update()
        self.check_events()
        self.draw()
        self.block_map.draw()

    def run(self):
        c = 0

        while True:
            self.update()
            if self.start and c != 1:
                c = 1
                start, end = self.block_map.get_start_end_points()

                self.search_algorithm.initialize_start_coordinates(start)
                self.search_algorithm.initialize_goal_coordinates(end)
                self.search_algorithm.perform_search()

            elif c == 1:
                self.search_algorithm.perform_search()
                if self.search_algorithm.goal_found:
                    print("gefunden")
                    return


if __name__ == '__main__':

    m = Map()
    b = Bfs(map=m)

    w = Window(block_map=m,
               search_algorithm=b)
    w.run()


