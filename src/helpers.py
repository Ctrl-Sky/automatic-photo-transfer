def image_shift_up(image):
    # Expects filename of form IMG_####.JPG and increases #### by one
    try:
        number = int(image[4:8])
    except:
        raise Exception(f"{image}: Incorrect file name. Must match format IMG_####.JPG")

    number += 1

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

    if number < 1:
        raise Exception("Image number can not be less than 1")

    string_number = str(number)
    missing_digits = 4 - len(string_number)
    
    for i in range(missing_digits, 0, -1):
        string_number = "0" + string_number

    return f"IMG_{string_number}.JPG"