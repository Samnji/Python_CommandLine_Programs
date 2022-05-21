import csv

class Passwords:
	def __init__(self):
		self.file0 = open("accounts.csv", 'w')

	def CreateUserID(self):
		UserID = input("\n\nEnter your User ID: ")
		
		self.file= open("accounts.csv", 'r')
		for row in self.file:
			if UserID in row:
				print("User ID already exit")
		else:
			self.file1= open("accounts.csv", 'a')
			password = input("Enter a password: ")
			strength = 0
			length = False
			lower = False
			upper = False
			symbol = False

			print(len(password))

			for item in password:
				if len(password) >= 8:
					length = True

				elif item.islower():
					lower = True

				elif item.isupper():
					upper = True

				elif '!' or '£' or '$' or '%' or '&' or '<' or '*' or '@' in password:
					symbol = True


			if length:
				strength += 1

			elif lower:
				strength += 1

			elif upper:
				strength += 1
			print(strength)
			self.file1.write(f'{UserID}, {password}\n')

	def ChangePassword(self):
		print("\n\nAm Change Passwords")

	def DislpayUserID(self):
		print("UserID   :  Password")

		self.file2 = open("accounts.csv", 'r')
		
		for row in self.file2:
			line = row.split(',')

			print(f'{line[0]}  	:  {line[1]}')

p = Passwords()

while True:
	print("\n\n\t\t\t*********Passwords Storage************\n\n")
	print("\t1) Create a new User ID\n")
	print("\t2) Change a password\n")
	print("\t3) Display all User IDs\n")
	print("\t4) Quit\n\n")

	choice = int(input("What's your selection: "))

	if choice == 1:
		p.CreateUserID()

	elif choice == 2:
		p.ChangePassword()

	elif choice == 3:
		p.DislpayUserID()

	elif choice == 4:
		exit()

	else:
		print("Enter a valid choice")
		continue