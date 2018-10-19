print('Compound-Interest Calculator')
print('Enter The Details To Proceed')
run = True 
def ci():
	global run
	s = input('Do You Want To Find Out Compoud Interest Annually OR Semi-Annually:')
	if s == 'Quit':
		print('Goodbye')
		run = False
	else:
		run = True
	p = int(input('Enter The Principle:'))
	r = int(input('Enter The Rate OF Interest:'))
	t = int(input('Enter The Time Period(IN YEARS):'))
	if s == 'Semi-Annually':
		a = p*(1 + r/200)**2*t
	else:
		a = p*(1 + r/100)**t
	ci = a-p
	print(ci)
	print('Thank You For Using Compound-Interest Calculator')
while run:
	ci()
