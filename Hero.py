"""Hero class."""

from tkinter import *
from PIL import Image, ImageTk
from Character import Character


class Hero(Character):
    """Hero class."""

    def __init__(self, canvas, max_health, defend, strike):
        super().__init__(canvas, "hero", max_health, defend, strike)
        self.x_pos = 0
        self.y_pos = 0
        self.load_assets()
        self.image = self.hero_down

    def load_assets(self):
        """Loading the image of tile."""
        try:
            self.img_hero_down = Image.open("pictures/hero-down.png")
            self.hero_down = ImageTk.PhotoImage(self.img_hero_down)

            self.img_hero_up = Image.open("pictures/hero-up.png")
            self.hero_up = ImageTk.PhotoImage(self.img_hero_up)

            self.img_hero_left = Image.open("pictures/hero-left.png")
            self.hero_left = ImageTk.PhotoImage(self.img_hero_left)

            self.img_hero_right = Image.open("pictures/hero-right.png")
            self.hero_right = ImageTk.PhotoImage(self.img_hero_right)

        except IOError as error:
            print(error)
