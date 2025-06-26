import pytest
from src.helpers import image_shift_up

def test_single_digit():
    assert image_shift_up("IMG_0001.JPG") == "IMG_0002.JPG"

def test_double_digit():
    assert image_shift_up("IMG_0010.JPG") == "IMG_0011.JPG"

def test_triple_digit():
    assert image_shift_up("IMG_0100.JPG") == "IMG_0101.JPG"

def test_quadruple_digit():
    assert image_shift_up("IMG_1000.JPG") == "IMG_1001.JPG"

def test_image_limit():
    assert image_shift_up("IMG_9999.JPG") == "Hit Photo Limit"

def test_invalid_image():
    with pytest.raises(Exception):
        image_shift_up("IMG_IMG1000.JPG")

