import random
from threading import Thread
from time import sleep
from tkinter import Tk, Canvas
from submarine import Submarine
from bubble import Bubble

window = Tk()

window.geometry('800x600')
window.title('Bubble Hunter')

# Инициализируем холст
canvas = Canvas(window, background='#000485', height=600, width=800)
window.focus_set()
canvas.pack()

# Добавляем объект подводной лодки
submarine = Submarine(canvas)
bubbles = []
for i in range(5):
    bubbles.append(Bubble(
        canvas,
        random.randint(10, 800),
        random.randint(10, 600),
        random.randint(10, 30),
        "white"
    ))

window.bind("<Key>", submarine.move)
def move_bubble():
    while True:
        for bubble in bubbles:
            bubble.move()
        sleep(.1)

Thread(
    target=move_bubble,
    daemon=True
).start()

window.mainloop()
