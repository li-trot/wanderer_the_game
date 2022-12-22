"""Hero class."""

from tkinter import NW
from PIL import Image, ImageTk
from character import Character


class Hero(Character):
    """Hero class."""

    def __init__(self, canvas, max_health, defend, strike):
        """Initialise Hero class."""
        super().__init__(canvas, "Hero", max_health, defend, strike)
        self.load_assets()
        self.image = self.hero_down
        self.key = False
        self.kill_boss = False
        self.move = True

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

    def draw(self):
        "Draw the hero."
        if self.health > 0:
            self.canvas.create_image(
                self.x_pos, self.y_pos, image=self.image, anchor=NW, tag="hero")
