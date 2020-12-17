
"""
 The MIT License (MIT)

Copyright © 2020 batuhangonenc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import sys,os
from random import randint as rInt
from time import time
#date-generator
from datetime import datetime
now= datetime.now()
today = now.strftime("%D")
#---

chars = "abcdefqwrtyuiop[]}{POIUYTREWQsghjkl;'|:LKJHGFDSAzxvnm,./?><MNBVCXZ1234567890-=+_)(*&^%$#@!~ığüşöçİĞÜŞÖÇ"

#key-generator

def keyGenerator():
	generalPurposeStr = "abcdefghijklmnopqrstuvwxyz()[]}{:;,./?><+_*#$&!'^ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	
	used=list()

	theKey=""
	
	keySections = list()
	
	ct = 10

	while ct > 0 :
		integerWeNeed_1 = rInt(0,(len(generalPurposeStr) - 1))
		charWeNeed = generalPurposeStr[integerWeNeed_1]

		control_flag = False
		for i in used:
			if i == charWeNeed:
				control_flag = True

		if control_flag:
			continue


		integerWeNeed_2 = rInt(0,92)

		for i in used:
			if i == integerWeNeed_2:
				control_flag = True

		if control_flag:
			continue


		keySection = "{}{}".format(charWeNeed,integerWeNeed_2)
		keySections.append(keySection)

		#appends useds to a list to dont use they again
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
print("\n\n=============\nrabbit\n=============\nfor exit 'q'.\nfor generate a key 'g'.\nfor enter a key 'k'.\n=============")

while 1:
	key = ""
	while 1:
		first_input = input("\n\n-------------\nchoose one ('o' for options):")

		if first_input == "o":
			print("----------\ng - generate a key\nq - exit\nk - enter a rabbit key\n----------")
		elif first_input == "q":
			sys.exit()

		elif first_input == "g":
			keyGenerator()
			continue

		elif first_input == "k":
			keyflag = True

			ct = 3
			while 1:
				if ct == 0:
					print("-----\nyou entered a lot of wrong key.\ntry another time.")
					keyflag = False
					break

				key = input("----------\nenter a key :")

				if not(key.count("-")==9):
					ct -= 1
					continue

				break

			if keyflag:
				break

			continue

		else:
			continue


	key_backup = key

	if key == "q":
		break


	elif key == "g":
		keyGenerator()
		continue


	#an unique character array to encrypt
	specialCharArray = list()
	for i in chars:
		specialCharArray.append(i)

	#makes key ready to use
	splitted_keys = key.split("-")


	#fetch chars from sections of key
	k1_1 = splitted_keys[0][0]
	k2_1 = splitted_keys[1][0]
	k3_1 = splitted_keys[2][0]
	k4_1 = splitted_keys[3][0]
	k5_1 = splitted_keys[4][0]
	k6_1 = splitted_keys[5][0]
	k7_1 = splitted_keys[6][0]
	k8_1 = splitted_keys[7][0]
	k9_1 = splitted_keys[8][0]
	k10_1 = splitted_keys[9][0]

	#remove chars from list
	specialCharArray.remove(k1_1)
	specialCharArray.remove(k2_1)
	specialCharArray.remove(k3_1)
	specialCharArray.remove(k4_1)
	specialCharArray.remove(k5_1)
	specialCharArray.remove(k6_1)
	specialCharArray.remove(k7_1)
	specialCharArray.remove(k8_1)
	specialCharArray.remove(k9_1)
	specialCharArray.remove(k10_1)

	#fetch indexes of chars in key
	k1_2 = int(splitted_keys[0].replace(k1_1,""))
	k2_2 = int(splitted_keys[1].replace(k2_1,""))
	k3_2 = int(splitted_keys[2].replace(k3_1,""))
	k4_2 = int(splitted_keys[3].replace(k4_1,""))
	k5_2 = int(splitted_keys[4].replace(k5_1,""))
	k6_2 = int(splitted_keys[5].replace(k6_1,""))
	k7_2 = int(splitted_keys[6].replace(k7_1,""))
	k8_2 = int(splitted_keys[7].replace(k8_1,""))
	k9_2 = int(splitted_keys[8].replace(k9_1,""))
	k10_2 = int(splitted_keys[9].replace(k10_1,""))

	#backup of old chars
	instead_1 = specialCharArray[k1_2]
	instead_2 = specialCharArray[k2_2]
	instead_3 = specialCharArray[k3_2]
	instead_4 = specialCharArray[k4_2]
	instead_5 = specialCharArray[k5_2]
	instead_6 = specialCharArray[k6_2]
	instead_7 = specialCharArray[k7_2]
	instead_8 = specialCharArray[k8_2]
	instead_9 = specialCharArray[k9_2]
	instead_10 = specialCharArray[k10_2]

	insteads = [instead_1,instead_2,instead_3,instead_4,instead_5,instead_6,instead_7,instead_8,instead_9,instead_10]

	#declares new chars instead olds
	specialCharArray[k1_2] = splitted_keys[0][0]
	specialCharArray[k2_2] = splitted_keys[1][0]
	specialCharArray[k3_2] = splitted_keys[2][0]
	specialCharArray[k4_2] = splitted_keys[3][0]
	specialCharArray[k5_2] = splitted_keys[4][0]
	specialCharArray[k6_2] = splitted_keys[5][0]
	specialCharArray[k7_2] = splitted_keys[6][0]
	specialCharArray[k8_2] = splitted_keys[7][0]
	specialCharArray[k9_2] = splitted_keys[8][0]
	specialCharArray[k10_2] = splitted_keys[9][0]

	#appends old chars to list too
	for i in insteads:
		specialCharArray.append(i)


	#finds a text to rabbited
	willRabbited = ""
	
	while 1:
		way = input("which one do you prefer ?\na path to the .txt file (p)\na simple message by hand now (m) :")

		if way == "p":
			
			path_to_file = input("-\nenter the path to file :")

			try:
				file = open(path_to_file,"r")
				willRabbited = file.read()
				file.close()
				break
			except:
				print("-\n#something went wrong.#\n-\n-")
				continue

		elif way == "m":
			willRabbited = input("-\nenter your text :")
			break
		else:
			print("-\n#unvalid input#\n-")
			continue

	#rabbited-text
	start = time()
	result = rabbit(willRabbited,specialCharArray)
	end = time()

	#how long it take
	takes = end - start


	print("\n\n{}\n******\n".format(result))



	while 1:
		last_request = input("---\nare you want to save it ? ( y / n ) :")

		if last_request.lower() == "y":

			try:
				os.chdir("rabbitlogs")
			except:
				os.mkdir("rabbitlogs")
				os.chdir("rabbitlogs")


			
			today = today.replace("/","")

			lastlognum = 0
			comparenum = 1


			for a,b,c in os.walk(os.getcwd()):
				for i in c:
					if i.startswith("rabbitlog"):
						prelog = i.replace("rabbitlog","")
						prelog = prelog.replace(".txt","")
						date = prelog[2:]

						if (date == today):
							comparenum = int(prelog[0])

							if (comparenum > lastlognum):
								lastlognum = comparenum


						
			newlognum = lastlognum + 1


			filename = "rabbitlog{}_{}.txt".format(newlognum,today)
			filename = filename.replace("/","")
			file = open(filename,"w")

			now = datetime.now()
			now = now.strftime("%x %X")

			content="key : {}\n\ntext : {}\n\nrabbited : {}\n\nit took {} seconds to compute\n\n{}".format(key_backup,willRabbited,result,takes,now)

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
