"""Class Text."""

from tkinter import CENTER, NW
from PIL import ImageTk


class Text():
    """Text information about hero."""

    def __init__(self, canvas, hero, width, height, tile):
        """Init Text field. Level generate."""
        self.canvas = canvas
        self.hero = hero
        self.height = height
        self.width = width
        self.num_name = 1
        self.first_tile = tile
        self.first_tile_load = ImageTk.PhotoImage(self.first_tile)

    def hero_info(self):
        """Print text."""
        self.canvas.delete("hero_info", "fight_info")
        text_gen = (f"Hero (level {self.hero.level}) HP:{self.hero.max_health}/{self.hero.health} "
                    f"| DP:{self.hero.defend} | SP:{self.hero.strike} | KEY:{self.hero.key}")
        self.canvas.create_text(
            self.width/2,
            self.height-15,
            text=text_gen,
            fill="black",
            font=("tkDefaeultFont 24"), tag="hero_info"
        )

    def fight_info(self, monster):
        """Print text."""
        self.canvas.delete("hero_info", "fight_info")
        name = monster.type
        text_hero = (f"Hero (level {self.hero.level}) HP:{self.hero.max_health}/{self.hero.health} "
                     f"| DP:{self.hero.defend} | SP:{self.hero.strike}")
        text_enemy = (f"{name} HP:{monster.max_health}/{monster.health} "
                      f"| DP:{monster.defend} | SP:{monster.strike}")
        text_gen = text_hero + "   VS   " + text_enemy
        self.canvas.create_text(
            self.width/2,
            self.height-15,
            text=text_gen,
            fill="red",
            font=("tkDefaeultFont 12"),
            tag="fight_info"
        )

    def game_over(self):
        """Print text "game over"."""
        text_gen = "GAME OVER"
        self.canvas.create_rectangle(
            0, 0, self.width, self.height, fill="grey")
        self.canvas.create_text(
            self.width/2,
            self.height/2,
            text=text_gen,
            fill="white",
            font=("tkDefaeultFont 40"), tag="game_over"
        )

    def print(self, sample, color="red"):
        """Print passed text."""
        tag_name = f"pr{self.num_name}"
        self.canvas.create_text(
            self.width/2,
            self.height/2,
            text=sample,
            fill=color,
            font=("tkDefaeultFont 20"),
            tag=tag_name
        )
        self.canvas.after(500, self.move_up, tag_name)
        self.canvas.after(3500, self.delete_smth, tag_name)
        self.num_name += 1

    def delete_smth(self, what_del):
        """Deletes from canvas object."""
        self.canvas.delete(what_del)

    def move_up(self, what_move):
        """Moving text up."""
        x = 0
        y = -20
        self.canvas.move(what_move, x, y)
        self.canvas.after(1000, self.move_up, what_move)

    def new_level(self, level):
        """Creates info about new level"""
        self.canvas.create_rectangle(0, 0,
                                     self.width, self.height,
                                     fill="grey", tag="load")
        self.canvas.create_image(
            self.width/2, self.height/2, image=self.first_tile_load, anchor=CENTER, tag="load")
        self.canvas.create_text(self.width/2, self.height/2 + 100, anchor=CENTER,
                                text=(f"Level {level}"), fill="white",
                                font=("tkDefaeultFont 40"), tag="load")
        self.canvas.after(3000, self.delete_smth, "load")

    def print_points(self, points, color, position):
        """Print passed text."""
        tag_name = f"points{self.num_name}"
        width, height = position
        if color == "green":
            width += 40
        self.canvas.create_text(
            width,
            height,
            text=points,
            fill=color,
            font=("tkDefaeultFont 24"),
            tag=tag_name,
            anchor=NW
        )
        self.canvas.after(1000, self.move_up, tag_name)
        self.canvas.after(2500, self.delete_smth, tag_name)
        self.num_name += 1
