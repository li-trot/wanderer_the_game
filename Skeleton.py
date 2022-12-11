"""Class Skeletons."""

from tkinter import *
from PIL import Image, ImageTk
from Character import Character


class Skeleton(Character):
    """Skeleton class."""

    def __init__(self, canvas, max_health, defend, strike):
        """Initialise Skeleton class."""
        super().__init__(canvas, "skeleton", max_health, defend, strike)
        self.x_pos = 0
        self.y_pos = 0
        self.load_assets()
        self.image = self.skeleton

    def load_assets(self):
        """Loading the image of tile."""
        try:
            self.img_skeleton = Image.open("pictures/skeleton.png")
            self.skeleton = ImageTk.PhotoImage(self.img_skeleton)
        except IOError as error:
            print(error)
