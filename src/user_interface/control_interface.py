import sys
import tkinter as tk
from tkinter import messagebox

from src.map_structure.map_structure import MapStructure
from src.search_algorithms.breadth_first_search import Bfs
from src.search_algorithms.depth_first_search import Dfs
from src.settings.settings import INFORMATION_FRAME_TEXT, RESOLUTION
from src.user_interface.application_window import ApplicationWindow


class ControlInterface(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.width, self.height = RESOLUTION
        self.size_frame = tk.Frame(master=self,
                                   relief="groove",
                                   borderwidth=2)
        self.size_frame.grid(column=0,
                             row=0)

        self.label_width = tk.Label(master=self.size_frame,
                                    text="Width",
                                    justify="right")
        self.label_width.grid(row=0,
                              column=0)
        self.label_width_entry = tk.Entry(master=self.size_frame,
                                          justify="right")
        self.label_width_entry.insert(0, self.width)
        self.label_width_entry.grid(row=0,
                                    column=1)

        self.label_height = tk.Label(master=self.size_frame,
                                     text="Heigth",
                                     justify="right")
        self.label_height.grid(row=1,
                               column=0)
        self.label_height_entry = tk.Entry(master=self.size_frame,
                                           justify="right")
        self.label_height_entry.insert(0, self.height)
        self.label_height_entry.grid(row=1,
                                     column=1)

        self.button_frame = tk.Frame(master=self)
        self.button_frame.grid(column=0,
                               row=1,
                               sticky="NSWE")
        self.algorithm_selection_frame = tk.Frame(master=self.button_frame,
                                                  relief="groove",
                                                  borderwidth=2)
        self.algorithm_selection_frame.pack(fill=tk.X)
        self.information_frame = tk.Frame(master=self,
                                          relief="groove",
                                          borderwidth=2)
        self.information_frame.grid(column=1,
                                    row=0,
                                    rowspan=2)
        self.information_label = tk.Label(master=self.information_frame,
                                          text=INFORMATION_FRAME_TEXT,
                                          justify="left")
        self.information_label.pack(fill=tk.X)

        self.search_algorithms = {"Breadth First Search": Bfs, "Depth First Search": Dfs}
        self.application = None
        self.map_structure = None
        self.search_algorithm = None
        self.initialized = False
        self.selected_search_algorithm = tk.StringVar()
        self.randomized_walls = tk.IntVar()
        for key in self.search_algorithms.keys():
            tk.Radiobutton(master=self.algorithm_selection_frame,
                           text=key,
                           variable=self.selected_search_algorithm,
                           value=key).pack(fill= tk.X)

        self.checkbox = tk.Checkbutton(master=self.button_frame,
                                       text="Randomized Walls?",
                                       variable=self.randomized_walls,
                                       onvalue=1,
                                       offvalue=0)
        self.checkbox.pack(fill= tk.X)

        self.initialize_application_button = tk.Button(master= self.button_frame,
                                                       text="Initialize Programm",
                                                       command=lambda: self.initialize_search_application())
        self.initialize_application_button.pack(fill=tk.X)

        self.start_button = tk.Button(master=self.button_frame,
                                      text="Start search programm",
                                      command=lambda: self.run(),
                                      state=tk.DISABLED)
        self.start_button.pack(fill=tk.X)

        self.quit_button = tk.Button(master=self.button_frame,
                                     text="Quit",
                                     command=lambda: sys.exit())
        self.quit_button.pack(fill=tk.X)

    def normalize_values(self, *, value_to_normalize: str) -> int:
        value_to_normalize = (int(value_to_normalize) // 10) * 10
        return value_to_normalize

    def input_is_integer(self, *, input_value: str) -> bool:
        return input_value.isdigit()

    def initialize_search_application(self) -> None:

        self.width = self.label_width_entry.get()
        self.height = self.label_height_entry.get()

        if not self.input_is_integer(input_value=self.width) or not self.input_is_integer(input_value=self.height):
            messagebox.showinfo(title="Wrong input",
                                message="Please enter a number as input for height / width and initialize again.")
            return

        # normalize values if someone entered values like 344 or 522 or whatever
        self.width = self.normalize_values(value_to_normalize=self.width)
        self.height = self.normalize_values(value_to_normalize=self.height)

        randomized_walls = bool(self.randomized_walls.get())
        self.map_structure = MapStructure(randomized_walls=randomized_walls,
                                          width=int(self.width),
                                          height=int(self.height))
        selected_algorithm = self.selected_search_algorithm.get()
        self.search_algorithm = self.search_algorithms[selected_algorithm](map_structure=self.map_structure)

        self.initialized = True
        self.start_button.config(state=tk.ACTIVE)

    def run(self):

        self.application = ApplicationWindow(block_map=self.map_structure,
                                             search_algorithm=self.search_algorithm,
                                             width=int(self.width),
                                             height=int(self.height))

        while True:
            
            self.application.run()
            # either found goal or no way exists
            if self.application.search_is_over():
                input()