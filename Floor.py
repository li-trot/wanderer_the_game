"""Floor class. To generate 10*10 tiles floor."""

from Path import Path
from Wall import Wall


class Floor():
    """Class for generation floor 10*10 Path bricks."""

    def __init__(self, canvas, width_fl, height_fl):
        """Initialise Floor wtith:
        Parameters:
            canvas - canvas frame;
            width_fl - max width of floor;
            height_fl - max height of floor;

        Additional arguments:
            width.step, height_step - each step
            keep - directory to keep each brick.
                keys are numbers of rows,
                values - columns with Path object.
        """
        self.canvas = canvas
        self.width_fl = width_fl
        self.height_fl = height_fl
        self.width_step = int(self.width_fl/10)
        self.height_step = int(self.height_fl/10)
        self.keep = {}
        self.generate_floor()

    def generate_floor(self):
        """Generation of floor."""
        y_position = 0
        for num_y in range(1, 11):
            self.keep[num_y] = {}
            x_position = 0
            for num_x in range(1, 11):
                tile = Path(self.canvas, x_position, y_position)
                new_pair = {num_x: tile}
                self.keep[num_y].update(new_pair)
                x_position += self.width_step
            y_position += self.height_step

    def get_coordinates(self, raw, column):
        spot = []
        x = self.keep[raw][column].get_x()
        spot.append(x)
        y = self.keep[raw][column].get_y()
        spot.append(y)
        return spot

    def add_wall(self, raw, column):
        coordin = self.get_coordinates(raw, column)
        x_cor, y_cor = coordin
        self.keep[raw][column] = Wall(self.canvas, x_cor, y_cor)

    def wall_1(self):
        list_wall = [
            [1, 4], [2, 4], [2, 6], [2, 8], [2, 9],
            [3, 2], [3, 3], [3, 4], [3, 6],
            [3, 8], [3, 9], [4, 6], [5, 1], [5, 2],
            [5, 3], [5, 4], [5, 6], [5, 7],
            [5, 8], [5, 9], [6, 2], [6, 4], [7, 2],
            [7, 4], [7, 6], [7, 7], [7, 9],
            [8, 6], [8, 7], [8, 9], [9, 2], [9, 3],
            [9, 4], [9, 9], [10, 4], [10, 6], [10, 7]
        ]

        for elem in list_wall:
            row, col = elem
            self.add_wall(row, col)

    def check_what(self, x_f, y_f):
        """Checks what type of object on that position."""
        obj = self.keep[y_f][x_f]
        print(obj.type)
        print(obj.check_cross())
        return obj.check_cross()
