def is_prime(input):
	"""This functions goal is to check if an input number is prime."""
	# I included a try-except block to account for a user inputing
	# a string or a float.
	try:
		# First, the input is converted to an integer.  
		integer_input = int(input)
		# Then, Python checks if it is a positive value.
		if integer_input > 0:
			# A for loop is used here to go through each number from 2
			# to the input number. 
			for i in range(2, (integer_input)):
				# The input_number is divided by each number in the for loops range.
				# If no remainder is found, it is not prime and the loop is exited.  
				if (integer_input % i) == 0:
					return(str(integer_input) + " is not a prime number.")
					break
			else:
				return(str(integer_input) + " is a prime number.")
		else:
			return("The number has to be a positive, whole number")
	except ValueError:
		return("You must enter a positive, whole number")
									
while True:
	"""This while loop continuly asks the user for a number to check
	if it is prime or until the user enters 'q' to quit."""
	prompt = "Enter a number and I will tell you if it is prime, "
	prompt += "\nor enter 'q' to exit: "
	ask = input(prompt)
	
	if ask == 'q':
		break
	
	print(is_prime(ask))
