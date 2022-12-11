"""Module to draw rectangle in Canvas and function to manipulate with it."""

from tkinter import *
from PIL import Image
from Path import Path
from Floor import Floor
from Hero import Hero
from Text import Text
from random import randint


class Wonderer():
    """The game Wonderer."""

    tile = Image.open("pictures/floor.png")

    def __init__(self):
        """Initialise Wonderer with:
        width, height - for canvas.
        create canvas
        area_number - integer - counter of level of the game."""
        self.area_number = 1
        self.canvas = None
        self.width_step = self.tile.width
        self.height_step = self.tile.height
        self.width = self.cal_width()
        self.height = self.cal_height()
        self.floor = None
        self.hero = None
        self.rect = None
        self.hero_act = None
        self.text = None

    def cal_width(self):
        """Calculates width of canvas."""
        side = (self.tile.width * 10)
        return side

    def cal_height(self):
        """Calculates height of canvas."""
        side = (self.tile.height * 10)
        return side

    def start_game(self):
        """Launching the game."""
        root = Tk()
        root.title("Wanderer")
        root.geometry("722x752")
        root.resizable(False, False)
        root.configure(background='black')

        self.canvas = Canvas(root, width=self.width,
                             height=self.height+30, background="black")
        self.canvas.create_rectangle(0, 720, self.width,
                                     (self.height+30), fill="white")

        self.canvas.bind("<KeyPress>", self.on_key_press)
        self.canvas.pack(anchor=CENTER, expand=True)
        self.canvas.focus_set()

        self.floor = Floor(self.canvas, self.width,
                           self.height, self.area_number)
        self.floor.wall_1()
        self.add_hero()

        self.hero_act = self.canvas.create_image(
            self.hero.x_pos, self.hero.y_pos, image=self.hero.image, anchor=NW, tag="hero")

        self.text = Text(self.canvas, self.hero, self.width, self.height)
        self.text.print_text(self.area_number)

        self.floor.add_monsters(3)
        self.floor.add_boss()
        self.floor.create_monsters()

        root.mainloop()

    def add_hero(self):
        """Calculate Hero info."""
        health_g = 20 + (3 * randint(1, 6))
        defeat_g = 2 * randint(1, 6)
        strike_g = 5 + randint(1, 6)
        self.hero = Hero(self.canvas, health_g, defeat_g, strike_g)

    def on_key_press(self, enter):
        """When arrows are pressed the box moves i appropriate way on 100."""
        # go up
        if enter.keycode in (38, 87):
            self.hero.image = self.hero.hero_up
            if self.hero.y_pos - self.height_step >= 0:
                if self.floor.check_cross(self.hero.x_pos, self.hero.y_pos - self.height_step):
                    self.hero.y_pos = self.hero.y_pos - self.height_step
        # go down
        elif enter.keycode in (40, 83):
            self.hero.image = self.hero.hero_down
            if self.hero.y_pos + self.height_step <= self.height - self.height_step:
                if self.floor.check_cross(self.hero.x_pos, self.hero.y_pos + self.height_step):
                    self.hero.y_pos = self.hero.y_pos + self.height_step
        # go right
        elif enter.keycode in (39, 68):
            self.hero.image = self.hero.hero_right
            if self.hero.x_pos + self.width_step <= self.width - self.width_step:
                if self.floor.check_cross(self.hero.x_pos + self.width_step, self.hero.y_pos):
                    self.hero.x_pos = self.hero.x_pos + self.height_step
        # go left
        elif enter.keycode in (37, 65):
            self.hero.image = self.hero.hero_left
            if self.hero.x_pos - self.width_step >= 0:
                if self.floor.check_cross(self.hero.x_pos - self.width_step, self.hero.y_pos):
                    self.hero.x_pos = self.hero.x_pos - self.height_step
        # and lower if the key that was pressed the down arrow
        self.canvas.delete("hero")
        self.hero_act = self.canvas.create_image(
            self.hero.x_pos, self.hero.y_pos, image=self.hero.image, anchor=NW, tag="hero")


# Select the canvas to be in focused so it actually receives the key hitting.
# Draw the box in the initial position


if __name__ == "__main__":
    firstGame = Wonderer()
    firstGame.start_game()
