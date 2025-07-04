import os
from transfer_photos import get_end_values, transfer_photos

IMG_DATE="2024:07:02 10:19:42"
HD_PATH="tests/hard_drive"

def test_get_end_values_edge_case():
    assert get_end_values("tests/DCIM/102CANON", "IMG_0001.JPG", IMG_DATE) == ("tests/DCIM/101CANON", "IMG_9999.JPG", IMG_DATE)

def test_get_end_values():
    assert get_end_values("tests/DCIM/101CANON", "IMG_8424.JPG", IMG_DATE) == ("tests/DCIM/101CANON", "IMG_8423.JPG", IMG_DATE)

def test_transfer_photos_1_dir():
    assert transfer_photos("tests/DCIM/103CANON", "IMG_8423.JPG", HD_PATH) == ("tests/DCIM/103CANON", "IMG_8425.JPG", IMG_DATE)
    
    # Clean up environment
    os.rename("tests/hard_drive/Jul-2024/IMG_8423.JPG", "tests/DCIM/103CANON/IMG_8423.JPG")
    os.rename("tests/hard_drive/Jul-2024/IMG_8424.JPG", "tests/DCIM/103CANON/IMG_8424.JPG")
    os.rename("tests/hard_drive/Jul-2024/IMG_8425.JPG", "tests/DCIM/103CANON/IMG_8425.JPG")
    os.rmdir("tests/hard_drive/Jul-2024")

def test_transfer_photos_2_dir():
    assert transfer_photos("tests/DCIM/103CANON", "IMG_9998.JPG", HD_PATH) == ("tests/DCIM/104CANON", "IMG_0002.JPG", IMG_DATE)
    
    # Clean up environment
    os.rename("tests/hard_drive/Jul-2024/IMG_9998.JPG", "tests/DCIM/103CANON/IMG_9998.JPG")
    os.rename("tests/hard_drive/Jul-2024/IMG_9999.JPG", "tests/DCIM/103CANON/IMG_9999.JPG")
    os.rename("tests/hard_drive/Jul-2024/IMG_0001.JPG", "tests/DCIM/104CANON/IMG_0001.JPG")
    os.rename("tests/hard_drive/Jul-2024/IMG_0002.JPG", "tests/DCIM/104CANON/IMG_0002.JPG")
    os.rmdir("tests/hard_drive/Jul-2024")

def test_transfer_photos_diff_dates():
    assert transfer_photos("tests/DCIM/104CANON", "IMG_1000.JPG", HD_PATH) == ("tests/DCIM/104CANON", "IMG_1001.JPG", IMG_DATE)

    # Clean up environment
    os.rename("tests/hard_drive/Jan-2023/IMG_1000.JPG", "tests/DCIM/104CANON/IMG_1000.JPG")
    os.rename("tests/hard_drive/Jul-2024/IMG_1001.JPG", "tests/DCIM/104CANON/IMG_1001.JPG")
    os.rmdir("tests/hard_drive/Jul-2024")
    os.rmdir("tests/hard_drive/Jan-2023")

def test_transfer_photos_include_day():
    assert transfer_photos("tests/DCIM/104CANON", "IMG_1000.JPG", HD_PATH, include_day=True) == ("tests/DCIM/104CANON", "IMG_1001.JPG", IMG_DATE)

    # Clean up environment
    os.rename("tests/hard_drive/Jan-29-2023/IMG_1000.JPG", "tests/DCIM/104CANON/IMG_1000.JPG")
    os.rename("tests/hard_drive/Jul-02-2024/IMG_1001.JPG", "tests/DCIM/104CANON/IMG_1001.JPG")
    os.rmdir("tests/hard_drive/Jul-02-2024")
    os.rmdir("tests/hard_drive/Jan-29-2023")