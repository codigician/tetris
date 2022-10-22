import threading
from .shape import Shape
from .shape import Unit

import typing


class OccupiedPositionException(Exception):
    pass


class TetrisVirtualGrid:
    def __init__(self, row: int, col: int) -> None:
        self.lock = threading.Lock()
        self.map: typing.List[typing.List[Unit]] = [
            [None for _ in range(col)] for _ in range(row)]

    def add_shape(self, shape: Shape):
        self.lock.acquire()

        if not self.__is_shape_placeable(shape):
            self.lock.release()
            raise OccupiedPositionException()

        for unit in shape.units:
            self.map[unit.row][unit.col] = unit

        self.lock.release()

    def relocate_shape(self, shape: Shape, row: int, col: int):
        self.lock.acquire()

        self.__remove_shape(shape)

        if not self.__is_shape_placeable(shape, row, col):
            self.__place_shape(shape)
            self.lock.release()
            raise OccupiedPositionException()

        self.__place_shape(shape, row, col)
        self.lock.release()
        self.solidify()

    def replace_shape(self, shape: Shape, relocated: Shape):
        self.lock.acquire()

        self.__remove_shape(shape)

        if not self.__is_shape_placeable(relocated):
            self.__place_shape(shape)  # old shape
            self.lock.release()
            raise OccupiedPositionException()

        self.__place_shape(relocated)
        self.lock.release()
        self.solidify()

    def __is_shape_placeable(self, shape: Shape, row=0, col=0) -> bool:
        for unit in shape.units:
            if self.map[unit.row + row][unit.col + col] is not None:
                return False
        return True

    def __remove_shape(self, shape: Shape):
        for unit in shape.units:
            self.map[unit.row][unit.col] = None

    def __place_shape(self, shape: Shape, row=0, col=0):
        for unit in shape.units:
            self.map[unit.row + row][unit.col + col] = unit

    def solidify(self):
        self.lock.acquire()
        self.lock.release()
