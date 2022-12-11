"""Floor class. To generate 10*10 tiles floor."""
from tkinter import NW
from Path import Path
from Wall import Wall
from Skeleton import Skeleton
from Boss import Boss
import random


class Floor():
    """Class for generation floor 10*10 Path bricks."""

    def __init__(self, canvas, width_fl, height_fl, level):
        """Initialise Floor with:
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
        self.level = level
        self.canvas = canvas
        self.width_fl = width_fl
        self.height_fl = height_fl
        self.width_step = int(self.width_fl/10)
        self.height_step = int(self.height_fl/10)
        self.keep_floor = {}
        self.generate_floor()
        self.keep_monsters = []
        self.boss = None
        self.monster_here = []

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
                x_position += self.width_step
            y_position += self.height_step

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
            row_cor = (row * self.width_step) - self.width_step
            col_cor = (col * self.width_step) - self.height_step
            self.add_wall(row_cor, col_cor)

    def check_cross(self, x_f, y_f):
        """Checks what type of object on that position."""
        obj = [x_f, y_f]
        path = self.path_only()
        if obj in self.monster_here:
            return False
        if obj in path:
            return True
        return False

    def add_monsters(self, num):
        """Add monsters on the floor.
        Argument: number - how many monsters add."""
        health_max = 2 * self.level * random.randint(1, 6)
        defend = self.level / 2 * random.randint(1, 6)
        strike = self.level * random.randint(1, 6)
        while num > 0:
            skeleton = Skeleton(self.canvas, health_max, defend, strike)
            self.keep_monsters.append(skeleton)
            num -= 1

    def add_boss(self):
        """Add Boss to the list."""
        health_max = 2 * self.level * random.randint(1, 6)
        defend = (self.level / 2 * random.randint(1, 6)) + \
            (random.randint(1, 6)/2)
        strike = self.level * random.randint(1, 6) + self.level
        self.boss = Boss(self.canvas, health_max, defend, strike)

    def create_monsters(self):
        """Create Monsters object."""
        floor_available = self.path_only()
        try:
            floor_available.remove([0, 0])
        except ValueError:
            pass
        for i in range(len(floor_available)):
            spots = random.sample(floor_available, len(self.keep_monsters)+1)
        for num, monster in enumerate(self.keep_monsters):
            monster.x_pos = spots[num][0]
            monster.y_pos = spots[num][1]
            spot = [monster.x_pos, monster.y_pos]
            self.monster_here.append(spot)
            self.canvas.create_image(
                monster.x_pos, monster.y_pos, image=monster.image, anchor=NW, tag="monster")
        self.canvas.create_image(
            spots[-1][0], spots[-1][1], image=self.boss.image, anchor=NW, tag="boss")
        spo_b = [spots[-1][0], spots[-1][1]]
        self.monster_here.append(spo_b)

    def path_only(self):
        """Get only path positions."""
        path_pos = []
        for key, value in self.keep_floor.items():
            for each_obj in value.values():
                if each_obj.type == "path":
                    x_num = each_obj.get_x()
                    y_num = each_obj.get_y()
                    path_pos.append([x_num, y_num])
        return path_pos
