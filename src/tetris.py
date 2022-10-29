from shape import Shape
from shape import create_shape
import random

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (0, 0, 0)


class Tetris:
    def __init__(self) -> None:
        self.active_shape: Shape = None
        self.hold_shape: Shape = None

        self.grid = None
        self.score = 0
        self.level = 0

    def play(self) -> None:
        """play starts the game loop
        Initialize the grid and the active shape
        Start gravity thread to move the active shape down
        """
        pass

    def gameover(self) -> None:
        """gameover ends the game
        output the score and level
        """
        pass

    def move(self, direction: str) -> None:
        """move the active shape in the given direction

        Args:
            direction (str): left, right, down, or rotate
        """
        pass

    def hold(self) -> None:
        """hold the active shape
        If there is already a held shape, swap them
        """
        pass


class RandomShapeGenerator:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.shapes = ['T', "Z", "L", "I", "Square"]
        self.colors = [RED, BLUE, YELLOW, WHITE]

    def generate_random_shape(self) -> Shape:
        shape_type = random.choice(self.shapes)
        shape_color = random.choice(self.colors)

        return create_shape(shape_type, self.row, self.col, shape_color)


if __name__ == "__main__":
    print('hello world')
