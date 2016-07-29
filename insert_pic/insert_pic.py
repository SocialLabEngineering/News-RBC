# import libraries
import os
from bs4 import BeautifulSoup

# open svg file without pictures
# in open() insert path to svg file
with open('Курултай.svg', 'r') as f:
    doc = f.read()
soup = BeautifulSoup(doc, 'lxml')
for g in soup.findAll('g'):
    children = g.children
    for child in children:
        if child.name == 'text':
            name = g.find('text').text
            # path to folder with pictures
            path_to_folder = ''
            # create name of picture
            jpg_name = path_to_folder + '_'.join(name.split()) + '.jpg'
            # check if there is picture with this name
            print(jpg_name)
            if os.path.isfile(jpg_name):
                print('found!')
                rect = g.rect
                attrs = rect.attrs
                attrs.pop('fill', None)
                attrs['xlink:href'] = jpg_name
                image = soup.new_tag('image')
                image.attrs = attrs
                rect.replace_with(image)
# save new svg file with pictures
# if open() can be any name of new file
invalid_tags = ['html', 'body']
for tag in invalid_tags: 
    for match in soup.findAll(tag):
        match.replaceWithChildren()
with open('output.svg', 'w') as f:
    f.write(str(soup))