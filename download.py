#!/usr/bin/python3

import os
import settings
import fetcher
import bsparser
import saver
import uuid
from db import create_book, find_book_by_url

manager = settings.SettingsManager()

url = input("Input URL: ")

book = find_book_by_url(url)
if book:
    print(f"Document found: ID={book.id}, Author={book.author}, Title={book.title}, Folder={book.folder}")
    print("Skip.")
else:
    print("Let's create new book!")

    html_code = fetcher.fetch_html(url)

    if html_code:
        select1 = manager.get_setting('select1', default='#documents a.rel-link')
        #select2 = manager.get_setting('select2', default='#documents a.rel-link')
        authors_class1 = manager.get_setting('authors_class1', default='__title')
        authors_text = manager.get_setting('authors_text', default='Tags List:')
        authors_class2 = manager.get_setting('authors_class2', default='_content')
        href_values = bsparser.extract_href_values(html_code, select1)
        author = bsparser.extract_authors(html_code, authors_class1, authors_text, authors_class2)
        if href_values:
            print(f"Author(s): {author}.\nCount: {len(href_values)}")
            library = manager.get_setting('library', default='~/.ppp/library')
            uuid_str = str(uuid.uuid4())
            new_folder_name = os.path.join(library, uuid_str)
            saver.save_all(href_values, new_folder_name)
            create_book(author, bsparser.extract_title_value(html_code), url, uuid_str)
        else:
            print("No href found")
    else:
        print("Failed to get page html code")   