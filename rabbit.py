
"""
 The MIT License (MIT)

Copyright © 2020 Batuhan Gonenc

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


chars = "qwertyuiop[]}{POIUYTREWQasdfghjkl;'|:LKJHGFDSAzxcvbnm,./?><MNBVCXZ1234567890-=+_)(*&^%$#@!~"

def renc(ar):
    encrypted=''
    for i in ar:
    	if i == " ":
    		encrypted += "`"
    		continue

    	try:
    		newind = (len(chars) - chars.index(i)) - 1
    		newchar = chars[newind]
    	except:
    		return "*\nan error happened with chars.\n*"

    	encrypted += newchar

    return encrypted

def rdec(ar):
	decoded=''
	for i in ar:
		if i == "`":
			decoded += ' '
			continue
		try:
			newind = (len(chars) - chars.index(i)) - 1
			newchar = chars[newind]
		except:
			return "*\nan error happened with chars.\n*"

		decoded += newchar

	return decoded

print("=============\nrabbit\n=============\n1 - encrypt\n=============\n2 - decode\n=============\nfor exit 'q'.\n=============")

while 1:
	i1 = input(">")

	if i1 == 'q':
		break

	elif i1 == '1':

		i2 = input('>>')
		print('\n')
		print(renc(i2))

	elif i1 == '2':

		i2 = input('>>')
		print('\n')
		print(rdec(i2))

	else:
		continue

#===============================end=of=the=program.
