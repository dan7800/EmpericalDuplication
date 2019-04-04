""" This file adds the top and bottom tags for the xml to be in a proper format. """

import re
import glob

PRE_FILE = """<?xml version="1.0" encoding="UTF-8"?>
<bugs>
"""
POST_FILE = '</bugs>'


def sanitize_file(file_name):
    already_sanitized = False

    with open(file_name, 'r') as orig_file:
        file_content = orig_file.read()
        if re.search(r'(?m)^<bugs>', file_content):
            already_sanitized = True

    if not already_sanitized:
        with open(file_name, 'w') as new_file:
            print('sanitizing file: ', file_name)
            new_file.write(PRE_FILE + file_content + POST_FILE)


def sanitize_xml_directory(dir_path):
    files = glob.glob(dir_path)
    for f_name in files:
        print('reading ', f_name)
        sanitize_file(f_name)

