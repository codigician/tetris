import copy
import threading
from shape import Shape
from shape import Unit

import typing


class OccupiedPositionException(Exception):
    pass


class TetrisGrid:
    """TetrisGrid is a class that represents the grid of the game."""

    def __init__(self, row: int, col: int) -> None:
        self.__lock = threading.Lock()
        self.__map: typing.List[typing.List[Unit]] = [
            [None for _ in range(col)] for _ in range(row)]

    def sync(self, virtual: typing.List[typing.List[Unit]]) -> None:
        """sync synchronizes the virtual grid with the real grid.

        Args:
            virtual typing.List[typing.List[Unit]]: The virtual grid.
        """
        self.__lock.acquire()

        for i in range(len(self.__map)):
            for j in range(len(self.__map[i])):
                self.__map[i][j] = virtual[i][j]

        self.__lock.release()

    def get_map(self) -> typing.Tuple[typing.Tuple[Unit]]:
        """get_map returns the map of the grid as tuple."""
        self.__lock.acquire()

        grid = tuple(tuple(row) for row in self.__map)

        self.__lock.release()
        return grid


class TetrisVirtualGrid:
    """TetrisVirtualGrid allows the computation of the next state of the grid
    After the computations are done, virtual grid is solidified and will update the actual grid
    """

    def __init__(self, row: int, col: int, sync) -> None:
        self.__lock = threading.Lock()
        self.__sync = sync

        self.map: typing.List[typing.List[Unit]] = [
            [None for _ in range(col)] for _ in range(row)]

    def add_shape(self, shape: Shape):
        """Add a new shape to the grid.

        Args:
            shape (Shape): Shape object to be added to the grid.

        Raises:
            OccupiedPositionException: If the shape cannot be placed on the grid.
        """
        self.__lock.acquire()

        if not self.__is_shape_placeable(shape):
            self.__lock.release()
            raise OccupiedPositionException()

        self.__place_shape(shape)
        self.__solidify()

    def relocate_shape(self, shape: Shape, row: int, col: int):
        """Relocate a shape on the grid.

        Args:
            shape (Shape): Shape object to be relocated on the grid.
            row (int): Integer value to inc/dec from each unit's row value.
            col (int): Integer value to inc/dec from each unit's col value.

        Raises:
            OccupiedPositionException: If the shape cannot be placed on the grid.
        """
        self.__lock.acquire()

        self.__remove_shape(shape)

        if not self.__is_shape_placeable(shape, row, col):
            self.__place_shape(shape)
            self.__lock.release()
            raise OccupiedPositionException()

        self.__place_shape(shape, row, col)
        self.__solidify()

    def replace_shape(self, old: Shape, new: Shape):
        """Replace an old shape with a new shape.
        Removes the old shape from the grid and adds the new shape to the grid.
        If the new shape cannot be placed on the grid, the old shape is added back to the grid.

        Args:
            old (Shape): Shape object to be removed from the grid.
            new (Shape): Shape object to be added to the grid.

        Raises:
            OccupiedPositionException: If the new shape cannot be placed on the grid.
        """
        self.__lock.acquire()

        self.__remove_shape(old)

        if not self.__is_shape_placeable(new):
            self.__place_shape(old)
            self.__lock.release()
            raise OccupiedPositionException()

        self.__place_shape(new)
        self.__solidify()

    def __is_shape_placeable(self, shape: Shape, row=0, col=0) -> bool:
        """Check if a shape can be placed on the grid.

        Args:
            shape (Shape): Shape object to be checked.
            row (int, optional): Integer value to inc/dec from each unit's row value. Defaults to 0.
            col (int, optional): Integer value to inc/dec from each unit's col value. Defaults to 0.

        Returns:
            bool: Returns True if the shape can be placed on the grid, False otherwise.
        """
        for unit in shape.units:
            if unit.row+row >= len(self.map) or unit.col+col >= len(self.map[0]) or unit.row + row < 0 or unit.col + col < 0:
                return False
            if self.map[unit.row + row][unit.col + col] is not None:
                return False
        return True

    def __remove_shape(self, shape: Shape):
        """Remove a shape from the grid

        Args:
            shape (Shape): Shape object to be removed from the grid.
        """
        for unit in shape.units:
            self.map[unit.row][unit.col] = None

    def __place_shape(self, shape: Shape, row=0, col=0):
        """Place a shape on the grid and update the shape units
        with the increased/decreased row and col values.

        Args:
            shape (Shape): Shape object to be placed on the grid.
            row (int, optional): Integer value to inc/dec from each unit's row value. Defaults to 0.
            col (int, optional): Integer value to inc/dec from each unit's col value. Defaults to 0.
        """
        for unit in shape.units:
            self.map[unit.row + row][unit.col + col] = unit
            unit.row, unit.col = unit.row + row, unit.col + col

        # update start row and col otherwise rotate will be wrong
        shape.start_row += row
        shape.start_col += col

    def shift_down_rows(self, idx):
        while idx >= 1:
            copy_row = copy.copy(self.map[idx-1])
            self.map[idx] = copy_row
            idx -= 1

    def __solidify(self):
        """Solidify the current state of the virtual grid and release the lock"""
        self.__sync(self.map)
        self.__lock.release()
