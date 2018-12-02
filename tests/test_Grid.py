import pytest
from src import Grid
from itertools import product

class TestMinesweeper:

    def test_board_needs_to_have_positive_area(self):
        with pytest.raises(Exception):
            grid = Grid(num_rows=0, num_cols=0)
        with pytest.raises(Exception):
            grid = Grid(num_rows=10,num_cols=0)
        with pytest.raises(Exception):
            grid = Grid(num_rows=0, num_cols=10)
        with pytest.raises(Exception):
            grid = Grid(num_rows=-10, num_cols=-10)
        with pytest.raises(Exception):
            grid = Grid(num_rows=0, num_cols=-10)
        with pytest.raises(Exception):
            grid = Grid(num_rows=-10, num_cols=0)


    def test_initialize(self):
        grid = Grid(num_rows=2, num_cols=2)


    def test_init_numbers(self):
        grid = self.create_grid_with_mines([
            [1, 0],
            [0, 0]
        ])
        self.verify_num_surrounding_mines(grid, [
            [0, 1],
            [1, 1]
        ])

        grid = self.create_grid_with_mines([
            [0, 0, 0, 0, 1],
            [0, 1, 1, 1, 1]
        ])
        self.verify_num_surrounding_mines(grid, [
            [1, 2, 3, 4, 2],
            [1, 1, 2, 3, 2]
        ])

        grid = self.create_grid_with_mines([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ])
        self.verify_num_surrounding_mines(grid, [
            [0, 0, 0, 0, 0],
            [0, 1, 2, 2, 1],
            [1, 2, 3, 2, 2],
            [1, 2, 5, 3, 2],
            [1, 2, 2, 2, 1],
            [0, 1, 1, 1, 0]
        ])


    def create_grid_with_mines(self, mines):
        num_rows = len(mines)
        num_cols = len(mines[0])
        grid = Grid(num_rows, num_cols)
        for row, col in product(range(num_rows), range(num_cols)):
            if mines[row][col] == 1:
                grid.place_mine((row, col))
        return grid
    
    def verify_num_surrounding_mines(self, grid, expected):
        num_rows = len(expected)
        num_cols = len(expected[0])
        for row, col in product(range(num_rows), range(num_cols)):
            actual = grid.num_surrounding_mines((row, col))
            assert actual == expected[row][col], 'Expected %d, number of surrounding mines at (%d, %d) to be %d' % (actual, row, col, expected[row][col])
