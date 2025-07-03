import csv
import os
from helpers import directory_shift_up, image_shift_up

def does_path_exist(path):
    if not os.path.exists(path):
        raise Exception(f"{path} does not exist")

def initialize_table(table_path):
    """
        Takes a path to a csv file and if it doesn't exist, creates the file and adds the header

        :param table_path: The full path including the file name to a csv table
        :type table_path: string
    """
    # Create Parent Directories
    if os.path.dirname(table_path) != "":
        os.makedirs(os.path.dirname(table_path))

    # Create csv file
    with open(table_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["migration_name", "sd_card_name", "start_dir", "start_image", "start_date", "end_dir", "end_image", "end_date"])

def get_start_values(table_path, sd_card_path):
    """
        If the sd card is referenced within the table, get  the most recent photos that were uploaded from that sd card, increment by one set as the the new start point
        If the sd card is not referenced, return the default start values for the new start point

        :param table_path: The full path to a csv table
        :type table_path: string
        :param sd_card_path: The full path to a sd card
        :type sd_card_path: string
        :return: the new file name shifted up by one
        :rtype: string
    """
    sd_card_name = os.path.basename(sd_card_path)
    with open(table_path, 'r') as file:
        reversed_reader = reversed(list(csv.reader(file)))
        for row in reversed_reader:
            if row[1] == sd_card_name:
                # Return the end_dir, end_image
                start_dir, start_image =  row[5], row[6]

                # Shift image up to new values that need to be uploaded
                start_image = image_shift_up(start_image)
                if start_image == "Hit Photo Limit":
                    start_dir, start_image = edge_case_9999(start_dir)
                return start_dir, start_image

        return f"{sd_card_path}/DCIM/100CANON", "IMG_0001.JPG"
    
def edge_case_9999(start_dir):
    # For when image is at final name of IMG_9999.JPG, no more space so must shift to new directory
    new_dir = directory_shift_up(start_dir)
    new_image = "IMG_0001.JPG"
    return new_dir, new_image

def initialize_repo(sd_card_path, external_hd_path, table_path):
    """
        Within the table path, if the SD card had a recorded migration, pulls the most recent photo that was migrated from the SD 
        card and uses that as references for the next starting point for the next migration.
        If the SD card has never had a recorded migration, use the defual values as the starting point

        :param sd_card_path: The full path to a sd card
        :type sd_card_path: string
        :param external_hd_path: The full path to a external hd
        :type external_hd_path: string
        :param table_path: The full path to a csv table
        :type table_path: string
        :return: two values, the start directory and image for the next migration
        :rtype: string, string
    """
    does_path_exist(sd_card_path)
    does_path_exist(external_hd_path)

    # If table does not exist, create it and add headers
    if not os.path.exists(table_path):
        initialize_table(table_path)

    return get_start_values(table_path, sd_card_path)
