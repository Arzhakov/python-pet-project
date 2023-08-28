import requests

def fetch_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Page fetch error. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error while executing request: {e}")
        return None
    