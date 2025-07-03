import os
import helpers

def get_end_values(current_dir, current_image):
    # Edge case: If new_dir/IMG_0001.JPG does not exist but old_dir/IMG_9999.JPG does
    if not os.path.exists(current_dir):
        end_dir = helpers.directory_shift_down(current_dir)
        end_image = "IMG_9999.JPG"
        end_date = helpers.get_date_taken(f"{end_dir}/{end_image}")
    else:
        end_dir = current_dir
        end_image = helpers.image_shift_down(current_image)
        end_date = helpers.get_date_taken(f"{end_dir}/{end_image}")
    return end_dir, end_image, end_date
        

def transfer_photos(start_dir, start_image, external_hd_path):
    current_dir = start_dir
    current_image = start_image
    current_path = f"{current_dir}/{current_image}"

    while os.path.exists(current_path):
        current_date = helpers.get_date_taken(current_path)
        pretty_date = helpers.convert_to_month_year(current_date)

        hd_pretty_date_path = f"{external_hd_path}/{pretty_date}"
        if not os.path.exists(hd_pretty_date_path):
            os.makedirs(hd_pretty_date_path)

        # Move the photo to the external hard drive
        os.rename(current_path, f"{hd_pretty_date_path}/{current_image}")

        current_image = helpers.image_shift_up(current_image)
        if current_image == "Hit Photo Limit":
            current_image = "IMG_0001.JPG"
            current_dir = helpers.directory_shift_up(current_dir)
    
    return get_end_values(current_dir, current_image)