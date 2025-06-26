import pytest
from src.helpers import directory_shift_down

def test_shift_down():
    assert directory_shift_down("/Volumes/SD_CARD_1/DCIM/101CANON") == "/Volumes/SD_CARD_1/DCIM/100CANON"

def test_directory_limit():
    with pytest.raises(Exception):
        directory_shift_down("/Volumes/SD_CARD_1/DCIM/100CANON")

def test_invalid_directory():
    with pytest.raises(Exception):
        directory_shift_down("/Volumes/SD_CARD_1/DCIM/1a01CANON")