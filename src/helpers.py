import os
from datetime import datetime
from PIL import Image

def image_shift_up(image):
    """
        Takes an image of form IMG_####.JPG and increases the value by one. 
        For example, given IMG_0001.JPG, it will return IMG_0002.JPG

        :param image: the file name of the image
        :type image: string
        :return: the new file name shifted up by one
        :rtype: string
    """
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
    """
        Takes an image of form IMG_####.JPG and decreases the value by one. 
        For example, given IMG_0002.JPG, it will return IMG_0001.JPG
        
        :param image: the file name of the image
        :type image: string
        :return: the new file name shifted down by one
        :rtype: string
    """
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
    """
        Takes a directory of form path/to/image/###CANON and decreases the value by one. 
        For example, given /Volumes/SD_CARD_1/DCIM/101CANON, it will return /Volumes/SD_CARD_1/DCIM/100CANON
        
        :param dir: the directory containing the images
        :type dir: string
        :return: the new directory shifted down by one
        :rtype: string
    """
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
    """
        Takes a directory of form path/to/image/###CANON and increases the value by one. 
        For example, given /Volumes/SD_CARD_1/DCIM/100CANON, it will return /Volumes/SD_CARD_1/DCIM/101CANON
        
        :param dir: the directory containing the images
        :type dir: string
        :return: the new directory shifted up by one
        :rtype: string
    """
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
    """
        Takes a path to an image, reads the EXIF and returns the date the photo was taken
        
        :param image_path: The full path including file name of the image
        :type image_path: string
        :return: the date the photo was taken
        :rtype: string
    """
    exif = Image.open(image_path)._getexif()
    if not exif:
        return "Image does not have EXIF data"
    return exif[36867]

def convert_to_month_year(exif_date, include_date=False):
    """
        Convert an exif date in the form YYYY:MM:DD HH:MM:SS into a pretty print of just month-year or month-date-year
        
        :param exif_date: A date in pulled from the EXIF
        :type exif_date: string
        :param include_date: Whether or not to return the date, default to False
        :type include_date: bool, optional
        :return: An easier to read string of the date
        :rtype: string
    """
    date = exif_date.split(" ")[0]
    datetime_obj = datetime.strptime(date, "%Y:%m:%d")
    
    if include_date:
        return datetime_obj.strftime("%b-%d-%Y")
    else:
        return datetime_obj.strftime("%b-%Y")