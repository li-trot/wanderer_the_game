"""Floor class. To generate 10*10 tiles floor."""

from path import Path
from wall import Wall
from monsters import Monsters


class Floor():
    """Class for generation floor 10*10 Path bricks.
    by Level_Main.
    Creates - Path and Wall, Monsters instances.
    """

    def __init__(self, canvas_main, width_fl_main, height_fl_main, level_main, step_main):
        """Initialise Floor with (by Level-Main):
        Parameters:
            canvas - canvas of the Main frame;
            width_fl - max width of floor;
            height_fl - max height of floor;
            level_main - level of the game
            step_main - each step

        Set arguments:
            keep_floor {} - directory to keep each brick.
                            keys are y_coordinates,
                                values - x_coord - keep Path's objects.
            self.monsters - Monsters instance

        Property: path_only - list of path positions [x, y]

        Methods:
            start() - generate floor, draws it, add Monsters.
            generate_floor - draw 10*10 path only, add objects
            add_wall - draw Walls, add objects
            wall_1 - contain grid positions of the floor. Draws wall on each.
            check_cross - check if path could be crossed.
        """
        self.level = level_main
        self.canvas = canvas_main
        self.width_fl = width_fl_main
        self.height_fl = height_fl_main
        self.step = step_main
        self.keep_floor = {}
        self.monsters = None
        self.path_only = None
        self.start()

    def start(self):
        """Initial map."""
        self.generate_floor()
        self.wall_1()
        self.path_only = self.path_only_cal()
        self.monsters = Monsters(self.canvas, self.level, self.path_only)
        self.monsters.add_skeletons(3)
        self.monsters.add_boss()
        self.monsters.first_draw_monsters()

    def path_only_cal(self):
        """Get only path positions."""
        path_pos = []
        for value in self.keep_floor.values():
            for each_obj in value.values():
                if each_obj.type == "path":
                    x_num = each_obj.get_x()
                    y_num = each_obj.get_y()

                    path_pos.append([x_num, y_num])
        return path_pos

    def generate_floor(self):
        """Generation of floor."""
        y_position = 0
        while y_position < self.height_fl:
            self.keep_floor[y_position] = {}
            x_position = 0
            while x_position < self.width_fl:
                tile = Path(self.canvas, x_position, y_position)
                new_pair = {x_position: tile}
                self.keep_floor[y_position].update(new_pair)
                x_position += self.step
            y_position += self.step

    def add_wall(self, raw, column):
        """Adds walls to the floor."""
        self.keep_floor[raw][column] = Wall(self.canvas, column, raw)

    def wall_1(self):
        """Map of the walls."""
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
            row_cor = (row * self.step) - self.step
            col_cor = (col * self.step) - self.step
            self.add_wall(row_cor, col_cor)

    def check_cross(self, x_f, y_f):
        """Checks what type of object on that position."""
        obj = [x_f, y_f]
        path = self.path_only
        if obj in path:
            return True
        return False
