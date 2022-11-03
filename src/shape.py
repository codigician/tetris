import typing


class Unit:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col


class Shape:
    def __init__(self, start_row: int, start_col: int, color=(0, 0, 0)) -> None:
        self.start_row = start_row
        self.start_col = start_col

        self.color: typing.Tuple(int, int, int) = color
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
    def __init__(self, start_row: int, start_col: int, color=(0, 0, 0)) -> None:
        self.start_row = start_row
        self.start_col = start_col

        self.units = [
            Unit(start_row, start_col),
            Unit(start_row + 1, start_col),
            Unit(start_row + 2, start_col),
            Unit(start_row+3, start_col),
        ]

        self.color: typing.Tuple(int, int, int) = color
        self.grid = [[None for _ in range(4)] for _ in range(4)]

        for unit in self.units:
            self.grid[unit.row - start_row][unit.col - start_col] = unit


class LShape(Shape):
    def __init__(self, start_row: int, start_col: int, color=(0, 0, 0)) -> None:
        self.start_row = start_row
        self.start_col = start_col

        self.units = [
            Unit(start_row, start_col),
            Unit(start_row+1, start_col),
            Unit(start_row + 2, start_col),
            Unit(start_row + 2, start_col + 1),
        ]

        self.color: typing.Tuple(int, int, int) = color
        self.grid = [[None for _ in range(3)] for _ in range(3)]

        for unit in self.units:
            self.grid[unit.row - start_row][unit.col - start_col] = unit


class TShape(Shape):
    def __init__(self, start_row: int, start_col: int, color=(0, 0, 0)) -> None:
        self.start_row = start_row
        self.start_col = start_col

        self.units = [
            Unit(start_row, start_col),
            Unit(start_row, start_col + 1),
            Unit(start_row, start_col + 2),
            Unit(start_row + 1, start_col + 1),
        ]

        self.color: typing.Tuple(int, int, int) = color
        self.grid = [[None for _ in range(3)] for _ in range(3)]

        for unit in self.units:
            self.grid[unit.row - start_row][unit.col - start_col] = unit


class ZShape(Shape):
    def __init__(self, start_row: int, start_col: int, color=(0, 0, 0)) -> None:
        self.start_row = start_row
        self.start_col = start_col

        self.units = [
            Unit(start_row, start_col),
            Unit(start_row, start_col + 1),
            Unit(start_row + 1, start_col + 1),
            Unit(start_row + 1, start_col + 2),
        ]

        self.color: typing.Tuple(int, int, int) = color
        self.grid = [[None for _ in range(3)] for _ in range(3)]

        for unit in self.units:
            self.grid[unit.row - start_row][unit.col - start_col] = unit


class SquareShape(Shape):
    def __init__(self, start_row: int, start_col: int, color=(0, 0, 0)) -> None:
        self.start_row = start_row
        self.start_col = start_col

        self.units = [
            Unit(start_row, start_col),
            Unit(start_row, start_col + 1),
            Unit(start_row + 1, start_col),
            Unit(start_row + 1, start_col + 1),
        ]

        self.color: typing.Tuple(int, int, int) = color
        self.grid = [[None for _ in range(2)] for _ in range(2)]

        for unit in self.units:
            self.grid[unit.row - start_row][unit.col - start_col] = unit


def create_shape(type: str, start_row: int, start_col: int, color=(0, 0, 0)) -> Shape:
    if type == "I":
        return IShape(start_row, start_col, color)
    elif type == "L":
        return LShape(start_row, start_col, color)
    elif type == "T":
        return TShape(start_row, start_col, color)
    elif type == "Z":
        return ZShape(start_row, start_col, color)
    elif type == "S":
        return SquareShape(start_row, start_col, color)

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
                    Unit(row + shape.start_row, col + shape.start_col))

    rotated_shape = Shape(shape.start_row, shape.start_col)
    rotated_shape.grid = rotated_grid
    rotated_shape.units = units

    # DEBUG: uncomment to see the rotation
    # print('OLD_SHAPE\n%s\nROTATED_SHAPE\n%s' % (shape.__str__(), rotated_shape.__str__()))
    # print(["{} {}".format(unit.row, unit.col) for unit in rotated_shape.units])
    return rotated_shape
