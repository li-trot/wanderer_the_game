"""Floor class. To generate 10*10 tiles floor."""

from Path import Path


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
        y_position = 3
        for num_y in range(1, 11):
            self.keep[num_y] = {}
            x_position = 3
            for num_x in range(1, 11):
                tile = Path(self.canvas, x_position, y_position)
                new_pair = {num_x: tile}
                self.keep[num_y].update(new_pair)
                x_position += self.width_step
            y_position += self.height_step
