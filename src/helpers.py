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

print(image_shift_up("IMG_9999.JPG"))
# Test invalid name: "IMG_IMG1000.JPG"
# Test name: "IMG_1000" assert IMG_1001
# IMG_0100 asser IMG_0101
# IMG_0010 assert IMG_0011.JGP
# IMG_0001 assert IMG_0002
# IMG_0009 assert IMG_0010
# IMG_9999 assert Hit Photo Limit