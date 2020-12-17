
"""
 The MIT License (MIT)

Copyright © 2020 batuhangonenc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from random import randint as rInt

#date-generator
from datetime import datetime
now= datetime.now()
today = now.strftime("%D")
#---

chars = "abcdefqwrtyuiop[]}{POIUYTREWQsghjkl;'|:LKJHGFDSAzxvnm,./?><MNBVCXZ1234567890-=+_)(*&^%$#@!~üğçşöı"

#key-generator

def keyGenerator():
	generalPurposeStr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	used=list()

	theKey=""
	
	keySections = list()
	
	ct = 6

	while ct > 0 :
		integerWeNeed_1 = rInt(0,(len(generalPurposeStr) - 1))
		charWeNeed = generalPurposeStr[integerWeNeed_1]

		control_flag = False
		for i in used:
			if i == charWeNeed:
				control_flag = True

		if control_flag:
			continue


		integerWeNeed_2 = rInt(0,90)

		for i in used:
			if i == integerWeNeed_2:
				control_flag = True

		if control_flag:
			continue


		keySection = "{}{}".format(charWeNeed,integerWeNeed_2)
		keySections.append(keySection)

		used.append(charWeNeed)
		used.append(integerWeNeed_2)

		ct -= 1

	theKey = "-".join(keySections)

	print("-\n--\n---\nyour key is ready below:\n{}\n=================".format(theKey))






#function that decodes or encrypts texts
def rabbit(ar,char_array):
    rabbited=''
    for i in ar:
    	if i == " ":
    		rabbited += "`"
    		continue

    	elif i == "`":
    		rabbited += " "
    		continue

    	try:
    		newind = (len(char_array) - char_array.index(i)) - 1
    		newchar = char_array[newind]
    	except:
    		return "*\nan error happened with chars.\n*"

    	rabbited += newchar

    return rabbited


#then program starts
print("=============\nrabbit v2\n=============\nfor exit 'q'.\nfor generate a key 'g'.\n=============\n=============")

while 1:
	key = input("-\n-\nenter your rabbit key :")

	key_backup = key

	if key == "q":
		break


	elif key == "g":
		keyGenerator()
		continue


	specialCharArray = list()
	for i in chars:
		specialCharArray.append(i)


	splitted_keys = key.split("-")

	k1_1 = splitted_keys[0][0]
	k2_1 = splitted_keys[1][0]
	k3_1 = splitted_keys[2][0]
	k4_1 = splitted_keys[3][0]
	k5_1 = splitted_keys[4][0]
	k6_1 = splitted_keys[5][0]

	specialCharArray.remove(k1_1)
	specialCharArray.remove(k2_1)
	specialCharArray.remove(k3_1)
	specialCharArray.remove(k4_1)
	specialCharArray.remove(k5_1)
	specialCharArray.remove(k6_1)

	k1_2 = int(splitted_keys[0].replace(k1_1,""))
	k2_2 = int(splitted_keys[1].replace(k2_1,""))
	k3_2 = int(splitted_keys[2].replace(k3_1,""))
	k4_2 = int(splitted_keys[3].replace(k4_1,""))
	k5_2 = int(splitted_keys[4].replace(k5_1,""))
	k6_2 = int(splitted_keys[5].replace(k6_1,""))


	instead_1 = specialCharArray[k1_2]
	instead_2 = specialCharArray[k2_2]
	instead_3 = specialCharArray[k3_2]
	instead_4 = specialCharArray[k4_2]
	instead_5 = specialCharArray[k5_2]
	instead_6 = specialCharArray[k6_2]

	insteads = [instead_1,instead_2,instead_3,instead_4,instead_5,instead_6]

	specialCharArray[k1_2] = splitted_keys[0][0]
	specialCharArray[k2_2] = splitted_keys[1][0]
	specialCharArray[k3_2] = splitted_keys[2][0]
	specialCharArray[k4_2] = splitted_keys[3][0]
	specialCharArray[k5_2] = splitted_keys[4][0]
	specialCharArray[k6_2] = splitted_keys[5][0]

	for i in insteads:
		specialCharArray.append(i)


	#the text will be rabbited
	willRabbited = input(">>>\nenter a text:")

	#rabbited-text
	result = rabbit(willRabbited,specialCharArray)

	print("\n\n{}\n******\n".format(result))



	while 1:
		last_request = input("---\nare you want to save it ? ( y / n ) :")

		if last_request.lower() == "y":

			filename = "rabbitlog_{}.txt".format(today)
			filename = filename.replace("/","l")
			file = open(filename,"w")
			content="key : {}\n\ntext : {}".format(key_backup,result)

			file.write(content)
			file.close()

			print("-\nprocess saved successfully.\n-")
			break

		elif last_request.lower() == "n":
			print("-\nok , no problem.\n-")
			break


		else:
			print("-\n#unvalid input#\n-")
			continue




#===============================end=of=the=program.
