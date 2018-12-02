from itertools import product

class Grid:
    def __init__(self, num_rows, num_cols):
        if num_cols <= 0:
            raise Exception('Number of columns must be positive')
        if num_rows <= 0:
            raise Exception('Number of rows must be positive')

        self.num_rows = num_rows
        self.num_cols = num_cols
        self._init_grid()

    
    def _init_grid(self):
        self._mines = [[False] * self.num_cols for row in range(self.num_rows)]
        self._number_grid = [[0] * self.num_cols for row in range(self.num_rows)]
        self._has_calculated_number_grid = False


    def place_mine(self, coord):
        """Places a mine at the given coordinate (row, col)"""
        self.assert_coordinate_in_bounds(coord)

        row, col = coord
        self._mines[row][col] = True
        self._has_calculated_number_grid = False

    
    def has_mine(self, coord):
        """Returns whether the given coordinate has a mine"""
        self.assert_coordinate_in_bounds(coord)
        row, col = coord
        return self._mines[row][col]


    def num_surrounding_mines(self, coord):
        """Returns number of mines surounding coordinate"""
        self.assert_coordinate_in_bounds(coord)

        if not self._has_calculated_number_grid:
            self._calculate_num_surrounding_mines()
        
        row, col = coord
        return self._number_grid[row][col]


    def _calculate_num_surrounding_mines(self):
        for row, col in product(range(self.num_rows), range(self.num_cols)):
            # Get the 8 coordinates that are surrounding the square
            surrounding_coords = [(row + i, col + j) for i, j in product([-1, 0, 1], repeat=2) if i != 0 or j != 0]

            # Filter out coordinates that are out of bounds of the grid
            in_bound_coords = [(a, b) for a, b in surrounding_coords if a >= 0 and b >= 0 and a < self.num_rows and b < self.num_cols]

            num_surrounding_mines = len([1 for (a, b) in in_bound_coords if self._mines[a][b]])
            self._number_grid[row][col] = num_surrounding_mines
        self._has_calculated_number_grid = True

    
    def assert_coordinate_in_bounds(self, coord):
        row, col = coord
        if row < 0:
            raise Exception('row must be positive')
        if col < 0:
            raise Exception('col must be positive')
        if row >= self.num_rows:
            raise Exception('row must be less than num_rows')
        if col >= self.num_cols:
            raise Exception('col must be less than num_cols')
