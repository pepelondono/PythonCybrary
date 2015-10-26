import operator

saved_string=''


def remove_letter(): #Remove a selected letter from a string
	base_string=str(raw_input("enter a string: "))
	letter_remove=str(raw_input('enter letter: '))
	letter_remove=letter_remove[0]
	string_length=(len(base_string))
	location=0

	while location < string_length:
		if base_string[location] == letter_remove:
			base_string = base_string[:location]+base_string[location+1::]
			string_length -=1
		location+=1
	print 'Result: %s' % base_string

	return

def num_compare(): #Compare 2 numbers to determine the larger
	num1=int(raw_input('Enter number 1: '))
	num2=int(raw_input('Enter number 2: '))

	if num1>num2:
		print num1, 'is bigger than ', num2
	elif num1==num2:
		print num1, 'is equal to', num2
	else:
		print num1, 'is smaller than', num2

	return

def print_string(): #Print the previously stored string
	print saved_string
	return

def calculator(): #Basic calculator
	sign_dict={'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.div}
	num1=int(raw_input('Number 1: '))
	sign=str(raw_input('Action: '))
	num2=int(raw_input('Number 2: '))
	print sign_dict[sign] (num1, num2)

	return

def accept_and_store(): #Accept and store a string
	print 'Accept and store'
	global saved_string
	saved_string=str(raw_input('Input string: '))
	return

def main(): #menu goes here
	opt_list = [accept_and_store,
				calculator,
				print_string,
				num_compare,
				remove_letter]

	while(True):
		print 'SELECT OPTION: '
		print '1\tAccept and Store'
		print '2\tCalculator'
		print '3\tPrint Stored String'
		print '4\tNumber Comparison'
		print '5\tRemove letter'
		opt_choice = int(raw_input('SLECTION:'))
		opt_choice -= 1
		opt_list[opt_choice]()
	return

main()
