import pytest
from src.helpers import image_shift_down

def test_single_digit():
    assert image_shift_down("IMG_0002.JPG") == "IMG_0001.JPG"

def test_double_digit():
    assert image_shift_down("IMG_0010.JPG") == "IMG_0009.JPG"

def test_triple_digit():
    assert image_shift_down("IMG_0100.JPG") == "IMG_0099.JPG"

def test_quadruple_digit():
    assert image_shift_down("IMG_1000.JPG") == "IMG_0999.JPG"

def test_image_is_zero():
    with pytest.raises(Exception):
        image_shift_down("IMG_0001.JPG")

def test_invalid_image():
    with pytest.raises(Exception):
        image_shift_down("IMG_IMG1000.JPG")

