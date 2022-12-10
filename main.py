"""Module to draw rectangle in Canvas and function to manipulate with it."""

from tkinter import *
from PIL import Image
from Path import Path
from Floor import Floor


class Wonderer():
    """The game Wonderer."""

    def __init__(self):
        """Initialise Wonderer with:
        width, height - for canvas.
        create canvas
        area_number - integer - counter of level of the game."""
        self.area_number = 1
        self.img_tile = Image.open("pictures/floor.png")
        self.width_step = self.img_tile.width
        self.height_step = self.img_tile.height
        self.width = self.cal_width()
        self.height = self.cal_height()
        self.floor = None

    def cal_width(self):
        """Calculates width of canvas."""
        side = (self.img_tile.width * 10)
        return side

    def cal_height(self):
        """Calculates height of canvas."""
        side = (self.img_tile.height * 10)
        return side

    def start_game(self):
        """Launching the game."""
        root = Tk()
        root.title("Wanderer")
        root.resizable(False, False)

        canvas = Canvas(root, width=self.width+2,
                        height=self.height+2, background="green")
        canvas.pack()
        self.floor = Floor(canvas, self.width, self.height)
        self.floor.wall_1()
        root.mainloop()


if __name__ == "__main__":
    firstGame = Wonderer()
    firstGame.start_game()
