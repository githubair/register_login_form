from getpass import getpass

# Simply register and login form in python

print('Simply registration form')
keyz ={'asd': 'zxc', 'qwe': 'asd'}

n = 5
i = 0
while i < n:

	def welcome():
		print('Please select operation: \n'
			'1. For register\n' 
			'2. For login\n'
			'3. Show info\n'
			'For exit press CTRL+C \n')
		select = input('Press: ')

		if select == '1':
			joinform()
		elif select == '2':
			loginform()
		elif select == '3':
			print('Stored info: \n', keyz, '\n')
		else:
			print ('invalid input \n')


	def joinform():
		lj = input('Choose your login: ')
		pj = getpass('Choose your password: ')
		keyz[lj]=pj
		return welcome()
		

	def loginform():
		ll = input('Enter your login: ')
		pl = getpass('Enter you password: ')
		z = (ll, pl) in keyz.items()
		if z == True:
			print ('\n password is ok! \n')
		else:
			print('\n no! \n')

	welcome()
	i += 1



if __name__ == '__main__':
	 welcome()