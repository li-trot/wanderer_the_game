"""Path class. To create tile."""
from tkinter import NW
from PIL import Image, ImageTk
from Brick import Brick


class Path(Brick):
    """Class Path, descendant of Brick class:
    could be crossed if there is not some monster.
    """

    def __init__(self, canvas_board, x_coord, y_coord):
        """Initialise Path with:
        Parameters:
            canvas - canvas instance;
            coordinates - list of two integers, x,y coordinates.
        Additional argument:
            monster - whether there is a monster.
        """
        super().__init__(canvas_board, "path", x_coord, y_coord)
        self.load_assets()
        self.create_tile()
        self.monster = False

    def occupy(self):
        """Whether there is something on the path."""
        self.crossability = False
        self.monster = True

    def load_assets(self):
        """Loading the image of tile."""
        try:
            self.img_tile = Image.open("pictures/floor.png")
            self.tile = ImageTk.PhotoImage(self.img_tile)
        except IOError as error:
            print(error)

    def create_tile(self):
        """Create tile path."""
        self.canvas.create_image(
            self.x_pos, self.y_pos, image=self.tile, anchor=NW, tag="path")
