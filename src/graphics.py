from tkinter import Tk, BOTH, Canvas, Button
from line import Line

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, {"bg": "white", "height": height, "width": width})
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.running = False

    def draw_line(self, line: Line, fill_color: str="black"):
        line.draw(self.canvas, fill_color)

    def draw_button(self, text):
        button = Button(self.root, text= text, command=self.printText, fg="blue", bg="red")
        return button;

    def printText(self):
        print("button Pressed")


