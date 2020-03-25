#Page 116
import os
path_input = input("Please enter path:")
if os.path.exists(path_input):
    file_name = input("Please enter the name of the file:")
    with open(file_name, 'r') as file_content:
        print(file_content.read())
else:
    print("Directory not found")