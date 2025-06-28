import pytest
from helpers import image_shift_up, image_shift_down

def test_up_single_digit():
    assert image_shift_up("IMG_0001.JPG") == "IMG_0002.JPG"

def test_up_double_digit():
    assert image_shift_up("IMG_0010.JPG") == "IMG_0011.JPG"

def test_up_triple_digit():
    assert image_shift_up("IMG_0100.JPG") == "IMG_0101.JPG"

def test_up_quadruple_digit():
    assert image_shift_up("IMG_1000.JPG") == "IMG_1001.JPG"

def test_up_image_limit():
    assert image_shift_up("IMG_9999.JPG") == "Hit Photo Limit"

def test_up_invalid_image():
    with pytest.raises(Exception):
        image_shift_up("IMG_IMG1000.JPG")

def test_down_single_digit():
    assert image_shift_down("IMG_0002.JPG") == "IMG_0001.JPG"

def test_down_double_digit():
    assert image_shift_down("IMG_0010.JPG") == "IMG_0009.JPG"

def test_down_triple_digit():
    assert image_shift_down("IMG_0100.JPG") == "IMG_0099.JPG"

def test_down_quadruple_digit():
    assert image_shift_down("IMG_1000.JPG") == "IMG_0999.JPG"

def test_down_image_is_zero():
    with pytest.raises(Exception):
        image_shift_down("IMG_0001.JPG")

def test_down_invalid_image():
    with pytest.raises(Exception):
        image_shift_down("IMG_IMG1000.JPG")
