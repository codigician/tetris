from shape import Shape


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


if __name__ == "__main__":
    print('hello world')
