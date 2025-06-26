def image_shift_up(image):
    # Expects filename of form IMG_####.JPG and increases #### by one
    try:
        number = int(image[4:8])
    except:
        raise Exception(f"{image}: Incorrect file name. Must match format IMG_####.JPG")

    number += 1
    new_image_name = f"IMG_{str(number)}.JPG"
    return new_image_name



