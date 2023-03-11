from point import Point
from graphics import Window
from line import Line

class Cell():
    def __init__(self, win: Window = None) -> None:
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self.point_1 = None # top left 
        self.point_2 = None # bottom right
        self.win = win

    def draw(self, point1, point2):
        self.point_1 = point1  
        self.point_2 = point2        

        if self.has_left_wall:
            line: Line = Line(self.point_1, Point(self.point_1.x, self.point_2.y))
            self.win.draw_line(line)
        else:
            line: Line = Line(self.point_1, Point(self.point_1.x, self.point_2.y))
            self.win.draw_line(line, "white")

        if self.has_top_wall:
            line: Line = Line(self.point_1, Point(self.point_2.x, self.point_1.y))
            self.win.draw_line(line)
        else:
            line: Line = Line(self.point_1, Point(self.point_2.x, self.point_1.y))
            self.win.draw_line(line, "white")

        if self.has_right_wall:
            line: Line = Line(self.point_2, Point(self.point_2.x, self.point_1.y))
            self.win.draw_line(line)
        else:
            line: Line = Line(self.point_2, Point(self.point_2.x, self.point_1.y))
            self.win.draw_line(line, "white")

        if self.has_bottom_wall:
            line: Line = Line(self.point_2, Point(self.point_1.x, self.point_2.y))
            self.win.draw_line(line)
        else:
            line: Line = Line(self.point_2, Point(self.point_1.x, self.point_2.y))
            self.win.draw_line(line, "white")


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

        #move left
        if self.point_1.x > to_cell.point_1.x:
            line: Line = Line(Point(self.point_1.x, cell_1_y_mid), Point(cell_1_x_mid, cell_1_y_mid))
            self.win.draw_line(line, color_fill)
            line: Line = Line(Point(cell_2_x_mid, cell_2_y_mid), Point(to_cell.point_2.x, cell_2_y_mid))
            self.win.draw_line(line, color_fill)

        #move right
        if self.point_1.x < to_cell.point_1.x:
            line: Line = Line(Point(cell_1_x_mid, cell_1_y_mid), Point(self.point_2.x, cell_1_y_mid))
            self.win.draw_line(line, color_fill)
            line: Line = Line(Point(to_cell.point_1.x, cell_2_y_mid), Point(cell_2_x_mid, cell_2_y_mid))
            self.win.draw_line(line, color_fill)

        #move up
        if self.point_1.y > to_cell.point_1.y:
            line: Line = Line(Point(cell_1_x_mid, cell_1_y_mid), Point(cell_1_x_mid, self.point_1.y))
            self.win.draw_line(line, color_fill)
            line: Line = Line(Point(cell_2_x_mid, to_cell.point_2.y), Point(cell_2_x_mid, cell_2_y_mid))
            self.win.draw_line(line, color_fill)      

        #move down
        if self.point_1.y < to_cell.point_1.y:
            line: Line = Line(Point(cell_1_x_mid, cell_1_y_mid), Point(cell_1_x_mid, self.point_2.y))
            self.win.draw_line(line, color_fill)
            line: Line = Line(Point(cell_2_x_mid, cell_2_y_mid), Point(cell_2_x_mid, to_cell.point_1.y))
            self.win.draw_line(line, color_fill)      
