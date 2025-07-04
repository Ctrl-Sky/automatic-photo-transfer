# automatic-photo-transfer

uses python3.12.8

Setup
python3.12 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pytest (from root)
python src/main.py

This is specifically designed for Canon cameras and the SD cards they format. 
For these SD cards, they always come in the format:
<SD_CARD_NAME>
    -> DCIM
        -> 100CANON
            -> This folder will contains IMG_<0001 - 9999>.JPG, once it hits 9999 it will start again in a new folder
        -> 101CANON
            -> This folder will start again at IMG_<0001 - 9999>.JPG

So this automation script is based on the fact that every image follows the name IMG_####.JPG, every image is in some directory /Volumes/<SD_CARD_NAME>/DCIM/###CANON/, and, when the images hit 9999, it will overflow into a new directory. 

In case anthor SD card from another brand is used, here are the functions that have the value hard coded and will need to be changed:
helpers.py
    directory shift up and down
    image shift up and down
initialize.py
    initialize_table
    get_start_values
    edge_case_9999
    initialize_repo
Each of these will usually just contain one line hard coded in