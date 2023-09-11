from bs4 import BeautifulSoup

def extract_href_values(html_code, select):
    href_values = []
    soup = BeautifulSoup(html_code, 'html.parser')
    tags = soup.select(select)
    for tag in tags:
        href_values.append(tag['href'])
    return href_values

def extract_title_value(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    title_tag = soup.title
    title_text = title_tag.string
    return title_text


def extract_authors(html_code, authors_class1, authors_text, authors_class2):
    soup = BeautifulSoup(html_code, 'html.parser')
    
    title_span = soup.find('span', class_=authors_class1, text=authors_text)
    content_div = title_span.find_next('div', class_=authors_class2)
    elements = content_div.find_all('span', class_=False)

    values = [span.text for span in elements]
    values_str = ''
    if len(values) == 1:
        values_str = values[0]
    else:
        values_str = ', '.join(values)

    return values_str
