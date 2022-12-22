"""The Characters."""


class Character():
    """The Characters
    Every character has a (max and current) health point (HP), a defend (DP) and strike point (SP).
    These values can change during the game.
    When a character's health point is 0 or below, it is dead.
    It disappears from the area.
    If its the hero, it is the end of the game."""

    def __init__(self, canvas_main, type_char, max_health, defend, strike):
        """Initialise element.
        canvas -  main canvas of the game
        type_char - type of the character ("Hero"/"Boss"/"Skeleton")
        max_health  - integer
        health - integer - actual health
        defend  - integer
        strike - integer
        x_pos = 0 - integer
        y_pos = 0 - integer
        level = 0 - integer

        Property:
        position - returns [x, y]

        Property setter:
        position = [x, y]

        Methods:
        is_alive - returns Boolean;
        type_is - returns type string
        """
        self.canvas = canvas_main
        self.type = type_char
        self.max_health = max_health
        self.health = max_health
        self.defend = defend
        self.strike = strike
        self.x_pos = 0
        self.y_pos = 0
        self.level = 1

    @property
    def position(self):
        """Returns [x, y] position. """
        return [self.x_pos, self.y_pos]

    @position.setter
    def position(self, position_pass):
        """Sets x and y position from [x, y] list."""
        self.x_pos, self.y_pos = position_pass

    def is_alive(self):
        """Returns Boolean - whether the character is alive or not."""
        if self.health <= 0:
            return False
        return True
