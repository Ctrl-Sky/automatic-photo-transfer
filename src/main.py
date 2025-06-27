import argparse
import os
from helpers import get_date_taken

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sd_card_name", default="SD_CARD_1")
    parser.add_argument("--external_hd_name", default="kl")
    args = parser.parse_args()

    if not os.path.exists(f"/Volumes/{args.sd_card_name}"):
        raise Exception(f"/Volumes/{args.sd_card_name} does not exist. Ensure SD card is correctly connected")
    
    if not os.path.exists(f"/Volumes/{args.external_hd_name}"):
        raise Exception(f"/Volumes/{args.external_hd_name} does not exist. Ensure HD is correctly connected")
    
    if not os.path.exists("tables/sd_migration_table.csv"):
        os.makedirs("tables")
        open('tables/sd_migration_table.csv', 'w').close()
        start_dir = f"/Volumes/{args.sd_card_name}/DCIM/100CANON"
        start_image = "IMG_0001.JPG"
        start_time = get_date_taken(f"{start_dir}/{start_image}")