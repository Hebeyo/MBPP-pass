'''Write a function to find the demlo number for the given number.
'''
def find_demlo(s): 
	l = len(s) 
	res = "" 
	for i in range(1,l+1): 
		res = res + str(i) 
	for i in range(l-1,0,-1): 
		res = res + str(i) 
	return res
'''
Standard answer: 
def find_demlo(s): 
	l = len(s) 
	res = "" 
	for i in range(1,l+1): 
		res = res + str(i) 
	for i in range(l-1,0,-1): 
		res = res + str(i) 
	return res 	
'''
assert find_demlo("111111") == '12345654321'
assert find_demlo("1111") == '1234321'
assert find_demlo("13333122222") == '123456789101110987654321'
