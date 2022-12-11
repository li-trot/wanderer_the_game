"""Class Boss."""

from tkinter import *
from PIL import Image, ImageTk
from Character import Character


class Boss(Character):
    """boss class."""

    def __init__(self, canvas, max_health, defend, strike):
        """Initialise Boss class."""
        super().__init__(canvas, "boss", max_health, defend, strike)
        self.load_assets()
        self.image = self.boss

    def load_assets(self):
        """Loading the image of tile."""
        try:
            self.img_boss = Image.open("pictures/boss.png")
            self.boss = ImageTk.PhotoImage(self.img_boss)
        except IOError as error:
            print(error)
