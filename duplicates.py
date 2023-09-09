#!/usr/bin/python

import os
import hashlib

def calculate_directory_hash(directory_path):
    """Calculates the hash sum of directory content."""
    file_hashes = []
    
    for root, _, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                file_contents = f.read()
                file_hash = hashlib.sha256(file_contents).hexdigest()
                file_hashes.append(file_hash)
    
    # Combine hashes of all files in the directory
    combined_hash = hashlib.sha256(''.join(file_hashes).encode()).hexdigest()
    return combined_hash

def find_duplicates(path):
    """Finds directory duplicates based on content."""
    directory_hashes = {}
    duplicates = []
    
    for dir_name in os.listdir(path):
        dir_path = os.path.join(path, dir_name)
        
        if os.path.isdir(dir_path):
            dir_hash = calculate_directory_hash(dir_path)
            if dir_hash in directory_hashes:
                duplicates.append((directory_hashes[dir_hash], dir_name))
            else:
                directory_hashes[dir_hash] = dir_name
    
    return duplicates

if __name__ == "__main__":
    path_to_search = input("Enter the path to search for duplicates: ")
    duplicates_list = find_duplicates(path_to_search)
    
    if duplicates_list:
        print("Found the following directory duplicates:")
        for duplicate in duplicates_list:
            print(f"Directories '{duplicate[0]}' and '{duplicate[1]}' have identical content.")
    else:
        print("No duplicates found.")
