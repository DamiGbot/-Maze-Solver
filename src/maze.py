from point import Point
from cell import Cell
from graphics import Window
import time 
import random

class Maze():
    
    def __init__(self, point: Point, num_rows: int, num_cols: int, cell_size_x, cell_size_y, win: Window = None, seed= None) -> None:
        self._cells: list[Cell] = []
        self._point = point
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visted()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells: list[Cell] = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
    
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self._win is None:
            return 
        
        point_1: Point = Point(0, 0);
        point_2: Point = Point(0, 0)
        point_1.x = self._point.x + col * self._cell_size_x
        point_1.y = self._point.y + row * self._cell_size_y
        point_2.x = point_1.x + self._cell_size_x
        point_2.y = point_1.y + self._cell_size_y
        self._cells[col][row].draw(point_1, point_2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, col, row):
        self._cells[col][row].visited = True

        while True:
            next_index_list = []
            self._check_possible_directions(col, row, next_index_list)

            # if there is nowhere to go from here
            # just break out
            possible_direction_indexes = len(next_index_list)
            if possible_direction_indexes == 0:
                self._draw_cell(col, row)
                return
            
            # we want to get a possible position
            direction_index = random.randrange(possible_direction_indexes)
            next_index = next_index_list[direction_index]

            # I have a next position
            self._break_selected_cell(col, row, next_index)
            self._break_walls_r(next_index[0], next_index[1])

    def _check_possible_directions(self, col, row, next_index_list):
        # determine which cell(s) to visit next
        # left
        if col > 0 and not self._cells[col - 1][row].visited:
            next_index_list.append((col - 1, row))

        # right
        if col < self._num_cols - 1 and not self._cells[col + 1][row].visited:
            next_index_list.append((col + 1, row))

        # up
        if row > 0 and not self._cells[col][row - 1].visited:
            next_index_list.append((col, row - 1))

        # down
        if row < self._num_rows - 1 and not self._cells[col][row + 1].visited:
            next_index_list.append((col, row + 1))


    def _break_selected_cell(self, col, row, nextPosition):
        if nextPosition[0] == col + 1:
            self._cells[col][row].has_right_wall = False
            self._cells[col + 1][row].has_left_wall = False
        
        if nextPosition[0] == col - 1:
            self._cells[col][row].has_left_wall = False
            self._cells[col - 1][row].has_right_wall = False
        
        if nextPosition[1] == row + 1:
            self._cells[col][row].has_bottom_wall = False
            self._cells[col][row + 1].has_top_wall = False
        
        if nextPosition[1] == row - 1:
            self._cells[col][row].has_top_wall = False
            self._cells[col][row - 1].has_bottom_wall = False

    def _reset_cells_visted(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    # returns True if this is the end cell, OR if it leads to the end cell.
    # returns False if this is a loser cell.
    def _solve_r(self, col, row):
        self._animate()

        # vist the current cell
        self._cells[col][row].visited = True

        # if we are at the end cell, we are done!
        if col == self._num_cols - 1 and row == self._num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (col > 0 and not self._cells[col][col].has_left_wall and not self._cells[col - 1][row].visited):
            self._cells[col][row].draw_move(self._cells[col - 1][row])
            if self._solve_r(col - 1, row):
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col - 1][row], True)

        # move right if there is no wall and it hasn't been visited
        if (col < self._num_cols - 1 and not self._cells[col][row].has_right_wall and not self._cells[col + 1][row].visited):
            self._cells[col][row].draw_move(self._cells[col + 1][row])
            if self._solve_r(col + 1, row):
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col + 1][row], True)

        # move up if there is no wall and it hasn't been visited
        if (row > 0 and not self._cells[col][row].has_top_wall and not self._cells[col][row - 1].visited):
            self._cells[col][row].draw_move(self._cells[col][row - 1])
            if self._solve_r(col, row - 1):
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col][row - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (row < self._num_rows - 1 and not self._cells[col][row].has_bottom_wall and not self._cells[col][row + 1].visited):
            self._cells[col][row].draw_move(self._cells[col][row + 1])
            if self._solve_r(col, row + 1):
                return True
            else:
                self._cells[col][row].draw_move(self._cells[col][row + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False

    # create the moves for the solution using a depth first search
    def solve(self):
        return self._solve_r(0, 0)

