from shape import Shape
from unit import Unit


class LShape(Shape):
    def __init__(self, start_row, start_col):
        self.squares = [
            Unit(start_row, start_col),
            Unit(start_row, start_col+1),
            Unit(start_row, start_col+2),
            Unit(start_row+1, start_col+2),
        ]
