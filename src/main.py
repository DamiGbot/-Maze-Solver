from graphics import Window
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    point_1 = Point(20, 20)
    point_2 = Point(40, 40)
    point_3 = Point(40, 20)
    point_4 = Point(60, 40)
    cell_1 = Cell(win, False, False, True, True, False, point_1, point_2)
    cell_2 = Cell(win, False, False, True, True, False, point_3, point_4)
    cell_1.draw()
    cell_2.draw()
    cell_1.draw_move(cell_2)
    win.wait_for_close()

main()