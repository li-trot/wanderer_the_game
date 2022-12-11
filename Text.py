"""Class Text."""

from tkinter import CENTER


class Text():
    """Text information about hero."""

    def __init__(self, canvas, hero, width, height):
        """Init Text field."""
        self.canvas = canvas
        self.hero = hero
        self.height = height+15
        self.width = width/2

    def print_text(self, level):
        """Print text."""
        text_gen = (f"Hero (level {level}) HP:{self.hero.max_health}/{self.hero.health} "
                    f"| DP:{self.hero.defend} | SP:{self.hero.strike}")
        self.canvas.create_text(
            self.width,
            self.height,
            text=text_gen,
            fill="black",
            font=("tkDefaeultFont 24")
        )
