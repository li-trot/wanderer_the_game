from tkinter import *


class Box(object):
    """Class for drawing a rectangle inside canvas."""

    def __init__(self):
        """Initialise Box with coordinate parameters."""
        self.test_box_x = 0
        self.test_box_y = 0

    def draw(self, canvas_board):
        """Draw rectangle on new position."""
        canvas_board.create_rectangle(0, 0, 600, 600, fill='white')
        canvas_board.create_rectangle(self.test_box_x, self.test_box_y,
                                      self.test_box_x+100, self.test_box_y+100, fill='lime green')


# Create the tk environment as usual
WIDTH = 600
HEIGHT = 600
root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT)

# Creating a box that can draw itself in a certain position
box = Box()

# Create a function that can be called when a key pressing happens


def on_key_press(enter):
    """When arrows are pressed the box moves i appropriate way on 100."""
    if enter.keycode == 38:
        if box.test_box_y - 100 >= 0:
            box.test_box_y = box.test_box_y - 100
    elif enter.keycode == 40:
        if box.test_box_y + 100 <= HEIGHT - 100:
            box.test_box_y = box.test_box_y + 100
    elif enter.keycode == 39:
        if box.test_box_x + 100 <= WIDTH - 100:
            box.test_box_x = box.test_box_x + 100
    elif enter.keycode == 37:
        if box.test_box_x - 100 >= 0:
            box.test_box_x = box.test_box_x - 100
    # and lower if the key that was pressed the down arrow
    # draw the box again in the new position
    box.draw(canvas)


# Tell the canvas that we prepared a function that can deal with the key press events
canvas.bind("<KeyPress>", on_key_press)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

# Draw the box in the initial position
box.draw(canvas)

root.mainloop()
