from src.shape import create_shape


def test_I_shape():
    shape = create_shape("I", 0, 0)

    assert shape.units[0].row == 0
    assert shape.units[0].col == 0
    assert shape.units[1].row == 0
    assert shape.units[1].col == 1
    assert shape.units[2].row == 0
    assert shape.units[2].col == 2
    assert shape.units[3].row == 0
    assert shape.units[3].col == 3


def test_L_shape():
    shape = create_shape("L", 0, 0)

    assert shape.units[0].row == 0
    assert shape.units[0].col == 0
    assert shape.units[1].row == 0
    assert shape.units[1].col == 1
    assert shape.units[2].row == 0
    assert shape.units[2].col == 2
    assert shape.units[3].row == 1
    assert shape.units[3].col == 2

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