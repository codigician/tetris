from grid import OccupiedPositionException
from grid import TetrisGrid
from grid import TetrisVirtualGrid
from shape import Shape
from shape import create_shape
from shape import rotate
from enum import Enum

import threading
import time
import random
import typing


BLACK = (0, 0, 0)


class GameState(Enum):
    PAUSE = 1
    PLAYING = 2
    GAMEOVER = 3


class Tetris:
    def __init__(self, grid, virtual_grid, shape_generator, gravity) -> None:
        self.grid = grid
        self.virtual_grid = virtual_grid
        self.shape_generator = shape_generator

        self.score = 0
        self.level = (self.score+1) / 1000

        self.gravity = gravity
        self.gravity.set_speed(speed=1 - 2*(self.level / 10))

        self.gravity.set_move_down(self.move_down)

        self.active_shape: Shape = None
        self.held_shape: Shape = None
        self.is_shape_exchanged = False

        self.state: GameState = None

    def play(self) -> None:
        """play starts the game loop
        Initialize the grid and the active shape
        Start gravity thread to move the active shape down
        """
        self.state = GameState.PLAYING
        self.active_shape: Shape = self.shape_generator.generate()
        self.virtual_grid.add_shape(self.active_shape)
        self.gravity.start()

    def pause(self):
        self.state = GameState.PAUSE

        self.gravity.pause()

    def resume(self):
        if self.state != GameState.PAUSE:
            raise RuntimeError("resume only works if the game is paused")

        self.state = GameState.PLAYING
        self.gravity.resume()

    def gameover(self) -> None:
        """gameover ends the game, output the score and level"""
        self.state = GameState.GAMEOVER
        self.gravity.terminate()

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

    def explode(self):
        counter = 0
        for i in range(len(self.virtual_grid.map)):
            if None not in self.virtual_grid.map[i]:
                counter += 1
                self.virtual_grid.shift_down_rows(idx=i)
        self.score = self.calculate_score(counter)

    def calculate_score(self, counter):
        self.score += (counter**2) * 20
        return self.score

    def __move(self, row=0, col=0, onfail: typing.Callable = None) -> bool:
        try:
            self.virtual_grid.relocate_shape(self.active_shape, row, col)
            return True
        except OccupiedPositionException:
            if onfail is not None:
                onfail()
            return False

    def __add_new_shape(self):
        try:
            self.explode()
            self.active_shape = self.shape_generator.generate()
            self.virtual_grid.add_shape(self.active_shape)
            self.is_shape_exchanged = False
        except OccupiedPositionException:
            self.gameover()


class Gravity(threading.Thread):
    def __init__(self, move_down: typing.Callable = None) -> None:
        super().__init__(None, None, 'Gravity', None, None, daemon=True)

        self.__playing = True
        self.__pause = False
        self.__speed = 1
        self.__move_down = move_down

    def run(self) -> None:
        while self.__playing:
            while self.__pause:
                pass

            if self.__move_down is not None:
                self.__move_down()

            time.sleep(self.__speed)

    def set_speed(self, speed):
        self.__speed = speed

    def set_move_down(self, move_down):
        self.__move_down = move_down

    def pause(self):
        self.__pause = True

    def resume(self):
        self.__pause = False

    def terminate(self):
        self.__playing = False


class RandomShapeGenerator:
    def __init__(self, row: int, col: int, colors) -> None:
        self.row = row
        self.col = col
        self.shapes = ['T', "Z", "L", "I", "S"]
        self.colors = colors

    def generate(self) -> Shape:
        shape_type = random.choice(self.shapes)
        color = random.choice(self.colors)

        return create_shape(shape_type, self.row, self.col, color)


class GameRenderer(threading.Thread):
    def __init__(self, grid) -> None:
        super().__init__(None, None, 'GameRenderer', None, None, daemon=True)

        self.playing = True
        self.speed = 1/60
        self.grid = grid

    def run(self) -> None:
        while self.playing:
            self.render()
            time.sleep(self.speed)

    def render(self):
        print()
        for row in self.grid.get_map():
            for col in row:
                if col is None:
                    print('-', end=' ')
                else:
                    print('U', end=' ')
            print()


if __name__ == "__main__":
    tetris = Tetris()
    tetris.play()

    renderer = GameRenderer(tetris.grid)
    renderer.start()

    while True:
        choice = input()
        if choice == 'q':
            renderer.playing = False
            break

        if choice == 'a':
            tetris.move_left()
        elif choice == 'd':
            tetris.move_right()
        elif choice == 's':
            tetris.move_down()
        elif choice == 'r':
            tetris.rotate()
        elif choice == 'g':
            tetris.move_ground()
        elif choice == 'h':
            tetris.hold()
