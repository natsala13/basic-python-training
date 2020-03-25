# Page 112
# Code will replicate the text from one file to the other

FILENAME1 = 'text1.txt'
FILENAME2 = 'text2.txt'
with open(FILENAME2,'r') as copy_file:
    copy_text = copy_file.read()
with open(FILENAME1,'w') as write_file:
    write_file.write(copy_text)
