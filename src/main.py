import argparse
import csv
from .initialize import initialize_repo

# TABLE_PATH = "tables/sd_migration_table.csv"
TABLE_PATH = "tables/test.csv"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sd_card_name", default="SD_CARD_1")
    parser.add_argument("--external_hd_name", default="kl")
    parser.add_argument("--migration_name", required=False)
    args = parser.parse_args()

    start_dir, start_image, start_date = initialize_repo(args.sd_card_name, args.external_hd_name, TABLE_PATH)