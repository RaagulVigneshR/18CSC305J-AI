# Python program of the above approach
# Stores the overlapping state
dp = [[-1 for i in range(3001)] for j in range(1001)]

# Recursive function to find the maximum
# number of bananas that can be transferred
# to A distance using memoization
def recBananaCnt(A, B, C):

	# Base Case where count of bananas
	# is less that the given distance
	if (B <= A):
		return 0
		
	# Base Case where count of bananas
	# is less that camel's capacity
	if (B <= C):
		return B - A
	
	# Base Case where distance = 0
	if (A == 0):
		return B
	

	# If the current state is already
	# calculated
	if (dp[A][B] != -1):
		return dp[A][B]
	

	# Stores the maximum count of bananas
	maxCount = -2**32

	# Stores the number of trips to transfer
	# B bananas using a camel of capacity C
	tripCount = ((2 * B) // C) - 1 if(B % C == 0 ) else ((2 * B) // C) + 1

	# Loop to iterate over all the
	# breakpoints in range [1, A]
	for i in range(1,A+1):

		# Recursive call over the
		# remaining path
		curCount = recBananaCnt(A - i, B - tripCount * i, C)

		# Update the maxCount
		if (curCount > maxCount):
			maxCount = curCount

			# Memoize the current value
			dp[A][B] = maxCount
		
	# Return answer
	return maxCount

# Function to find the maximum number of
# bananas that can be transferred
def maxBananaCnt(A, B, C):

	# Function Call
	return recBananaCnt(A, B, C)

# Driver Code
A = 1000
B = 3000
C = 1000
print(maxBananaCnt(A, B, C))
