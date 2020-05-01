from unittest.mock import patch

import pytest

import color


@pytest.fixture(scope="module")
def gen():
    return color.gen_hex_color()


@patch.object(
    color, "sample", return_value=[0, 0, 0]
)  # return_value returns one value
def test_gen_hex_color(patch_sample, gen):
    assert next(gen) == "#000000"


@patch.object(
    color, "sample", side_effect=[[0, 255, 0], [255, 255, 255]]
)  # side_effect returns n values
def test_gen_hex_colors(patch_sample, gen):
    assert next(gen) == "#00FF00"
    assert next(gen) == "#FFFFFF"


@patch("color.sample", return_value=[0, 0, 0])
def test_gen_hex_color_patch(patch_sample, gen):
    assert next(gen) == "#000000"
    patch_sample.assert_called_with(range(0, 256), 3)
