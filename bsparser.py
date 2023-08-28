from bs4 import BeautifulSoup

def extract_href_values(html_code, select):
    href_values = []
    soup = BeautifulSoup(html_code, 'html.parser')
    tags = soup.select(select)
    for tag in tags:
        href_values.append(tag['href'])
    return href_values
