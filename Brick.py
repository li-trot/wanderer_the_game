"""Brick class."""


class Brick():
    """The Brick class."""

    def __init__(self, canvas_board, type_of_brick, x_coord, y_coord):
        """Initialise Brick class with:
        Parameters:
        canvas - canvas to draw;
        type - type of brick - path or wall.
        coordinates -  x and y coordinates, spot of the brick.

        Default arguments:
        crossability - True/False - whether it could be crossed, according to the type of brick;

        Raise ValueError - if type of Brick is wrong,
                passed coordinates are in wrong format."""
        try:
            if not isinstance(x_coord, int) or not isinstance(y_coord, int):
                raise TypeError("Coordinates must be integers")
        except ValueError:
            print("Argument 'coordinates' must be list with two integers.")
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.canvas = canvas_board
        self.type = type_of_brick
        if self.type == "path":
            self.crossability = True
        elif self.type == "wall":
            self.crossability = True
        else:
            raise ValueError("Type of brick could be only 'path' or 'wall'.")

    def check_cross(self):
        """Check the crossability of brick.
        Returns True/False."""
        if self.crossability is True:
            return True
        return False

    def get_x(self):
        """Returns x coordinate."""
        return self.x_pos

    def get_y(self):
        """Returns y coordinate."""
        return self.y_pos
