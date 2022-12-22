"""Monsters generation."""

from tkinter import NW
import random
from skeleton import Skeleton
from boss import Boss


class Monsters():
    """Class to hold Monsters.
    (by Floor_Level_Main)
    creates and keep - Skeleton, Boss instances"""

    def __init__(self, canvas_main, level_floor_main, path_only_floor):
        """Initialise with (by Floor-Level-Main):
        canvas - main canvas;
        level_floor_main - level of the game;
        path_only_floor - property of the Floor instance, without walls.

        Sets:
        canvas = canvas_main
        level_area = level_floor_main
        path_only = path_only_floor
        keep_skeletons - [] - instances of Skeletons
        boss - instance of Boss

        Properties:
        level_monster - calculate random level.
        monster_here - generate positions of the all monsters.

        Methods:
        add_skeletons(number) - generate and keep number amount of Skeleton's instances.
        add_boss - create Boss instance.
        first_draw_monsters - gives first positions on canvas to monsters and draw them.
        drawing_process - draws monsters according to their actual position.
        """
        self.canvas = canvas_main
        self.level_area = level_floor_main
        self.path_only = path_only_floor
        self.keep_skeletons = []
        self.boss = None

    @property
    def level_monster(self):
        """Calculate the level of the monsters."""
        chances = [self.level_area, self.level_area+1, self.level_area+2]
        random_ind = random.choices(chances, weights=(50, 40, 10), k=1)
        return random_ind[0]

    @property
    def monster_here(self):
        """Return list of x, y positions of the monsters."""
        list_positions = []
        try:
            if self.boss.is_alive() is True:
                list_positions.append(self.boss.position)
        except (ValueError, AttributeError):
            pass

        for obj in self.keep_skeletons:
            try:
                if obj.is_alive() is True:
                    list_positions.append(obj.position)
            except (ValueError, AttributeError):
                pass
        return list_positions

    def add_skeletons(self, num):
        """Add monsters on the floor.
        Argument: number - how many monsters add."""
        while num > 0:
            health_max = 2 * self.level_monster * random.randint(1, 6)
            defend = self.level_monster / 2 * random.randint(1, 6)
            strike = self.level_monster * random.randint(1, 6)
            skeleton = Skeleton(self.canvas, health_max, defend, strike, num)
            if num == 1:
                skeleton.key = True
            self.keep_skeletons.append(skeleton)
            num -= 1

    def add_boss(self):
        """Add Boss to the list."""
        health_max = 2 * self.level_monster * random.randint(1, 6)
        defend = (self.level_monster / 2 * random.randint(1, 6)) + \
            (random.randint(1, 6)/2)
        strike = self.level_monster * random.randint(1, 6) + self.level_monster
        self.boss = Boss(self.canvas, health_max, defend, strike)

    def first_draw_monsters(self):
        """Generate spots for monsters and drawing them first time."""
        # get list of available positions
        floor_available = self.path_only[:]
        try:
            # skip the hero position
            floor_available.remove([0, 0])
        except ValueError:
            pass
        # take random index from available positions
        for i in range(len(floor_available)):
            spots = random.sample(floor_available, len(self.keep_skeletons)+1)
        self.boss.x_pos = spots[0][0]
        self.boss.y_pos = spots[0][1]
        for_sk_spots = spots[1:]
        for num, skeleton in enumerate(self.keep_skeletons):
            skeleton.x_pos = for_sk_spots[num][0]
            skeleton.y_pos = for_sk_spots[num][1]
        self.canvas.after(3000, self.drawing_process)

    def drawing_process(self):
        """Draw monsters on spots from the list, Boss is first. Monster with keys is second"""
        try:
            if self.boss.is_alive() is True:
                self.canvas.create_image(
                    self.boss.x_pos, self.boss.y_pos, image=self.boss.image, anchor=NW, tag="boss")
        except (ValueError, AttributeError):
            pass

        for skelet in self.keep_skeletons:
            try:
                if skelet.is_alive() is True:
                    self.canvas.create_image(
                        skelet.x_pos, skelet.y_pos, image=skelet.image, anchor=NW, tag="skeleton")
            except (ValueError, AttributeError):
                pass
