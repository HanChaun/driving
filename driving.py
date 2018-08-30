country = input('Which country are you from:')
age = input('pls input your age:')
age = int(age)
if country == 'Taiwan':
	if age >= 18 :
		print('you can test for Driving Licence ')
	else:
		print('you can not test for Driving Licence ')