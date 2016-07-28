import time
from bs4 import BeautifulSoup
from urllib import request

counter = 1

def clear_str(s):
    s = s.lower()
    s = s.replace(chr(171), ' ')
    s = s.replace(chr(187), ' ')
    s = s.replace('.', ' ')
    s = s.replace('(', ' ')
    s = s.replace(')', ' ')
    s = s.replace(',', ' ')
    s = s.replace('.', ' ')
    s = s.replace(';', ' ')
    s = s.replace(chr(8220), ' ')
    s = s.replace(chr(8222), ' ')
    s = s.replace(chr(8230), ' ')
    s = s.replace(chr(34), ' ')
    s = s.replace('/', ' ')
    s = s.replace('\n', ' ')
    s = s.replace('\t', ' ')
    s = s.replace('\r', ' ')
    return s

def extract_text(url):
    try:
        html = request.urlopen(url).read()
    except:
        html = ''
    soup = BeautifulSoup(html, 'html.parser')
    text = ''
    for p in soup.find_all('p'):
        if not p.has_attr('class'):
            text += p.text.strip() + ' '
    text = clear_str(text)
    return text

if __name__ == '__main__':
    with open('urls.txt', 'r') as input:
        urls = input.read().split('\n')

    for url in urls:
        text = extract_text(url)
        f = open('texts.txt', 'a')
        f.write(text)
        f.write('\n')
        print('Extracted {} news'.format(counter))
        counter += 1
