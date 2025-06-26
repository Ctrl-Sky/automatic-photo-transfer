import pytest
from src.helpers import directory_shift_up

def test_shift_down():
    assert directory_shift_up("/Volumes/SD_CARD_1/DCIM/100CANON") == "/Volumes/SD_CARD_1/DCIM/101CANON"

def test_invalid_directory():
    with pytest.raises(Exception):
        directory_shift_up("/Volumes/SD_CARD_1/DCIM/1a01CANON")