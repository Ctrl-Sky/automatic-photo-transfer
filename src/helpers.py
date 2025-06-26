import os
from datetime import datetime
from PIL import Image

def image_shift_up(image):
    # Expects filename of form IMG_####.JPG and increases #### by one
    try:
        number = int(image[4:8])
    except:
        raise Exception(f"{image}: Incorrect file name. Must match format IMG_####.JPG")

    number += 1

    # IMG_9999.JPG is the highest possible number for filename
    if number > 9999:
        return "Hit Photo Limit"

    string_number = str(number)
    missing_digits = 4 - len(string_number)
    
    for i in range(missing_digits, 0, -1):
        string_number = "0" + string_number

    return f"IMG_{string_number}.JPG"

def image_shift_down(image):
    # Expects filename of form IMG_####.JPG and increases #### by one
    try:
        number = int(image[4:8])
    except:
        raise Exception(f"{image}: Incorrect file name. Must match format IMG_####.JPG")

    number -= 1

    # IMG_0001.JPG is the lowest possible number for filename
    if number < 1:
        raise Exception("Image number can not be less than 1")

    string_number = str(number)
    missing_digits = 4 - len(string_number)
    
    for i in range(missing_digits, 0, -1):
        string_number = "0" + string_number

    return f"IMG_{string_number}.JPG"

def directory_shift_down(dir):
    # Expects directory in the form .../.../.../1[0-9][0-9]CANON
    try:
        dir_name = os.path.basename(os.path.normpath(dir))
        number = int(dir_name[:3])
    except:
        raise Exception(f"{dir}: Incorrect directory name. Must match format .../.../.../1[0-9][0-9]CANON")

    number -= 1

    # 100CANON is the lowest possible directory name
    if number < 100:
        raise Exception(f"{dir}: Directory number can not be 100")

    new_dir_name = f"{str(number)}CANON"
    parent_dir = os.path.dirname(os.path.normpath(dir))

    return f"{parent_dir}/{new_dir_name}"

def directory_shift_up(dir):
    # Expects directory in the form .../.../.../1[0-9][0-9]CANON
    try:
        dir_name = os.path.basename(os.path.normpath(dir))
        number = int(dir_name[:3])
    except:
        raise Exception(f"{dir}: Incorrect directory name. Must match format .../.../.../1[0-9][0-9]CANON")

    number += 1

    new_dir_name = f"{str(number)}CANON"
    parent_dir = os.path.dirname(os.path.normpath(dir))

    return f"{parent_dir}/{new_dir_name}"

def get_date_taken(image_path):
    exif = Image.open(image_path)._getexif()
    if not exif:
        return "Image does not have EXIF data"
    return exif[36867]

def convert_to_month_year(exif_date, include_date=False):
    # Expects exif_date to be in form of %Y:%m:%d %H:%M:%S
    date = exif_date.split(" ")[0]
    datetime_obj = datetime.strptime(date, "%Y:%m:%d")
    
    if include_date:
        return datetime_obj.strftime("%b-%d-%Y")
    else:
        return datetime_obj.strftime("%b-%Y")

print(convert_to_month_year(get_date_taken("tests/IMG_8423.JPG"), True))