import pytest
from src import Minesweeper

class TestMinesweeper:

    def test_mines_needs_to_be_less_than_board_area(self):
        with pytest.raises(Exception):
            game = Minesweeper(num_rows=1, num_cols=1, num_mines=1)
        with pytest.raises(Exception):
            game = Minesweeper(num_rows=5, num_cols=10, num_mines=999)
        with pytest.raises(Exception):
            game = Minesweeper(num_rows=20, num_cols=10, num_mines=200)


    def test_initialize(self):
        game = Minesweeper(num_rows=2, num_cols=2, num_mines=1)


    def test_there_is_never_a_mine_on_first_move(self):
        for i in range(10):
            game = Minesweeper(num_rows=10, num_cols=10, num_mines=99)
            game.dig((0, 0))
        assert not game.grid.has_mine((0, 0))
