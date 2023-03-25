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
        self._myList = []
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
    # returns False if this is not the end cell.
    def _solve_r(self, col, row):
        self._animate()

        self._cells[col][row].visited = True

        # if we get to the end (row.length - 1, colomn - 1) we return true 
        if row == self._num_rows - 1 and col == self._num_cols - 1:
            return True;

        # start position is from (0, 0)
        # then I randomly pick a side that is opened (Meaning false)
        nextPosition = [];
        self._possible_directions_to_enter(col, row, nextPosition);

        if len(nextPosition) > 0:
            nextIdx = random.randint(0, len(nextPosition) - 1)
            nextCell = nextPosition[nextIdx]
            nextPosition.remove(nextCell)
            self._cells[col][row].draw_move(self._cells[nextCell[0]][nextCell[1]])
            self._myList.append((col, row))
            return self._solve_r(nextCell[0], nextCell[1])
        else: 
            if len(self._myList) > 0:
                listLength = len(self._myList) - 1
                prevCell = self._myList[listLength]
                self._myList.remove(prevCell)
                self._cells[col][row].draw_move(self._cells[prevCell[0]][prevCell[1]], True)
                return self._solve_r(prevCell[0], prevCell[1])
            else:
                # check if we can go back at most twice 
                return False;
            # I want to track back to previous cell 
    
    def _possible_directions_to_enter(self, col, row, next_index_list):
        # determine which cell(s) to enter next
        # left
        if col > 0 and not self._cells[col - 1][row].visited and not self._cells[col][row].has_left_wall:
            next_index_list.append((col - 1, row))

        # right
        if col < self._num_cols - 1 and not self._cells[col + 1][row].visited and not self._cells[col][row].has_right_wall:
            next_index_list.append((col + 1, row))

        # up
        if row > 0 and not self._cells[col][row - 1].visited and not self._cells[col][row].has_top_wall:
            next_index_list.append((col, row - 1))

        # down
        if row < self._num_rows - 1 and not self._cells[col][row + 1].visited and not self._cells[col][row].has_bottom_wall:
            next_index_list.append((col, row + 1))


    # create the moves for the solution using a depth first search
    def solve(self):
        return self._solve_r(0, 0)

# I want to create a stack 
# this stack is used to keep track of all the cell I have entered.
# if there is no way I pop of the top of the stack and move  to it 