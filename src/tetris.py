from grid import OccupiedPositionException
from grid import TetrisGrid
from grid import TetrisVirtualGrid
from shape import Shape
from shape import create_shape
from shape import rotate

import random
import typing


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (0, 0, 0)


class Tetris:
    def __init__(self) -> None:
        self.grid = TetrisGrid(10, 10)
        self.virtual_grid = TetrisVirtualGrid(10, 10, self.grid.sync)
        self.shape_generator = RandomShapeGenerator(0, 4)

        self.active_shape: Shape = None
        self.held_shape: Shape = None
        self.is_shape_exchanged = False

        self.score = 0
        self.level = 0

    def play(self) -> None:
        """play starts the game loop
        Initialize the grid and the active shape
        Start gravity thread to move the active shape down
        """
        self.active_shape: Shape = self.shape_generator.generate()
        self.virtual_grid.add_shape(self.active_shape)

    def gameover(self) -> None:
        """gameover ends the game, output the score and level"""
        pass

    def move_left(self):
        """move the active shape left direction"""
        self.__move(col=-1)

    def move_right(self):
        """move the active shape right direction"""
        self.__move(col=1)

    def move_down(self):
        """move the active shape down direction"""
        self.__move(row=1, onfail=self.__add_new_shape)

    def move_ground(self):
        """move the active shape to the ground"""
        while self.__move(row=1, onfail=self.__add_new_shape):
            pass

    def rotate(self):
        """rotates the active shape in the grid"""
        try:
            rotated_shape = rotate(self.active_shape)
            self.virtual_grid.replace_shape(self.active_shape, rotated_shape)
            self.active_shape = rotated_shape
        except OccupiedPositionException:
            pass

    def hold(self) -> None:
        """hold the active shape, If there is already a held shape, swap them"""
        if self.is_shape_exchanged:
            return

        try:
            # create tmp held shape variable to not set held shape when replace fails
            tmp_held_shape = self.held_shape
            if tmp_held_shape is None:
                tmp_held_shape = self.shape_generator.generate()

            self.virtual_grid.replace_shape(self.active_shape, tmp_held_shape)

            self.held_shape = tmp_held_shape
            self.active_shape, self.held_shape = self.held_shape, self.active_shape
            self.is_shape_exchanged = True
        except OccupiedPositionException:
            pass

    def __move(self, row=0, col=0, onfail: typing.Callable = None) -> bool:
        try:
            self.virtual_grid.relocate_shape(self.active_shape, row, col)
            return True
        except OccupiedPositionException:
            onfail()
            return False

    def __add_new_shape(self):
        try:
            self.active_shape = self.shape_generator.generate()
            self.virtual_grid.add_shape(self.active_shape)
            self.is_shape_exchanged = False
        except OccupiedPositionException:
            self.gameover()


class RandomShapeGenerator:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.shapes = ['T', "Z", "L", "I", "S"]
        self.colors = [RED, BLUE, YELLOW, WHITE]

    def generate(self) -> Shape:
        shape_type = random.choice(self.shapes)
        shape_color = random.choice(self.colors)

        return create_shape(shape_type, self.row, self.col, shape_color)


def render(m, title=None):
    print()
    print(title)
    for row in m:
        for col in row:
            if col is None:
                print('-', end=' ')
            else:
                print('U', end=' ')
        print()


if __name__ == "__main__":
    tetris = Tetris()
    tetris.play()
    render(tetris.grid.get_map())
    tetris.move_down()
    render(tetris.grid.get_map())
    tetris.move_ground()
    render(tetris.grid.get_map())
    tetris.move_right()
    render(tetris.grid.get_map())
    tetris.hold()
    render(tetris.grid.get_map(), "HOLD")
    tetris.hold()
    render(tetris.grid.get_map(), "HOLD")
    tetris.hold()
    render(tetris.grid.get_map(), "HOLD")
    tetris.move_ground()
    render(tetris.grid.get_map(), "GROUND")
    tetris.hold()
    render(tetris.grid.get_map(), "HOLD")
    tetris.rotate()
    render(tetris.grid.get_map(), "ROTATE")
    tetris.move_right()
    render(tetris.grid.get_map(), "RIGHT")
