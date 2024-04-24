'''Write a function to find n’th smart number.
'''
def smartNumber(n):
    MAX = 3000
    primes = [0] * MAX
    result = []
    for i in range(2, MAX):
        if (primes[i] == 0):
            primes[i] = 1
            j = i * 2
            while (j < MAX):
                primes[j] -= 1
                if ( (primes[j] + 3) == 0):
                    result.append(j)
                j = j + i
    result.sort()
    return result[n - 1]
'''
Standard answer: 
MAX = 3000 
def smartNumber(n): 
	primes = [0] * MAX 
	result = [] 
	for i in range(2, MAX): 
		if (primes[i] == 0): 
			primes[i] = 1 
			j = i * 2 
			while (j < MAX): 
				primes[j] -= 1 
				if ( (primes[j] + 3) == 0): 
					result.append(j) 
				j = j + i 
	result.sort() 
	return result[n - 1] 
'''
assert smartNumber(1) == 30
assert smartNumber(50) == 273
assert smartNumber(1000) == 2664
