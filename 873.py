'''Write a function to solve the fibonacci sequence using recursion.
'''
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return (fibonacci(n - 1) + fibonacci(n - 2))
'''
Standard answer: 
def fibonacci(n):
  if n == 1 or n == 2:
    return 1
  else:
    return (fibonacci(n - 1) + (fibonacci(n - 2)))
'''
assert fibonacci(7) == 13
assert fibonacci(8) == 21
assert fibonacci(9) == 34
