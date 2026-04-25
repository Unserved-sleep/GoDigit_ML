import os

open("C:\\Users\\Admin\\Downloads\\practice.txt", 'r') # mode(r, a, w, x, t,b)  could be to read, write, update

f = open("C:\\Users\\Admin\\Downloads\\practice.txt")
print(f) #  mode='r' encoding='UTF-8'>

#txt = f.read()
#txt1 = f.read(10) #first 10 letters
#line = f.readline() #read first line
lines = f.readlines() #list of lines
#print(txt)
#print(type(txt))
#print(txt1)
print(lines)
print(type(lines))

with open("C:\\Users\\Admin\\Downloads\\practice.txt",'a') as f:
    f.write('This text has to be appended at the end')

f = open("C:\\Users\\Admin\\Downloads\\practice.txt")
print(f.read())

with open('C:\\Users\\Admin\\Downloads\\practice1.txt','w') as f:
    f.write('This text will be written in a newly created file')
    #creates a new file

os.remove('C:\\Users\\Admin\\Downloads\\practice1.txt') #deletes file
"""
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
"""

f.close()