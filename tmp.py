#!/usr/bin/python3

import crypto
import uuid
import os
import shutil
import uuid

def tmp(directory):
    tmp_directory = os.path.join(os.path.dirname(library), 'tmp')
    os.makedirs(tmp_directory, exist_ok=True)
    list_of_directories = [dir for dir in os.listdir(library) if os.path.isdir(os.path.join(library, dir))]
    for dir_name in list_of_directories:
        dir_path = os.path.join(library, dir_name)
        uuid_value = str(uuid.uuid4())
        
        for file_name in os.listdir(dir_path):
            source_file_path = os.path.join(dir_path, file_name)
            new_file_name = f'{uuid_value}_{file_name}'
            new_file_path = os.path.join(tmp_directory, new_file_name)
            
            shutil.copy2(source_file_path, new_file_path)
            crypto.decrypt(new_file_path)
            print(f'File copied: {file_name} -> {new_file_name}')

    print("Completed.")

library = input("Input library path: ")

tmp(library)
