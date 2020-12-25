import os
import sys

print("============\nrabbit setup\n============")

uname = os.getlogin()
here = os.getcwd()
new = '\nalias rabbit="python3 {}/rabbit.py"'.format(here)
newcontent = content + new

file = open('/home/{}/.bashrc'.format(uname),'w')
file.write(newcontent)
file.close()

print("*\nrabbit successfully installed.\n*\nenjoy it.")
    
li = input("*\npress enter to exit.\n*")
    
os.remove('rabbit-setup.py')
os.remove('readme.txt')
os.remove('LICENSE')

