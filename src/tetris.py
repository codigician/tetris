from shape import Shape, create_shape
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

    def generate_random_shape(self) -> Shape:
        shapes = ['T', "Z", "L", "I", "Square"]
        colors = [red, blue, yellow, white]
        
        shape_type = random.choices(shapes)
        shape_color = random.choices(colors)
        
        return create_shape(shape_type, 0, 4, shape_color)


if __name__ == "__main__":
    print('hello world')
