import typing


class Unit:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col


class Shape:
    def __init__(self, start_row: int, start_col: int, color = (0, 0, 0)) -> None:
        self.color: typing.Tuple(int, int, int) = color
        self.units: typing.List[Unit] = []


class IShape(Shape):
    def __init__(self, start_row: int, start_col: int) -> None:
        self.units = [
            Unit(start_row, start_col),
            Unit(start_row, start_col + 1),
            Unit(start_row, start_col + 2),
            Unit(start_row, start_col + 3),
        ]


class LShape(Shape):
    def __init__(self, start_row: int, start_col: int) -> None:
        self.units = [
            Unit(start_row, start_col),
            Unit(start_row, start_col + 1),
            Unit(start_row, start_col + 2),
            Unit(start_row + 1, start_col + 2),
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
