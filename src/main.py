from graphics import Window
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    point_1 = Point(20, 20)
    point_2 = Point(40, 40)
    cell = Cell(True, False, True, True, False, point_1, point_2, win)
    cell.draw()
    win.wait_for_close()

main()