import os
import requests
import crypto

def save_all(href_values, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for idx, href in enumerate(href_values, start=1):
        try:
            response = requests.get(href)
            if response.status_code == 200:
                file_extension = href.split('.')[-1]
                file_path = os.path.join(directory, f'{idx:02d}.{file_extension}')
                with open(file_path, 'wb') as content_file:
                    content_file.write(response.content)
                print(f'File {idx} saved as {file_path}')
                crypto.encrypt(file_path)
            else:
                print(f"Content fetch error. Code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error while executing request: {e}")
            