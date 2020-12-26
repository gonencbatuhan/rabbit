import os
import sys

print("============\nrabbit setup\n============")

content = ""

while 1:
    uname = input("username:")

    try:
        f = open(f"/home/{uname}/.bashrc","r")
        content = f.read()
        f.close()
        break
    except:
        print("unvalid username.")
        continue


here = os.getcwd()
new = f'\nalias rabbit="python3 {here}/rabbit.py"'
newcontent = content + new

file = open(f'/home/{uname}/.bashrc','w')
file.write(newcontent)
file.close()

print("*\nrabbit successfully installed.\n*\nenjoy it.")
    
li = input("*\npress enter to exit.\n*")
    
os.remove('rabbit-setup.py')
os.remove('readme.txt')
os.remove('LICENSE')

