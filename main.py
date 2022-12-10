"""Module to draw rectangle in Canvas and function to manipulate with it."""

from tkinter import Canvas, Tk
from PIL import Image
from Path import Path


class Wonderer():
    """The game Wonderer."""

    def __init__(self):
        """Initialise Wonderer with:
        width, height - for canvas.
        create canvas
        area_number - integer - counter of level of the game."""
        self.img_tile = Image.open("pictures/floor.png")
        self.width_step = self.img_tile.width
        self.height_step = self.img_tile.height
        self.width = self.cal_width()
        self.height = self.cal_height()
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.width,
                             height=self.height, background="gray")
        self.area_number = 1

    def cal_width(self):
        """Calculates width of canvas."""
        side = self.img_tile.width * 10
        return side

    def cal_height(self):
        """Calculates height of canvas."""
        side = self.img_tile.height * 10
        return side

    def start_game(self):
        """Launching the game."""
        self.root.title("Wanderer")
        first_tile = Path(self.canvas, int(self.width/2), int(self.height/2))
        self.root.resizable(False, False)
        self.canvas.pack()
        self.root.mainloop()


if __name__ == "__main__":
    firstGame = Wonderer()
    firstGame.start_game()
