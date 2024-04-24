'''Write a python function to find common divisor between two numbers in a given pair.
'''
def num_comm_div(x, y):
    result = 0
    for i in range(1, min(x, y) + 1):
        if x % i == y % i == 0:
            result += 1
    return result
'''
Standard answer: 
def ngcd(x,y):
    i=1
    while(i<=x and i<=y):
        if(x%i==0 and y%i == 0):
            gcd=i;
        i+=1
    return gcd;
def num_comm_div(x,y):
  n = ngcd(x,y)
  result = 0
  z = int(n**0.5)
  i = 1
  while(i <= z):
    if(n % i == 0):
      result += 2 
      if(i == n/i):
        result-=1
    i+=1
  return result
'''
assert num_comm_div(2,4) == 2
assert num_comm_div(2,8) == 2
assert num_comm_div(12,24) == 6
