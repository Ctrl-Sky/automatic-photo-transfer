import argparse
import os
from initialize import initialize_repo
from transfer_photos import transfer_photos
from write_to_excel import write_to_migration_table

TABLE_PATH = "tables/sd_migration_table.csv"
# TABLE_PATH = "tables/test.csv"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sd_card_path", default="/Volumes/SD_CARD_1")
    parser.add_argument("--external_hd_path", default="/Volumes/kl")
    parser.add_argument("--migration_name", required=False, default="")
    parser.add_argument("--end_on", required=False, default="")
    parser.add_argument("--include_day", required=False, default=True)
    args = parser.parse_args()

    sd_card_path = args.sd_card_path
    external_hd_path = args.external_hd_path
    migration_name = args.migration_name
    end_on = args.end_on
    include_day = args.include_day

    start_dir, start_image, start_date = initialize_repo(sd_card_path, external_hd_path, TABLE_PATH)
    end_dir, end_image, end_date = transfer_photos(start_dir, start_image, external_hd_path, include_day=include_day, end_on=end_on)

    sd_card_name = os.path.basename(sd_card_path)
    write_to_migration_table(sd_card_name, start_dir, start_image, start_date, end_dir, end_image, end_date, TABLE_PATH, migration_name=migration_name)