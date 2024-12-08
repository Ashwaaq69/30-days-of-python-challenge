#File Handling
# In Python to handle data we use open() built-in function.
# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

# Opening Files for Reading
# f = open('./files/reading_file_example.txt')
# print(f)


# f = open('./day18/files/reading_file_example.txt')
# txt = f.read()
# print(type(txt))
# print(txt)
# f.close()

# Instead of printing all the text, let us print the first 10 characters of the text file.


# f = open('./day18/files/reading_file_example.txt')
# txt = f.read(10)
# print(type(txt))
# print(txt)
# f.close()


# readline(): read only the first line

# f = open('./day18/files/reading_file_example.txt')
# txt = f.readline()
# print(type(txt))
# print(txt)
# f.close()

# readlines(): read all the text line by line and returns a list of lines

# f = open('./day18/files/reading_file_example.txt')
# txt = f.readlines()
# print(type(txt))
# print(txt)
# f.close()

# Another way to get all the lines as a list is using splitlines():


# f = open('./day18/files/reading_file_example.txt')
# txt = f.read().splitlines()
# print(type(txt))
# print(txt)
# f.close()

# with open('./day18/files/reading_file_example.txt') as f:
#     lines = f.read().splitlines()
#     print(type(lines))
#     print(lines)
    
    
# Opening Files for Writing and Updating
# Let us append some text to the file we have been reading:


# with open('./day18/files/reading_file_example.txt','a') as f:
#     f.write('This text has to be appended at the end')
    
    # The method below creates a new file, if the file does not exist:


# with open('./day18/files/reading_file_example.txt','a','w') as f:
#     f.write('This text will be written in a newly created file')


# Deleting Files

# import os
# os.remove('./day18/files/example.txt')

# if os.path.exists('./day18/files/example.txt'):
#     os.remove('./day18/files/example.txt')
# else:
#     print('The file does not exist')


# File Types
#txt
# File with json Extension

# dictionary
# person_dct= {
#     "name":"ashuu",
#     "country":"somali",
#     "city":"mogadisho",
#     "skills":["JavaScrip", "React","Python"]
# }
# # JSON: A string form a dictionary

# person_json = "{'name': 'ashuu', 'country': 'somali', 'city': 'mogadisho', 'skills': ['JavaScrip', 'React', 'Python']}"

# # we use three quotes and make it multiple line to make it more readable

# person_json = '''{
#     "name":"ashuu",
#     "country":"somali",
#     "city":"mogadisho",
#     "skills":["JavaScrip", "React","Python"]
# }'''

# print(person_dct['name'])

import json

# person_json= '''{
#     "name":"ashuu",
#     "country":"somali",
#     "city":"mogadisho",
#     "skills":["JavaScrip", "React","Python"]
# }'''
# # let's change JSON to dictionary

# person_dct = json.loads(person_json)
# print(type(person_dct))
# print(person_dct)
# print(person_dct['name'])


# Changing Dictionary to JSON

# python dictionary
# person = {
#     "name": "ashuu",
#     "country": "somali",
#     "city": "mogadisho",
#     "skills": ["JavaScrip", "React", "Python"]
# }
# # let's convert it to  json
# person_json = json.dumps(person, indent=4)
# print(type(person_json))
# print(person_json)

#Saving as JSON File

# person = {
#     "name": "ashuu",
#     "country": "somali",
#     "city": "mogadisho",
#     "skills": ["JavaScrip", "React", "Python"]
# }

# with open('./day18/files/json_example.json', 'w', encoding= 'utf-8')as f:
#     json.dump(person, f, ensure_ascii=False, indent=4)


# import csv
#csv
# with open('./day18/files/csv_example.csv') as f:
#     csv_reader = csv.reader(f, delimiter=',') 
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are :{", ".join(row)}')
#             line_count += 1
#         else:
#             print(
#                 f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
#             line_count += 1
#     print(f'Number of lines:  {line_count}')

#File with xlsx Extension

# import xlrd
# excel_book = xlrd.open_workbook('sample.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)


# File with xml Extension


# import xml.etree.ElementTree as ET
# tree = ET.parse('./day18/files/xml_example.xml')
# root = tree.getroot()
# print('Root tag:', root.tag)
# print('Attribute:', root.attrib)
# for child in root:
#     print('field: ', child.tag)