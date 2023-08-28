import time
import os
import settings

manager = settings.SettingsManager()

def encrypt(file_path):
    start_time = time.time()

    key = int(manager.get_setting('salt', default='200'))

    with open(file_path, 'rb') as file:
        original_data = file.read()

    encrypted_data = bytearray()
    for byte in original_data:
        encrypted_byte = (byte + key) % 256
        encrypted_data.append(encrypted_byte)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'File {file_path} encrypted. Execution time: {elapsed_time:.4f} sec')

def decrypt(file_path):
    start_time = time.time()

    key = int(manager.get_setting('salt', default='200'))

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = bytearray()
    for byte in encrypted_data:
        decrypted_byte = (byte - key) % 256
        decrypted_data.append(decrypted_byte)

    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'File {file_path} decrypted. Execution time: {elapsed_time:.4f} sec')

def decrypt_files_in_directory(directory_path):
    tmp_file_path = os.path.join(directory_path, '___tmp___')
    if not os.path.isfile(tmp_file_path):
        print("File ___tmp___ not found.")
    else:
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file != '___tmp___':
                    file_path = os.path.join(root, file)
                    decrypt(file_path)
        
        print("Completed.")
        