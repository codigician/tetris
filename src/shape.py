import typing


class Unit:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col


class Shape:
    def __init__(self, start_row: int, start_col: int, color=(0, 0, 0)) -> None:
        self.color: typing.Tuple(int, int, int) = color
        self.units: typing.List[Unit] = []


class IShape(Shape):
    def __init__(self, start_row: int, start_col: int) -> None:
        self.units = [
            Unit(start_row, start_col),
            Unit(start_row + 1, start_col),
            Unit(start_row + 2, start_col),
            Unit(start_row+3, start_col),
        ]


class LShape(Shape):
    def __init__(self, start_row: int, start_col: int) -> None:
        self.units = [
            Unit(start_row, start_col),
            Unit(start_row+1, start_col),
            Unit(start_row + 2, start_col),
            Unit(start_row + 2, start_col + 1),
        ]


class TShape(Shape):
    def __init__(self, start_row: int, start_col: int) -> None:
        self.units = [
            Unit(start_row, start_col),
            Unit(start_row, start_col + 1),
            Unit(start_row, start_col + 2),
            Unit(start_row + 1, start_col + 1),
        ]


class ZShape(Shape):
    def __init__(self, start_row: int, start_col: int) -> None:
        self.units = [
            Unit(start_row, start_col),
            Unit(start_row, start_col + 1),
            Unit(start_row + 1, start_col + 1),
            Unit(start_row + 1, start_col + 2),
        ]


class SquareShape(Shape):
    def __init__(self, start_row: int, start_col: int) -> None:
        self.units = [
            Unit(start_row, start_col),
            Unit(start_row, start_col + 1),
            Unit(start_row + 1, start_col),
            Unit(start_row + 1, start_col + 1),
        ]


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


"""
    U - -
    U - -
    U U -

    U U U
    U - -
    - - -

    - U U
    - - U
    - - U

    - - -
    - - U
    U U U
    """


def rotate(shape: Shape) -> Shape:
    unit_row_array = [unit.row for unit in shape.units]
    unit_col_array = [unit.col for unit in shape.units]
    max_row, max_col = max(unit_row_array), max(unit_col_array)
    min_row, min_col = min(unit_row_array), min(unit_col_array)

    row_diff = max_row - min_row + 1
    col_diff = max_col - min_col + 1
    min_value = min(min_row, min_col)
    dimension = max(row_diff, col_diff)

    grid = [[None for _ in range(dimension)] for _ in range(dimension)]
    rotated_grid = [[None for _ in range(dimension)]
                    for _ in range(dimension)]

    for unit in shape.units:
        grid[unit.row-min_value][unit.col-min_value] = unit

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            rotated_grid[col][len(grid)-1-row] = grid[row][col]

    rotated_shape = Shape(0, 0)

    for row in range(len(rotated_grid)):
        for col in range(len(rotated_grid[row])):
            if rotated_grid[row][col]:
                rotated_shape.units.append(
                    Unit(row + min_value, col + min_value))

    return rotated_shape
