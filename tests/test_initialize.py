import pytest
import os
import csv
from initialize import initialize_table, get_end_values_from_table, edge_case_9999, initialize_repo, convert_end_to_start_values

CSV_PATH = "test/test.csv"
SD_CARD_1 = "SD_CARD_1"
SD_CARD_2 = "SD_CARD_2"
HARD_DRIVE = "HARD_DRIVE"

def remove_csv_path(path):
    os.remove(path)
    if os.path.dirname(path) != "":
        os.rmdir(os.path.dirname(path))

def test_initialize_table():
    initialize_table(CSV_PATH)
    assert os.path.exists(CSV_PATH) == True
    with open(CSV_PATH, 'r') as file:
        read = csv.reader(file)
        for row in read:
            assert row == ['migration_name', 'sd_card_name', 'start_dir', 'start_image', 'start_date', 'end_dir', 'end_image', 'end_date']
            break
    # Clean up test environment
    remove_csv_path(CSV_PATH)

def test_get_end_value_exist():
    # Initialize environment for testing get_end_values_from_table()
    initialize_table(CSV_PATH)
    with open(CSV_PATH, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(["vacation_2024",SD_CARD_1,"/DCIM/100CANON","IMG_0001.JPG","2024-07-01 09:00:00","/DCIM/101CANON","IMG_0150.JPG","2024-07-01 18:30:00"])

    # Test SD_CARD_NAME does exist in csv file
    assert get_end_values_from_table(CSV_PATH, SD_CARD_1) == ("/DCIM/101CANON","IMG_0150.JPG")

    # Clean up test environment
    remove_csv_path(CSV_PATH)

def test_get_eng_value_not_exist():
    # Initialize environment for testing get_end_values_from_table()
    initialize_table(CSV_PATH)
    with open(CSV_PATH, 'a') as file:
        writer = csv.writer(file)
        writer.writerow(["vacation_2024",SD_CARD_1,"/DCIM/100CANON","IMG_0001.JPG","2024-07-01 09:00:00","/DCIM/101CANON","IMG_0150.JPG","2024-07-01 18:30:00"])

    # Test SD_CARD_NAME does NOT exist in csv file
    assert get_end_values_from_table(CSV_PATH, SD_CARD_2) == ("NOT", "FOUND")

    # Clean up test environment
    remove_csv_path(CSV_PATH)

def test_convert_end_to_start_exist():
    assert convert_end_to_start_values("tests/DCIM/101CANON", "IMG_8422.JPG", "SD_CARD_1") == ("tests/DCIM/101CANON", "IMG_8423.JPG", "2024:07:02 10:19:42")

def test_convert_end_to_start_9999():
    assert convert_end_to_start_values("tests/DCIM/100CANON", "IMG_9999.JPG", "SD_CARD_1") == ("tests/DCIM/101CANON", "IMG_0001.JPG", "2024:07:02 10:19:42")

def test_convert_end_to_start_not_exist():
    assert convert_end_to_start_values("NOT", "FOUND", "tests") == ("tests/DCIM/100CANON", "IMG_0001.JPG", "2024:07:02 10:19:42")

def test_edge_case_9999():
    assert edge_case_9999(f"{SD_CARD_1}/DCIM/101CANON") == (f"{SD_CARD_1}/DCIM/102CANON", "IMG_0001.JPG")

# def test_initialize_repo_table_exist():
#     '''
#         Test when table already exist and sd card name exist in table
#     '''
#     # Initialize Environment for testing initialize_repo()
#     os.makedirs(SD_CARD_1)
#     os.makedirs(HARD_DRIVE)
#     initialize_table(CSV_PATH)
#     with open(CSV_PATH, 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow(["vacation_2024",SD_CARD_1,"/DCIM/100CANON","IMG_0001.JPG","2024-07-01 09:00:00","/DCIM/101CANON","IMG_0150.JPG","2024-07-01 18:30:00"])


#     assert initialize_repo(SD_CARD_1, HARD_DRIVE, CSV_PATH) == ("/DCIM/101CANON","IMG_0151.JPG")

#     # Clean up test environment
#     os.rmdir(SD_CARD_1)
#     os.rmdir(HARD_DRIVE)
#     remove_csv_path(CSV_PATH)

# def test_initialize_repo_table_not_exist():
#     '''
#         Test when table does not exist and sd card name does not exist within table
#     '''
#     # Initialize Environment for testing initialize_repo()
#     os.makedirs(SD_CARD_1)
#     os.makedirs(HARD_DRIVE)

#     assert initialize_repo(SD_CARD_1, HARD_DRIVE, CSV_PATH) == (f"{SD_CARD_1}/DCIM/100CANON", "IMG_0001.JPG")

#     # Clean up environment
#     os.rmdir(SD_CARD_1)
#     os.rmdir(HARD_DRIVE)
#     remove_csv_path(CSV_PATH)


# def test_initialize_repo_img_9999():
#     '''
#         Test when table already exist and most recent image is IMG_9999.JPG
#     '''
#     # Initialize Environment for testing initialize_repo()
#     os.makedirs(SD_CARD_1)
#     os.makedirs(HARD_DRIVE)
#     initialize_table(CSV_PATH)
#     with open(CSV_PATH, 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow(["vacation_2024",SD_CARD_1,"/DCIM/100CANON","IMG_0001.JPG","2024-07-01 09:00:00","/DCIM/101CANON","IMG_9999.JPG","2024-07-01 18:30:00"])

#     assert initialize_repo(SD_CARD_1, HARD_DRIVE, CSV_PATH) == ("/DCIM/102CANON","IMG_0001.JPG")

#     # Clean up test environment
#     os.rmdir(SD_CARD_1)
#     os.rmdir(HARD_DRIVE)
#     remove_csv_path(CSV_PATH)