'''Write a function to find the lcm of the given array elements.
'''
def get_lcm(l):
  num1 = l[0]
  num2 = l[1]
  lcm = num1 if num1 > num2 else num2
  while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
      for i in range(2, len(l)):
        if lcm % l[i] != 0:
          lcm += 1
          break
      else:
        return lcm
    else:
      lcm += 1
'''
Standard answer: 
def find_lcm(num1, num2): 
	if(num1>num2): 
		num = num1 
		den = num2 
	else: 
		num = num2 
		den = num1 
	rem = num % den 
	while (rem != 0): 
		num = den 
		den = rem 
		rem = num % den 
	gcd = den 
	lcm = int(int(num1 * num2)/int(gcd)) 
	return lcm 
def get_lcm(l):
  num1 = l[0]
  num2 = l[1]
  lcm = find_lcm(num1, num2)
  for i in range(2, len(l)):
    lcm = find_lcm(lcm, l[i])
  return lcm 
'''
assert get_lcm([2, 7, 3, 9, 4]) == 252
assert get_lcm([1, 2, 8, 3]) == 24
assert get_lcm([3, 8, 4, 10, 5]) == 120
