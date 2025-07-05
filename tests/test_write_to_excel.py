import csv
import os
from src.write_to_excel import write_to_migration_table
from src.initialize import initialize_table

TEST_PATH = "tables/test1.csv"
SD_CARD = "SD_CARD_1"

def test_write_to_excel_no_name():
    initialize_table(TEST_PATH)
    write_to_migration_table(SD_CARD,"/DCIM/100CANON","IMG_0001.JPG","2024:07:01 09:00:00","/DCIM/101CANON","IMG_0150.JPG","2024:07:04 18:30:00", TEST_PATH)

    with open(TEST_PATH, 'r') as file:
        read = csv.reader(file)
        rows = list(read)
        assert rows[1] == ["Jul-01-2024_Jul-04-2024", "SD_CARD_1","/DCIM/100CANON","IMG_0001.JPG","2024:07:01 09:00:00","/DCIM/101CANON","IMG_0150.JPG","2024:07:04 18:30:00"]

    # Clean up
    os.remove(TEST_PATH)

def test_write_to_excel_with_name():
    initialize_table(TEST_PATH)
    write_to_migration_table(SD_CARD,"/DCIM/100CANON","IMG_0001.JPG","2024:07:01 09:00:00","/DCIM/101CANON","IMG_0150.JPG","2024:07:04 18:30:00", TEST_PATH, migration_name="Vacation_time")

    with open(TEST_PATH, 'r') as file:
        read = csv.reader(file)
        rows = list(read)
        assert rows[1] == ["Vacation_time", "SD_CARD_1","/DCIM/100CANON","IMG_0001.JPG","2024:07:01 09:00:00","/DCIM/101CANON","IMG_0150.JPG","2024:07:04 18:30:00"]

    # Clean up
    os.remove(TEST_PATH)