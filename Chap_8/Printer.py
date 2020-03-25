# Page 114

import sys

file_name = input("Please enter the name of the file:")
with open(file_name, 'r') as file_content:
    print(file_content.read())
