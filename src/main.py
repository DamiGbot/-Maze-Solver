from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    point_1 = Point(50, 50)
    point_2 = Point(400, 400)
    line = Line(point_1, point_2)
    win.draw_line(line)
    win.wait_for_close()

main()