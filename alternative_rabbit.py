import rabbitmodule, sys


def menu(input1):
	if(input1 == "o"):
		print("-\ng - generate a key\nk - enter a key\nq - quit\nd - delete all rabbitlogs\n-")

	elif input1 == "q":	
		sys.exit()

	elif input1 == "g":
			print("\n\n" + rabbitmodule.key_generator())

	elif input1 == "d":
		import os
		os.chdir("rabbitlogs/")
		for a,b,c in os.walk(os.getcwd()):
			for i in c:
				os.remove(i)


		print("-\nall rabbitlogs deleted successfully.")
		os.chdir("../")
		

	elif input1 == "k":

		keyflag, key = rabbitmodule.key_validator()


		
		if keyflag:

			unique_array = rabbitmodule.get_unique_array(key)


			text=""

			while 1:
				way = input("which one do you prefer ?\na path to the .txt file (p)\na simple message by hand now (m) :")

				if way == "p":
						
					path_to_file = input("-\nenter the path to file :")

					try:
						file = open(path_to_file,"r")
						text = file.read()
						file.close()
						break
					except:
						print("-\n#something went wrong.#\n-\n-")
						continue

				elif way == "m":
					text = input("-\nenter your text :")
					break
				else:
					print("-\n#unvalid input#\n-")
					continue

			rabbited = rabbitmodule.rabbiter(text, unique_array)
                        print(f"---\n\n {rabbited}\n---\n")

			rabbitmodule.logger(key, text, rabbited)
		else:
			print("\nunvalid key.")


while 1:
	input1 = input("choose one (o for options):")

	menu(input1)
