class Passwords:
	def __init__(self):
		self.UserIDs = []
		self.passwords = []

		self.UserAccount = [self.UserIDs, self.passwords]

	def CreateUserID(self):
		UserID = input("\n\nEnter your User ID: ")
		
		if UserID in self.UserIDs:
			print("User ID already exit")
		else:
			password = input("Enter a password: ")
			strength = 0
			print(len(password))
			if len(password) > 8:
				strength += 1

			print(strength)

			self.passwords.append(password)

			self.UserIDs.append(UserID)


	def ChangePassword(self):
		print("\n\nAm Change Passwords")

	def DislpayUserID(self):
		print("UserID   :  Password")
		for account in self.UserAccount:
			print(account)

		for item in self.UserIDs:
			print(item)



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