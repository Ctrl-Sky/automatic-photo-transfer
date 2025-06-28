import csv
import os
from src.helpers import directory_shift_up

def does_path_exist(path):
    if not os.path.exists(path):
        raise Exception(f"{path} does not exist")

def initialize_table(table_path):
    '''
        Takes a path to a csv file
        Creates the parent directories if they exist
        Create the csv file and write the headers into it
    '''
    # Create Parent Directories
    if os.path.dirname(table_path) != "":
        os.makedirs(os.path.dirname(table_path))

    # Create csv file
    with open(table_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["migration_name", "sd_card_name", "start_dir", "start_image", "start_date", "end_dir", "end_image", "end_date"])

def get_start_values(table_path, sd_card_name):
    '''
        Starting from the bottom in the migration table, look for the most recent migration with the given SD card name
        If found, set the start values for this migration as the end values of the last migration
        If not found, set as default "start" migration values
    '''
    with open(table_path, 'r') as file:
        reversed_reader = reversed(list(csv.reader(file)))
        for row in reversed_reader:
            if row[1] == sd_card_name:
                # Return the end_dir, end_image, end_date
                return row[5], row[6], row[7]
        return f"/Volumes/{sd_card_name}/DCIM/100CANON", "IMG_0001.JPG", "N/A"
    
def edge_case_9999(start_dir):
    # For when image is at final name of IMG_9999.JPG, no more space so must shift to new directory
    new_dir = directory_shift_up(start_dir)
    new_image = "IMG_0001.JPG"
    return new_dir, new_image

def initialize_repo(sd_card_name, external_hd_name, table_path):
    '''
        Initialized the repository by:
        - Ensuring sd card and hard drive exist
        - Creating table and header if it does not exist
        - If it exist, get the most recent upload for the sd card in the csv file, then setting the new start values as the end values
        - If not exist, set default values for the start values
        - Shift start directory if start image is at IMG_9999
        - Return the start values
    '''
    does_path_exist(sd_card_name)
    does_path_exist(external_hd_name)

    # If table does not exist, create it and add headers
    if not os.path.exists(table_path):
        initialize_table(table_path)

    start_dir, start_image, start_date = get_start_values(table_path, sd_card_name)

    # If image at edge case
    if start_image == "IMG_9999.JPG":
        start_dir, start_image = edge_case_9999(start_dir)

    return start_dir, start_image, start_date