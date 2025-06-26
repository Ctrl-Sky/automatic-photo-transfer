import pytest
from src.helpers import directory_shift_up, directory_shift_down

def test_shift_up():
    assert directory_shift_up("/Volumes/SD_CARD_1/DCIM/100CANON") == "/Volumes/SD_CARD_1/DCIM/101CANON"

def test_up_invalid_directory():
    with pytest.raises(Exception):
        directory_shift_up("/Volumes/SD_CARD_1/DCIM/1a01CANON")

def test_shift_down():
    assert directory_shift_down("/Volumes/SD_CARD_1/DCIM/101CANON") == "/Volumes/SD_CARD_1/DCIM/100CANON"

def test_down_directory_limit():
    with pytest.raises(Exception):
        directory_shift_down("/Volumes/SD_CARD_1/DCIM/100CANON")

def test_down_invalid_directory():
    with pytest.raises(Exception):
        directory_shift_down("/Volumes/SD_CARD_1/DCIM/1a01CANON")