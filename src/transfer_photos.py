import os
import helpers

def get_end_values(current_dir, current_image, current_date):
    """
        To be used after the while loop. Due to the logic of the while loop, the current_image is shifted up until it doesn't exist
        anymore. Since the end values of the table must include the value of the last photo uploaded, the photo is shifted down so
        it represents the last photo uploaded.
    
        :param current_dir: The full path of the directory the current image is located in
        :type current_dir: string
        :param current_image: The file name of the current image
        :type current_image: string
        :return: three values, the end directory, image, and date of the final photo uploaded
        :rtype: string, string, string
    """
    # Edge case: If new_dir/IMG_0001.JPG does not exist but old_dir/IMG_9999.JPG does
    if not os.path.exists(current_dir):
        end_dir = helpers.directory_shift_down(current_dir)
        end_image = "IMG_9999.JPG"
    else:
        end_dir = current_dir
        end_image = helpers.image_shift_down(current_image)
    return end_dir, end_image, current_date
        

def transfer_photos(start_dir, start_image, external_hd_path, include_day=False):
    """
        Transfers photos from an SD card directory to an external hard drive, organizing them by the month and year the photo was taken.

        The function starts at the specified directory and image, and continues transferring sequential images until it reaches a file that does not exist.
        Each photo is moved into a subdirectory on the external hard drive named after the month and year the photo was taken (e.g., "Jul-2025").
        If the end of a directory or image sequence is reached, it automatically shifts to the next directory or wraps around as needed.

        :param start_dir: The full path of the directory the start image is located in
        :type start_dir: string
        :param start_image: The file name of the start image
        :type start_image: string
        :param external_hd_path: The full path to the external hard drive the photos will be moved to
        :type external_hd_path: string
        :return: two values, the start directory and image for the next migration
        :rtype: string, string
    """
    current_dir = start_dir
    current_image = start_image
    current_path = f"{current_dir}/{current_image}"

    while os.path.exists(current_path):
        current_date = helpers.get_date_taken(current_path)
        pretty_date = helpers.convert_to_month_year(current_date, include_day)

        hd_pretty_date_path = f"{external_hd_path}/{pretty_date}"
        if not os.path.exists(hd_pretty_date_path):
            os.makedirs(hd_pretty_date_path)

        # Move the photo to the external hard drive
        os.rename(current_path, f"{hd_pretty_date_path}/{current_image}")

        current_image = helpers.image_shift_up(current_image)
        if current_image == "Hit Photo Limit":
            current_image = "IMG_0001.JPG"
            current_dir = helpers.directory_shift_up(current_dir)
        current_path = f"{current_dir}/{current_image}"

    return get_end_values(current_dir, current_image, current_date)