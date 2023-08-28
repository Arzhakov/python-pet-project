#!/usr/bin/python3

import os
import settings
import fetcher
import bsparser
import saver
import uuid

manager = settings.SettingsManager()

url = input("Input URL: ")

html_code = fetcher.fetch_html(url)

if html_code:
    select = manager.get_setting('select', default='#documents a.rel-link')
    href_values = bsparser.extract_href_values(html_code, select)
    
    if href_values:
        library = manager.get_setting('library', default='~/.ppp/library')
        new_folder_name = os.path.join(library, str(uuid.uuid4()))

        saver.save_all(href_values, new_folder_name)
    else:
        print("No href found")
else:
    print("Failed to get page html code")