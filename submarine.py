import tkinter


class Submarine:
    canvas: tkinter.Canvas
    image: int

    def __init__(self, canvas):
        self.canvas = canvas
        self.image = self.canvas.create_oval(200, 200, 240, 240, fill='yellow')

    def __del__(self):
        self.canvas.delete(self.image)

    def move(self, event):
        if event.keysym == "Up":
            self.canvas.move(self.image, 0, -5)
        if event.keysym == "Down":
            self.canvas.move(self.image, 0, 5)
        if event.keysym == "Left":
            self.canvas.move(self.image, -5, 0)
        if event.keysym == "Right":
            self.canvas.move(self.image, 5, 0)