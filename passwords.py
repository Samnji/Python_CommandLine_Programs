import csv

class Passwords:
	def __init__(self):
		self.file0 = open("accounts.csv", 'r')
		self.user_ids = []
		self.accounts = []


		for row in self.file0:
			line = row.split(', ')
			self.accounts.append(line)

		for item in self.accounts:
			self.user_ids.append(item[0])
		#print(self.user_ids)
		#print(self.accounts)
	def checkScore():
		while True:
			score = 0
			length = False
			lower = False
			upper = False
			number = False
			symbol = False
			numbers = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
			symbols = [ '!', '£', '$', '%', '&', '<', '*', '@', '#', '^']


			password = input("Enter a strong password: ")

			if len(password) >= 8:
				length = True

			for item in password:
				if item.islower():
					lower = True

				elif item.isupper():
					upper = True

				elif item in numbers:
					number = True

				elif item in symbols:
					symbol = True

			if length:
				score = score + 1

			if lower:
				score = score + 1

			if upper:
				score = score + 1


			if number:
				score = score + 1

			if symbol:
				score = score + 1


			print(f'score = {score}')

		
			if score == 1 or score == 2:
				print("Weak password")

			elif score == 3 or score == 4:
				print("This password could be improved.")
			elif score == 5:
				return password
				break

	def createUser_id(self):
		try_again = True
		
		while try_again:	
			self.user_id = input(r"""Enter a suitable User Id or:
  type Quit to quit program: """)

			if self.user_id.lower() == "quit":
				try_again = False

			else: 
				if self.user_id in self.user_ids:
					print("User Id already taken")
				else:
					password = Passwords.checkScore()

					self.user_ids.append(self.user_id)
					account = self.user_id + ", " + password + "\n"

					print(self.user_id)
					with open("accounts.csv", 'a') as file1:
						#print(str(account))
						file1.write(str(account))

	def changePassword(self):
		try_again = True

		while try_again:
			user_id = input("""Enter the User Id for the account you want change the password:
or type Quit to quit program: """)


			if self.user_id.lower() == "quit":
				try_again = False

			else: 
				if user_id in self.user_ids:
					for account in self.accounts:
						if user_id in account:
							password = Passwords.checkScore()
							print(password)
							account[1] = password + "\n"
					with open("accounts.csv", 'w') as file2:
						for account in self.accounts:
							file2.write(", ".join(account))
					# print(self.accounts)

				else:
					print("User Id does not exist")

	def dislpayUser_id(self):
		print("user_ids")

		for item in self.user_ids:
			print(item)

		

p = Passwords()

while True:
	print(r"""
	    _____   _____   ______   ______   _       _   _______   _    __       _   _______
	   |  _  | |___  | |  ____| |  ____| | |     | | |  ___  | | | _/_/      | | |  _____|
	   | |_| |  ___| | | |____  | |____	 | | __  | | | |   | | | |/ /  _____ | | | |_____
	   |  ___| |  _  | |____  | |____  | | |/  \ | | | |   | | |  _/  /  __ '| | |_____  |
	   | |	   | |_| |  ____| |  ____| | |   /\ \| | | |___| | | |   |  (__| | |  _____| |
	   |_|	   |_____| |______| |______| |__/  \___| |_______| |_|    \______|_| |_______|
		""")
	print("\t1) Create a new User ID\n")
	print("\t2) Change a password\n")
	print("\t3) Display all User IDs\n")
	print("\t4) Quit\n\n")

	choice = int(input("What's your selection: "))

	if choice == 1:
		p.createUser_id()

	elif choice == 2:
		p.changePassword()

	elif choice == 3:
		p.dislpayUser_id()

	elif choice == 4:
		exit()

	else:
		print("Enter a valid choice")
		continue