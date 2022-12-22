"""Class Wall. You can't cross it."""
from tkinter import NW
from PIL import Image, ImageTk
from brick import Brick


class Wall(Brick):
    """Class Path, descendant of Brick class:
    can't be crossed, can't contain monsters.
    """

    def __init__(self, canvas_board, x_coord, y_coord):
        """Initialise Path with:
        Parameters:
            canvas - canvas instance;
            coordinates - list of two integers, x,y coordinates.
        Additional argument:
            monster - whether there is a monster.
        """
        super().__init__(canvas_board, "wall", x_coord, y_coord)
        self.load_assets()
        self.create_wall()
        self.crossability = False

    def load_assets(self):
        """Loading the image of wall."""
        try:
            self.img_tile = Image.open("pictures/wall.png")
            self.wall = ImageTk.PhotoImage(self.img_tile)
        except IOError as error:
            print(error)

    def create_wall(self):
        """Create wall brick."""
        self.canvas.create_image(
            self.x_pos, self.y_pos, image=self.wall, anchor=NW, tag="wall")
