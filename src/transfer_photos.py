import os
import helpers

def transfer_photos(start_dir, start_image, start_date, hard_drive):
    current_dir = start_dir
    current_image = start_image
    current_path = f"{start_dir}/{start_image}"

    while os.path.exists(current_path):
        current_date = helpers.get_date_taken(current_path)
        pretty_date = helpers.convert_to_month_year(current_date)

        os.makedirs()