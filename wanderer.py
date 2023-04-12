"""The main class of the game. Let's start."""

from tkinter import Tk, Canvas, CENTER
from PIL import Image
from level import Level


class Wanderer():
    """The game Wonderer.
        by StartGame.
        Creates: Canvas, Text, Level, Hero, Button.
    """

    def __init__(self):
        """Initialise Wonderer with:
        width, height - for canvas.
        create canvas
        area_number - integer - counter of level of the game.
        """
        self.tile = Image.open("pictures/floor.png")
        self.area_number = 1
        self.canvas = None
        self.step = None
        self.width = self.cal_width()
        self.height = self.cal_height()
        self.level = None
        self.hero = None
        self.text = None
        self.bind_key = None
        self.step_cl()
        self.start()

    def start(self):
        """Launching the game."""
        root = Tk()
        root.title("Wanderer")
        screen_width = root.winfo_screenwidth()
        width_geometry = 722
        y_for_root = int((screen_width/2) - (width_geometry/2))
        root.geometry(f"{width_geometry}x752+{y_for_root}+10")
        root.resizable(False, False)
        root.configure(background='black')
        self.canvas = Canvas(
            root, width=self.width, height=self.height + 30, background="black")

        self.canvas.create_rectangle(
            0, 720, self.width, self.height+30, fill="white")

        self.canvas.pack(anchor=CENTER, expand=True)

        self.level = Level(self.canvas, self.step, self.tile)

        root.mainloop()

    def step_cl(self):
        """Calculation of steps."""
        if self.tile.width == self.tile.height:
            self.step = self.tile.width
        else:
            raise ValueError("Picture must be square!")

    def cal_width(self):
        """Calculates width of canvas."""
        side = (self.tile.width * 10)
        return side

    def cal_height(self):
        """Calculates height of canvas."""
        side = (self.tile.height * 10)
        return side


if __name__ == "__main__":
    game = Wanderer()
