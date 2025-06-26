def image_shift_up(image):
    # Expects filename of form IMG_####.JPG and increases #### by one
    try:
        number = int(string_number)
    except:
        raise Exception(f"{image}: Incorrect file name. Must match format IMG_####.JPG")

    number += 1
    string_number = str(number)
    missing_digits = 4 - len(string_number)
    for i in range(missing_digits, -1, -1):
        string_number = "0" + string_number

    return f"IMG_{string_number}.JPG"

print(image_shift_up("IMG_0100.JPG"))