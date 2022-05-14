class Passwords:
	"""docstring for Passwords"""
	def __init__(self):
		pass

	def CreateUserID(self):
		print("\n\nAm Create")

	def ChangePassword(self):
		print("\n\nAm Change Passwords")

	def DislpayUserID(self):
		print("\n\nAm Dislpay User ID")



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