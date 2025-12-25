import os
import tkinter
from PIL import ImageTk, Image
from PIL.Image import Transpose


class Submarine:
    canvas: tkinter.Canvas
    image: int
    __image_path: str = os.path.join(os.getcwd(), 'submarine.png')

    def __init__(self, canvas):

        self.canvas = canvas
        # При помощи PIL считываем информацию о картинке из файла
        image_file = Image.open(self.__image_path)
        # Меняем размер картинки на 100x100
        image_file = image_file.resize((100, 100), resample=Image.Resampling.LANCZOS)
        # Конвертируем картинку в объект photo image для tkinter
        self._image_src_right = ImageTk.PhotoImage(image_file)
        # Добавляем вторую зеркальную картинку
        self._image_src_left = ImageTk.PhotoImage(image_file.transpose(Transpose.FLIP_LEFT_RIGHT))
        # Формируем изображение на холсте, используя объект photo image
        self.image = self.canvas.create_image(
            200,
            200,
            image=self._image_src_right
        )

    def __del__(self):
        self.canvas.delete(self.image)

    def move(self, event):
        if event.keysym == "Up":
            self.canvas.move(self.image, 0, -5)
        if event.keysym == "Down":
            self.canvas.move(self.image, 0, 5)
        if event.keysym == "Left":
            self.canvas.move(self.image, -5, 0)
            self.canvas.itemconfig(self.image, image=self._image_src_left)
        if event.keysym == "Right":
            self.canvas.move(self.image, 5, 0)
            self.canvas.itemconfig(self.image, image=self._image_src_right)