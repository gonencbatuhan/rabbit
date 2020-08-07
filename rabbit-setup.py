import os
import sys

print("============\nrabbit setup\n============")

border = 3
while 1:
    if border == 0:
        print("be cool and come again.\n*")
        sys.exit()

    un_input = input('enter your username in session:')

    try:
    	file = open('/home/{}/.bashrc'.format(un_input),'r')
    	content = file.read()
    	file.close()
    except:
    	print("*\nsomething went wrong.\ntry again.\n*")
    	border -= 1
    	continue

    here = os.getcwd()
    new = '\nalias rabbit="python3 {}/rabbit.py"'.format(here)
    newcontent = content + new

    file = open('/home/{}/.bashrc'.format(un_input),'w')
    file.write(newcontent)
    file.close()

    print("*\nrabbit successfully installed.\n*\nenjoy it.")

    os.remove('rabbit-setup.py')
    break

