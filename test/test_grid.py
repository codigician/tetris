from grid import OccupiedPositionException, TetrisVirtualGrid
from shape import Unit, create_shape
import pytest


def mock_sync(*args):
    pass


def test_add_shape_given_valid_shape_expect_shape_in_grid():
    grid = TetrisVirtualGrid(5, 5, mock_sync)
    shape_t = create_shape('T', 0, 2)

    grid.add_shape(shape_t)

    assert_map_with_shapes_only(grid.map, shape_t)


def test_add_shape_given_two_collided_shape_expect_occupied_position():
    grid = TetrisVirtualGrid(5, 5, mock_sync)
    shape_t = create_shape('T', 0, 1)
    shape_l = create_shape('L', 0, 1)

    grid.add_shape(shape_t)

    with pytest.raises(OccupiedPositionException):
        grid.add_shape(shape_l)


def test_add_shape_outbounds_of_grid():
    grid = TetrisVirtualGrid(5, 5, mock_sync)
    shape_t = create_shape('T', -1, 1)

    with pytest.raises(OccupiedPositionException):
        grid.add_shape(shape_t)


def test_relocate_shape_given_valid_shape_move_to_empty_unit():
    grid = TetrisVirtualGrid(5, 5, mock_sync)
    shape_t = create_shape('T', 0, 1)

    shape_positions = {
        (unit.row, unit.col): True
        for unit in shape_t.units
    }

    grid.add_shape(shape_t)

    grid.relocate_shape(shape_t, 1, 1)

    # check if unit row/col values updated by relocation values
    for unit in shape_t.units:
        assert (unit.row - 1, unit.col - 1) in shape_positions

    assert_map_with_shapes_only(grid.map, shape_t)


def test_relocate_shape_to_outbounds_of_grid():
    grid = TetrisVirtualGrid(5, 5, mock_sync)
    shape_t = create_shape('T', 0, 1)

    grid.add_shape(shape_t)

    shape_positions = {
        (unit.row, unit.col): True
        for unit in shape_t.units
    }

    with pytest.raises(OccupiedPositionException):
        grid.relocate_shape(shape_t, 0, 3)

    # check if units positions remain same
    for unit in shape_t.units:
        assert (unit.row, unit.col) in shape_positions

    assert_map_with_shapes_only(grid.map, shape_t)


def test_relocate_shape_given_valid_shape_move_to_occupied_position():
    grid = TetrisVirtualGrid(10, 10, mock_sync)
    shape_t = create_shape('T', 0, 1)
    shape_l = create_shape('L', 0, 4)

    grid.add_shape(shape_t)
    grid.add_shape(shape_l)

    with pytest.raises(OccupiedPositionException):
        grid.relocate_shape(shape_t, 0, 1)


def test_replace_shape_given_l_t_shape_replace_l_with_t():
    grid = TetrisVirtualGrid(5, 5, mock_sync)
    shape_l = create_shape('L', 0, 1)
    shape_t = create_shape('T', 2, 2)

    grid.add_shape(shape_l)

    grid.replace_shape(shape_l, shape_t)

    assert_map_with_shapes_only(grid.map, shape_t)


def test_replace_shape_given_new_shape_outbounds_of_grid():
    grid = TetrisVirtualGrid(5, 5, mock_sync)
    shape_l = create_shape('L', 0, 1)
    shape_t = create_shape('T', 2, 5)

    with pytest.raises(OccupiedPositionException):
        grid.replace_shape(shape_l, shape_t)

    assert_map_with_shapes_only(grid.map, shape_l)


def test_replace_shape_given_shape_collides_with_another_shape():
    grid = TetrisVirtualGrid(5, 5, mock_sync)
    shape_l = create_shape('L', 0, 1)
    shape_z = create_shape('Z', 2, 0)
    shape_t = create_shape('T', 0, 1)

    grid.add_shape(shape_l)
    grid.add_shape(shape_z)

    with pytest.raises(OccupiedPositionException):
        grid.replace_shape(shape_z, shape_t)


def assert_map_with_shapes_only(map, shape):
    """Checks if the shape is in map assert if not
    checks if other elements are None

    Args:
        map: 2D matrix
        shape: Shape object to check
    """
    for unit in shape.units:
        assert map[unit.row][unit.col] == unit

    occupied_positions = {
        (unit.row, unit.col): True
        for unit in shape.units
    }

    for i in range(len(map)):
        for j in range(len(map[i])):
            if (i, j) in occupied_positions:
                continue

            assert map[i][j] is None
