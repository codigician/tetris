import typing
import random


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
COLORS_LIST = [RED, BLUE, YELLOW, GREEN]


def choice_random_color():
    color = random.choice(COLORS_LIST)
    return color


class Unit:
    def __init__(self, row: int, col: int, color) -> None:
        self.row = row
        self.col = col
        self.color = color


class Shape:
    def __init__(self, start_row: int, start_col: int,) -> None:
        self.start_row = start_row
        self.start_col = start_col

        self.units: typing.List[Unit] = []
        self.grid: typing.List[typing.List[Unit]] = []

    def __str__(self) -> str:
        s = []
        for row in self.grid:
            for unit in row:
                if unit:
                    s.append('U ')
                else:
                    s.append('- ')
            s.append('\n')
        return "".join(s)


class IShape(Shape):
    def __init__(self, start_row: int, start_col: int,) -> None:
        self.start_row = start_row
        self.start_col = start_col

        color = choice_random_color()

        self.units = [
            Unit(start_row, start_col, color),
            Unit(start_row + 1, start_col, color),
            Unit(start_row + 2, start_col, color),
            Unit(start_row+3, start_col, color),
        ]

        self.grid = [[None for _ in range(4)] for _ in range(4)]

        for unit in self.units:
            self.grid[unit.row - start_row][unit.col - start_col] = unit


class LShape(Shape):
    def __init__(self, start_row: int, start_col: int,) -> None:
        self.start_row = start_row
        self.start_col = start_col

        color = choice_random_color()

        self.units = [
            Unit(start_row, start_col, color),
            Unit(start_row+1, start_col, color),
            Unit(start_row + 2, start_col, color),
            Unit(start_row + 2, start_col + 1, color),
        ]

        self.grid = [[None for _ in range(3)] for _ in range(3)]

        for unit in self.units:
            self.grid[unit.row - start_row][unit.col - start_col] = unit


class TShape(Shape):
    def __init__(self, start_row: int, start_col: int,) -> None:
        self.start_row = start_row
        self.start_col = start_col

        color = choice_random_color()

        self.units = [
            Unit(start_row, start_col, color),
            Unit(start_row, start_col + 1, color),
            Unit(start_row, start_col + 2, color),
            Unit(start_row + 1, start_col + 1, color),
        ]

        self.grid = [[None for _ in range(3)] for _ in range(3)]

        for unit in self.units:
            self.grid[unit.row - start_row][unit.col - start_col] = unit


class ZShape(Shape):
    def __init__(self, start_row: int, start_col: int,) -> None:
        self.start_row = start_row
        self.start_col = start_col

        color = choice_random_color()

        self.units = [
            Unit(start_row, start_col, color),
            Unit(start_row, start_col + 1, color),
            Unit(start_row + 1, start_col + 1, color),
            Unit(start_row + 1, start_col + 2, color),
        ]

        self.grid = [[None for _ in range(3)] for _ in range(3)]

        for unit in self.units:
            self.grid[unit.row - start_row][unit.col - start_col] = unit


class SquareShape(Shape):
    def __init__(self, start_row: int, start_col: int,) -> None:
        self.start_row = start_row
        self.start_col = start_col

        color = choice_random_color()

        self.units = [
            Unit(start_row, start_col, color),
            Unit(start_row, start_col + 1, color),
            Unit(start_row + 1, start_col, color),
            Unit(start_row + 1, start_col + 1, color),
        ]

        self.grid = [[None for _ in range(2)] for _ in range(2)]

        for unit in self.units:
            self.grid[unit.row - start_row][unit.col - start_col] = unit


def create_shape(type: str, start_row: int, start_col: int) -> Shape:
    if type == "I":
        return IShape(start_row, start_col)
    elif type == "L":
        return LShape(start_row, start_col)
    elif type == "T":
        return TShape(start_row, start_col)
    elif type == "Z":
        return ZShape(start_row, start_col)
    elif type == "S":
        return SquareShape(start_row, start_col)

    raise NotImplementedError("Shape type not implemented")


def rotate(shape: Shape) -> Shape:
    dimension = len(shape.grid)

    rotated_grid = [[None for _ in range(dimension)] for _ in range(dimension)]

    for row in range(dimension):
        for col in range(dimension):
            rotated_grid[col][dimension-1-row] = shape.grid[row][col]

    units = []
    for row in range(dimension):
        for col in range(dimension):
            if rotated_grid[row][col]:
                units.append(
                    Unit(row + shape.start_row, col + shape.start_col, shape.units[0].color))

    rotated_shape = Shape(
        shape.start_row, shape.start_col, shape.units[0].color)
    rotated_shape.grid = rotated_grid
    rotated_shape.units = units

    # DEBUG: uncomment to see the rotation
    # print('OLD_SHAPE\n%s\nROTATED_SHAPE\n%s' % (shape.__str__(), rotated_shape.__str__()))
    # print(["{} {}".format(unit.row, unit.col) for unit in rotated_shape.units])
    return rotated_shape
