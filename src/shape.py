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
    unit_row_array = []
    unit_col_array = []

    for unit in shape.units:
        unit_row_array.append(unit.row)
        unit_col_array.append(unit.col)

    row_diff = max(unit_row_array) - min(unit_row_array) + 1
    col_diff = max(unit_col_array) - min(unit_col_array) + 1
    min_value = min(min(unit_row_array), min(unit_col_array))
    dimension = max(row_diff, col_diff)

    grid = [[None for _ in range(dimension)] for _ in range(dimension)]
    second_grid = [[None for _ in range(dimension)] for _ in range(dimension)]

    for unit in shape.units:
        grid[unit.row-min_value][unit.col-min_value] = unit

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            second_grid[col][len(grid)-1-row] = grid[row][col]

    """
            second[0][2]   grid[0][0]
            second[1][2]   grid[0][1]
            second[2][2]   grid[0][2]

            second[0][1]   grid[1][0]
            second[1][1]   grid[1][1]
            second[2][0]   grid[1][2]
    """

    new_shape = Shape(0, 0)

    for row in range(len(second_grid)):
        for col in range(len(second_grid[row])):
            if second_grid[row][col] != None:
                new_shape.units.append(Unit(row + min_value, col + min_value))

    return new_shape
