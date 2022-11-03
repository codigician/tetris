from src.shape import create_shape, rotate

import pytest


def test_I_shape():
    shape = create_shape("I", 0, 0)

    assert shape.units[0].row == 0
    assert shape.units[0].col == 0
    assert shape.units[1].row == 1
    assert shape.units[1].col == 0
    assert shape.units[2].row == 2
    assert shape.units[2].col == 0
    assert shape.units[3].row == 3
    assert shape.units[3].col == 0


def test_L_shape():
    shape = create_shape("L", 0, 0)

    assert shape.units[0].row == 0
    assert shape.units[0].col == 0
    assert shape.units[1].row == 1
    assert shape.units[1].col == 0
    assert shape.units[2].row == 2
    assert shape.units[2].col == 0
    assert shape.units[3].row == 2
    assert shape.units[3].col == 1


def test_Z_shape():
    shape = create_shape("Z", 0, 0)

    assert shape.units[0].row == 0
    assert shape.units[0].col == 0
    assert shape.units[1].row == 0
    assert shape.units[1].col == 1
    assert shape.units[2].row == 1
    assert shape.units[2].col == 1
    assert shape.units[3].row == 1
    assert shape.units[3].col == 2


def test_T_shape():
    shape = create_shape("T", 0, 0)

    assert shape.units[0].row == 0
    assert shape.units[0].col == 0
    assert shape.units[1].row == 0
    assert shape.units[1].col == 1
    assert shape.units[2].row == 0
    assert shape.units[2].col == 2
    assert shape.units[3].row == 1
    assert shape.units[3].col == 1


def test_square_shape():
    shape = create_shape("S", 0, 0)

    assert shape.units[0].row == 0
    assert shape.units[0].col == 0
    assert shape.units[1].row == 0
    assert shape.units[1].col == 1
    assert shape.units[2].row == 1
    assert shape.units[2].col == 0
    assert shape.units[3].row == 1
    assert shape.units[3].col == 1


def test_unknown_shape_raise_not_implemented_error():
    with pytest.raises(NotImplementedError):
        create_shape("X", 0, 0)


def test_rotate_I_shape():
    """
        8 - - -     8 8 8 8     - - - 8     - - - -    8 - - -
        8 - - -     - - - -     - - - 8     - - - -    8 - - -
        8 - - -     - - - -     - - - 8     - - - -    8 - - -
        8 - - -     - - - -     - - - 8     8 8 8 8    8 - - -
    """

    i = create_shape('I', 0, 0)

    i_90 = rotate(i)
    assert i_90.units[0].row == 0
    assert i_90.units[0].col == 0
    assert i_90.units[1].row == 0
    assert i_90.units[1].col == 1
    assert i_90.units[2].row == 0
    assert i_90.units[2].col == 2
    assert i_90.units[3].row == 0
    assert i_90.units[3].col == 3

    i_180 = rotate(i_90)
    assert i_180.units[0].row == 0
    assert i_180.units[0].col == 3
    assert i_180.units[1].row == 1
    assert i_180.units[1].col == 3
    assert i_180.units[2].row == 2
    assert i_180.units[2].col == 3
    assert i_180.units[3].row == 3
    assert i_180.units[3].col == 3

    i_270 = rotate(i_180)
    assert i_270.units[0].row == 3
    assert i_270.units[0].col == 0
    assert i_270.units[1].row == 3
    assert i_270.units[1].col == 1
    assert i_270.units[2].row == 3
    assert i_270.units[2].col == 2
    assert i_270.units[3].row == 3
    assert i_270.units[3].col == 3

    i_360 = rotate(i_270)
    assert i_360.units[0].row == 0
    assert i_360.units[0].col == 0
    assert i_360.units[1].row == 1
    assert i_360.units[1].col == 0
    assert i_360.units[2].row == 2
    assert i_360.units[2].col == 0
    assert i_360.units[3].row == 3
    assert i_360.units[3].col == 0


