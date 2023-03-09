from point import Point
from cell import Cell
from graphics import Window
import time 
import random

class Maze():
    
    def __init__(self, point: Point, num_rows, num_cols, cell_size_x, cell_size_y, win: Window = None) -> None:
        self._cells: list[Cell] = []
        self._point = point
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells: list[Cell] = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return 
        
        point_1: Point
        point_2: Point
        point_1.x = self._point.x + i * self._cell_size_x
        point_1.y = self._point.y + j * self._cell_size_y
        point_2.x = point_1.x + self._cell_size_x
        point_2.y = point_1.y + self._cell_size_y
        self._cells[i][j].draw(point_1, point_2)
        self._animate()

        
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)


