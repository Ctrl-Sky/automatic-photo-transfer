from helpers import convert_to_month_year, get_date_taken

def test_get_date():
    assert get_date_taken("tests/DCIM/101CANON/IMG_8423.JPG") == "2024:07:02 10:19:42"

def test_date_convert():
    assert convert_to_month_year(get_date_taken("tests/DCIM/101CANON/IMG_8423.JPG")) == "Jul-2024"

def test_date_convert_with_day():
    assert convert_to_month_year(get_date_taken("tests/DCIM/101CANON/IMG_8423.JPG"), include_day=True) == "Jul-02-2024"