def test_rotate_L_shape():
    """
        8 - -      8 8 8      - 8 8     - - -    8 - -
        8 - -      8 - -      - - 8     - - 8    8 - -
        8 8 -      - - -      - - 8     8 8 8    8 8 -
    """

    l = create_shape('L', 5, 5)

    l_90 = rotate(l)
    assert l_90.units[0].row == 5
    assert l_90.units[0].col == 5
    assert l_90.units[1].row == 5
    assert l_90.units[1].col == 6
    assert l_90.units[2].row == 5
    assert l_90.units[2].col == 7
    assert l_90.units[3].row == 6
    assert l_90.units[3].col == 5

    l_180 = rotate(l_90)
    assert l_180.units[0].row == 5
    assert l_180.units[0].col == 6
    assert l_180.units[1].row == 5
    assert l_180.units[1].col == 7
    assert l_180.units[2].row == 6
    assert l_180.units[2].col == 7
    assert l_180.units[3].row == 7
    assert l_180.units[3].col == 7

    l_270 = rotate(l_180)
    assert l_270.units[0].row == 6
    assert l_270.units[0].col == 7
    assert l_270.units[1].row == 7
    assert l_270.units[1].col == 5
    assert l_270.units[2].row == 7
    assert l_270.units[2].col == 6
    assert l_270.units[3].row == 7
    assert l_270.units[3].col == 7

    l_360 = rotate(l_270)
    assert l_360.units[0].row == 5
    assert l_360.units[0].col == 5
    assert l_360.units[1].row == 6
    assert l_360.units[1].col == 5
    assert l_360.units[2].row == 7
    assert l_360.units[2].col == 5
    assert l_360.units[3].row == 7
    assert l_360.units[3].col == 6


def test_rotate_T_shape():
    """
        8 8 8    - - 8     - - -     8 - -    8 8 8
        - 8 -    - 8 8     - 8 -     8 8 -    - 8 -
        - - -    - - 8     8 8 8     8 - -    - - -
    """

    t = create_shape('T', 5, 5)

    t_90 = rotate(t)
    assert t_90.units[0].row == 5
    assert t_90.units[0].col == 7
    assert t_90.units[1].row == 6
    assert t_90.units[1].col == 6
    assert t_90.units[2].row == 6
    assert t_90.units[2].col == 7
    assert t_90.units[3].row == 7
    assert t_90.units[3].col == 7

    t_180 = rotate(t_90)
    assert t_180.units[0].row == 6
    assert t_180.units[0].col == 6
    assert t_180.units[1].row == 7
    assert t_180.units[1].col == 5
    assert t_180.units[2].row == 7
    assert t_180.units[2].col == 6
    assert t_180.units[3].row == 7
    assert t_180.units[3].col == 7

    t_270 = rotate(t_180)
    assert t_270.units[0].row == 5
    assert t_270.units[0].col == 5
    assert t_270.units[1].row == 6
    assert t_270.units[1].col == 5
    assert t_270.units[2].row == 6
    assert t_270.units[2].col == 6
    assert t_270.units[3].row == 7
    assert t_270.units[3].col == 5

    t_360 = rotate(t_270)
    assert t_360.units[0].row == 5
    assert t_360.units[0].col == 5
    assert t_360.units[1].row == 5
    assert t_360.units[1].col == 6
    assert t_360.units[2].row == 5
    assert t_360.units[2].col == 7
    assert t_360.units[3].row == 6
    assert t_360.units[3].col == 6

def test_rotate_Z_shape():
    """
        8 8 -   - - 8    - - -    - 8 -    8 8 -
        - 8 8   - 8 8    8 8 -    8 8 -    - 8 8
        - - -   - 8 -    - 8 8    8 - -    - - -
    """

    z = create_shape('Z', 2, 2)

    z_90 = rotate(z)
    assert z_90.units[0].row == 2
    assert z_90.units[0].col == 4
    assert z_90.units[1].row == 3
    assert z_90.units[1].col == 3
    assert z_90.units[2].row == 3
    assert z_90.units[2].col == 4
    assert z_90.units[3].row == 4
    assert z_90.units[3].col == 3

    z_180 = rotate(z_90)
    assert z_180.units[0].row == 3
    assert z_180.units[0].col == 2
    assert z_180.units[1].row == 3
    assert z_180.units[1].col == 3
    assert z_180.units[2].row == 4
    assert z_180.units[2].col == 3
    assert z_180.units[3].row == 4
    assert z_180.units[3].col == 4

    z_270 = rotate(z_180)
    assert z_270.units[0].row == 2
    assert z_270.units[0].col == 3
    assert z_270.units[1].row == 3
    assert z_270.units[1].col == 2
    assert z_270.units[2].row == 3
    assert z_270.units[2].col == 3
    assert z_270.units[3].row == 4
    assert z_270.units[3].col == 2

    z_360 = rotate(z_270)
    assert z_360.units[0].row == 2
    assert z_360.units[0].col == 2
    assert z_360.units[1].row == 2
    assert z_360.units[1].col == 3
    assert z_360.units[2].row == 3
    assert z_360.units[2].col == 3
    assert z_360.units[3].row == 3
    assert z_360.units[3].col == 4
