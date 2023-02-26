from point import Point
from graphics import Window
from line import Line
from typing import Type

class Cell():
    def __init__(self, has_left_wall: bool,has_right_wall: bool, has_top_wall: bool, has_bottom_wall: bool, visited: bool, point_1: Point, point_2: Point, win: Window) -> None:
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self.visited = visited
        self.point_1 = point_1 # top left 
        self.point_2 = point_2 # bottom right
        self.win = win

    def draw(self):
        if self.has_left_wall:
            line: Line = Line(self.point_1, Point(self.point_1.x, self.point_2.y))
            self.win.draw_line(line)

        if self.has_top_wall:
            line: Line = Line(self.point_1, Point(self.point_2.x, self.point_1.y))
            self.win.draw_line(line)

        if self.has_bottom_wall:
            line: Line = Line(self.point_2, Point(self.point_1.x, self.point_2.y))
            self.win.draw_line(line)

        if self.has_right_wall:
            line: Line = Line(self.point_2, Point(self.point_2.x, self.point_1.y))
            self.win.draw_line(line)

    def draw_move(self, to_cell, undo=False):
        if self.win is None:
            return
        
        cell_1_x_mid = (self.point_1.x + self.point_2.x) / 2
        cell_1_y_mid = (self.point_1.y + self.point_2.y) / 2

        cell_2_x_mid = (to_cell.point_1.x + to_cell.point_2.x) / 2
        cell_2_y_mid = (to_cell.point_1.y + to_cell.point_2.y) / 2

        color_fill = "red"
        if undo:
            color_fill = "gray"

        #move right
        if self.point_1.x < to_cell.point_1.x:
            line: Line = Line(Point(cell_1_x_mid, cell_1_y_mid), Point(self.point_2.x, cell_1_y_mid))
            self.win.draw_line(line, color_fill)
            line: Line = Line(Point(to_cell.point_1.x, cell_2_y_mid), Point(cell_2_x_mid, cell_2_y_mid))
            self.win.draw_line(line, color_fill)
