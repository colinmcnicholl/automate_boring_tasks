from collatz_sequence import collatz

def call_collatz():
	print('Enter number:')
	while True:
		try:
			number = int(input())
			result = collatz(number)
			if result == 1:
				return result
		except ValueError:
			print('You must enter an integer.')
			
		
print(call_collatz())