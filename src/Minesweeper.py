from random import shuffle
from itertools import product
from .Grid import Grid

class Minesweeper:

    def __init__(self, num_cols, num_rows, num_mines=10):
        self.grid = Grid(num_rows, num_cols)
        if num_mines >= num_cols * num_rows:
            raise Exception('Number of mines must not exceed board area')

        self.num_cols = num_cols
        self.num_rows = num_rows
        self.num_mines = num_mines

        self.has_ended = False

        self._has_started = False

    
    def dig(self, coord):
        """Dig up square at row, col"""
        if not self._has_started:
            self._init_mines(safe_coord=coord)

    
    def _init_mines(self, safe_coord):
        safe_row, safe_col = safe_coord

        # Flatten 2D grid into a line, put the mines at the beginning
        # Then shuffle to figure out where the mines should go
        # Subtract one because the safe coord will never have a mine
        linearized_grid = [False] * (self.num_rows * self.num_cols - 1)
        for i in range(self.num_mines):
            linearized_grid[i] = True
        shuffle(linearized_grid)

        # Insert the safe coordinate
        safe_index = safe_row * self.num_rows + safe_col
        linearized_grid.insert(safe_index, False)

        # Now map the line back to the 2D grid
        for grid_index, is_mine in enumerate(linearized_grid):
            if is_mine:
                row = int(grid_index / self.num_rows)
                col = grid_index % self.num_rows

                # Mines are represented as -1
                self.grid.place_mine((row, col))


    def _init_numbers(self):
        for row, col in product(range(self.num_rows), range(self.num_cols)):
            if self._grid[row][col] == -1:
                pass

            # Get the 8 coordinates that are surrounding the square
            surrounding_coords = [(row + i, col + j) for i, j in product([-1, 0, 1], repeat=2) if i != 0 or j != 0]

            # Filter out coordinates that are out of bounds of the grid
            surrounding_in_bound_coords = [(a, b) for a, b in surrounding_coords if a >= 0 and b >= 0 and a < self.num_rows and b < self.num_cols]

            num_surrounding_mines = len([1 for (a, b) in surrounding_in_bound_coords if self._grid[a][b] == -1])
            self._grid[row][col] = num_surrounding_mines
