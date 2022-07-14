# CSE422 - Theory of Computation
# String Pattern Matching with Finite Automata implementation

# defining global variable for looking at the ascii table characters. Searches extended version of ascii table
ASCII_NO_OF_CHARS = 256

'''
	The most important function in the algorithm. This function calls other helper functions and returns the result.
	It prints all occurences of pattern in the string.
'''
def searchPattern(pattern, str):
	global ASCII_NO_OF_CHARS
	lenPattern = len(pattern)
	lenString = len(str)

	TF = TFcomputation(pattern, lenPattern)	# Constructing transition table

	# Process string over Finite Automata(FA).
	state=0
	results = []

	# By traversing the created TF table it checks if there is a state in the table with the size of the entered pattern.
	for i in range(lenString):
		state = TF[state][ord(str[i])]
		if state == lenPattern:
			print("Pattern found at index : ",i-lenPattern+1)
			results.append(i-lenPattern+1)		# Collecting all index results in a results list

	return results


'''
	This function builds the TF table which
	represents Finite Automata for a given pattern
'''
def TFcomputation(pattern, lenPattern):
	global ASCII_NO_OF_CHARS

	# Create the TF table and put into zeros as many states as there are in total.
	# State number is determined after user pattern input
	TF = [[0 for i in range(ASCII_NO_OF_CHARS)]\
		for _ in range(lenPattern + 1)]

	# Checking whether the given pattern is in the given string by browsing through the states created here. 
	# If the state has changed, the TF table is updated with the value returned from the geNextState() function.
	for state in range(lenPattern + 1):
		for x in range(ASCII_NO_OF_CHARS):
			z = getNextState(pattern, lenPattern, state, x)
			TF[state][x] = z

	print("Transition Function : ")
	print(TF)

	return TF


'''
	It calculates the next state
'''
def getNextState(pattern, lenPattern, state, x):
	# If the character is same as next character in pattern, then simply increment state
	if state < lenPattern and x == ord(pattern[state]):
		return state+1

	i=0

	# nextstate stores the result and it will be the next state
	# nextstate contains the longest prefix
	# Starting from the largest possible value and stop when you find a prefix which is also suffix
	for nextstate in range(state, 0, -1):
		if ord(pattern[nextstate - 1]) == x:
			while(i < nextstate - 1):
				if pattern[i] != pattern[state-nextstate+1+i]:
					break
				i+=1
			if i == nextstate-1:
				return nextstate
	return 0

