
"""
 The MIT License (MIT)

Copyright © 2020 Batuhan Gonenc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


chars = "qwrtyuiop[]}{POIUYTREWQsghjkl;'|:LKJHGFDSAzxvnm,./?><MNBVCXZ1234567890-=+_)(*&^%$#@!~üğçşöı"

#encrypts texts
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


print("=============\nrabbit\n=============\nfor exit 'q'.\nfor help 'h'.\n=============\n=============")

while 1:
	key = input("-\n-\nenter your rabbit key :")

	if key == "q":
		break


	elif key == "h":
		print("===\na key must have different 6 number between 0-9.\nexamples:\n987654\n154378\n123456\n===")
		continue


	specialCharArray = list()
	for i in chars:
		specialCharArray.append(i)



	k1 = int(key[0])
	k2 = int(key[1])
	k3 = int(key[2])
	k4 = int(key[3])
	k5 = int(key[4])
	k6 = int(key[5])


	instead_a = chars[k1]
	instead_b = chars[k2]
	instead_c = chars[k3]
	instead_d = chars[k4]
	instead_e = chars[k5]
	instead_f = chars[k6]

	insteads = (instead_a,instead_b,instead_c,instead_d,instead_e,instead_f)

	specialCharArray[k1] = "a"
	specialCharArray[k2] = "b"
	specialCharArray[k3] = "c"
	specialCharArray[k4] = "d"
	specialCharArray[k5] = "e"
	specialCharArray[k6] = "f"

	for i in insteads:
		specialCharArray.append(i)



	willRabbited = input(">>>\nenter a text:")

	result = rabbit(willRabbited,specialCharArray)

	print("\n\n{}\n******\n".format(result))


#===============================end=of=the=program.
