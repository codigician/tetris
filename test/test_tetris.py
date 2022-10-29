from tetris import Tetris
from tetris import RandomShapeGenerator


def test_generate_random_shape_is_exist():
    generator = RandomShapeGenerator(0, 4)
    shape = generator.generate_random_shape()

    assert shape is not None
    assert shape.units[0].row == 0
    assert shape.units[0].col == 4
    assert shape.color in generator.colors
