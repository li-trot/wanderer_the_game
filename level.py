"""Class Level generation."""

from random import randint, choices
from floor import Floor
from hero import Hero
from text import Text


class Level():
    """Class for keeping all assets for the level"""

    def __init__(self, canvas_main, step_main, tile):
        """Initialise class with (by Main):
        canvas_main - Main canvas of the game;
        step_main - step from Main;

        Default sets:
        text_obj - to print text;
        area_number_main - level of game;
        hero_main - hero instance from Main;
        floor - object Floor instance;
        hero_act  -  activate hero on canvas;
        monsters - floor.monsters;

        Methods:
        create_level() - initial function, to create Floor and print info.
        battle(attacking_obj, defender_obj) - returns result - string (kill/dead/next).
        strike_start() - activate by space pressing, inits battle function.
        After victory return listener to previous position, hero can move again. Or ends the level.
        """
        self.canvas = canvas_main
        self.level = 1
        self.step = step_main
        self.width = self.step * 10
        self.height = self.step * 10
        self.first_tile = tile
        self.hero = None
        self.floor = None
        self.hero_act = None
        self.create_first_level()
        self.monsters = None
        self.bind_key = None
        self.enemy = None

    def create_first_level(self):
        """Create level from the beginning."""
        self.level = 1
        self.add_hero()
        self.text = Text(self.canvas, self.hero, self.width,
                         self.height+30, self.first_tile)
        self.create_new_level()

    def create_new_level(self):
        """Create new level from the beginning."""
        self.canvas.delete("skeleton", "path", "wall", "hero")
        self.floor = Floor(self.canvas, self.step*10,
                           self.step*10, self.level, self.step)
        self.text.new_level(self.level)
        self.canvas.after(3400, self.hero.draw)
        self.canvas.after(3400, self.text.hero_info)
        self.canvas.after(3500, self.bind_proc)

    def bind_proc(self):
        """Allows user to move hero."""
        self.canvas.bind("<KeyPress>", self.on_key_press)
        self.canvas.focus_set()

    def on_key_press(self, enter):
        """When arrows are pressed the box moves i appropriate way on 100."""
        # go up
        if self.floor is False:
            self.canvas.unbind("<Keypress>")

        if self.hero.move is False:
            self.text.print("You can't run away. Fight! Hit the space!")

        elif enter.keycode in (38, 87):
            self.hero.image = self.hero.hero_up
            if self.hero.y_pos - self.step >= 0:
                if self.floor.check_cross(self.hero.x_pos, self.hero.y_pos - self.step):
                    self.hero.y_pos = self.hero.y_pos - self.step
        # go down
        elif enter.keycode in (40, 83):
            self.hero.image = self.hero.hero_down
            if self.hero.y_pos + self.step <= self.height - self.step:
                if self.floor.check_cross(self.hero.x_pos, self.hero.y_pos + self.step):
                    self.hero.y_pos = self.hero.y_pos + self.step
        # go right
        elif enter.keycode in (39, 68):
            self.hero.image = self.hero.hero_right
            if self.hero.x_pos + self.step <= self.width - self.step:
                if self.floor.check_cross(self.hero.x_pos + self.step, self.hero.y_pos):
                    self.hero.x_pos = self.hero.x_pos + self.step
        # go left
        elif enter.keycode in (37, 65):
            self.hero.image = self.hero.hero_left
            if self.hero.x_pos - self.step >= 0:
                if self.floor.check_cross(self.hero.x_pos - self.step, self.hero.y_pos):
                    self.hero.x_pos = self.hero.x_pos - self.step
        # and lower if the key that was pressed the down arrow
        self.canvas.delete("hero")
        self.hero.draw()
        self.check_monster()

    def check_monster(self):
        """Checks if there is a monster on hero position, and start the batle."""
        monster = self.floor.monsters.monster_here
        if self.hero.position not in monster:
            pass
        elif self.hero.position in monster:
            self.canvas.bind("<KeyPress>", self.hit_monster)
            self.canvas.focus_set()
            self.text.delete_smth("hero_info")
            self.hero.move = False
            self.who_is_enemy()

    def who_is_enemy(self):
        """Checks who is on the same position with hero
        and returns object of the enemy."""
        try:
            if self.floor.monsters.boss.position is not False:
                boss_pos = self.floor.monsters.boss.position
                if boss_pos == self.hero.position:
                    self.enemy = self.floor.monsters.boss
        except AttributeError:
            pass

        for num, skel in enumerate(self.floor.monsters.keep_skeletons):
            if skel.position == self.hero.position:
                self.enemy = self.floor.monsters.keep_skeletons[num]
        self.text.fight_info(self.enemy)

    def hit_monster(self, enter):
        """Event listener for attack."""
        if enter.keycode == 32:
            if self.enemy is not None:
                self.strike_start()

    def strike_start(self):
        """Start fight with monster and take result of fighting.."""
        result = self.battle(self.hero, self.enemy)

        # next level
        if result == "next":
            self.text.delete_smth("fight_info")
            self.hero.move = False
            self.canvas.unbind("<KeyPress>")
            self.floor = None
            self.level += 1
            self.restore_hero()
            self.create_new_level()

        elif result == "kill":
            self.canvas.bind("<KeyPress>", self.hit_monster)
            self.canvas.focus_set()
            self.text.delete_smth("fight_info")
            self.text.hero_info()
            self.hero.move = True
            self.enemy = False
            self.canvas.bind("<KeyPress>", self.on_key_press)
            self.canvas.focus_set()

        elif result == "counter":
            result_monster = self.battle(self.enemy, self.hero)

            if result_monster == "attack":
                self.canvas.bind("<KeyPress>", self.hit_monster)
                self.canvas.focus_set()
                self.text.print("You can attack!Hit the space.")

            elif result_monster == "dead":
                self.text.delete_smth("fight_info")
                self.hero.move = False
                self.canvas.unbind("<Keypress")
                self.canvas.delete("hero", "wall", "path", "skeleton", "boss")
                del self.floor
                del self.hero
                self.text.game_over()

    def calculate_points(self, attacking_cl, defender_cl):
        """Calculates points of attack.
        And decrise health amount of a defender, if his defend points are less."""
        self.canvas.unbind("<KeyPress>")
        ran_num = randint(1, 6)
        strike_value = 2 * ran_num + attacking_cl.strike
        if strike_value > defender_cl.defend:
            defender_cl.health = defender_cl.health - \
                (strike_value - defender_cl.defend)
            if defender_cl.type == "Hero":
                color = "red"
            else:
                color = "green"
            self.text.print_points(
                f"-{(strike_value - defender_cl.defend)}", color, self.hero.position)
        self.text.fight_info(self.enemy)

    def battle(self, attacking_cl, defender_cl):
        """On a strike a strike value (SV) is calculated from SP and a d6 doubled.
        The strike is successful if 2 * d6 + SP is higher than the other character's DP.
        On a successful strike the other character's
        HP is decreased by the SV - the other character's DP."""
        self.calculate_points(attacking_cl, defender_cl)

        if defender_cl.type == "Hero":
            if defender_cl.is_alive() is False:
                return "dead"
            return "attack"

        # hero attacks
        if defender_cl.type != "Hero":
            if defender_cl.is_alive() is True:
                return "counter"

            # kill monster
            if defender_cl.is_alive() is False:
                # kill the boss
                if defender_cl.type == "Boss":
                    # and has key
                    if self.hero.key is True:
                        return "next"
                    # and no key
                    # delete boss
                    self.hero.kill_boss = True
                    self.canvas.delete("boss")
                    self.floor.monsters.boss = False
                    return "kill"

                # kill skeleton
                if defender_cl.type == "Skeleton":
                    # if get the key
                    if defender_cl.key is True:
                        self.hero.key = True
                        # and has killed the boss
                        if self.hero.kill_boss is True:
                            return "next"
                    # hasn't killed the boss
                    self.canvas.delete("skeleton")
                    self.floor.monsters.drawing_process()
                    for num, obj in enumerate(self.floor.monsters.keep_skeletons):
                        if obj == defender_cl:
                            del self.floor.monsters.keep_skeletons[num]
                    return "kill"

    def add_hero(self):
        """Calculate Hero info - FIRST TIME."""
        health_g = 20 + (3 * randint(1, 6))
        defeat_g = 2 * randint(1, 6)
        strike_g = 5 + randint(1, 6)
        self.hero = Hero(self.canvas, health_g, defeat_g, strike_g)

    def restore_hero(self):
        """Restoring health on starting new level."""
        chances = [self.hero.max_health,
                   int(self.hero.max_health/3),
                   int(self.hero.max_health/100*10)]
        random_chance = choices(chances, weights=(10, 40, 50), k=1)
        self.hero.health += random_chance[0]
        if self.hero.health > self.hero.max_health:
            self.hero.health = self.hero.max_health
        self.hero.level = self.level
        self.hero.position = [0, 0]
        self.hero.move = True
        self.hero.kill_boss = False
        self.hero.key = False
        self.hero.image = self.hero.hero_down
        self.enemy = None
