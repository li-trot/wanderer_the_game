"""The Characters."""


class Character():
    """The Characters
    Every character has a (max and current) health point (HP), a defend (DP) and strike point (SP).
    These values can change during the game.
    When a character's health point is 0 or below, it is dead.
    It disappears from the area.
    If its the hero, it is the end of the game."""

    def __init__(self, canvas, type_char, max_health, defend, strike):
        """Initialise element."""
        self.canvas = canvas
        self.type_char = type_char
        self.max_health = max_health
        self.health = max_health
        self.defend = defend
        self.strike = strike
        self.x_pos = 0
        self.y_pos = 0

    def is_alive(self):
        """Returns Boolean - whether the character is alive or not."""
        if self.health <= 0:
            return False
        return True

    def type_is(self):
        """Returns type of characters."""
        return self.type_char
