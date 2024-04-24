'''Write a function to add two numbers and print number of digits of sum.
'''
def count_digits(num1,num2):
    number=num1+num2
    count = 0
    while(number > 0):
        number = number // 10
        count = count + 1
    return count
'''
Standard answer: 
def count_digits(num1,num2):
    number=num1+num2
    count = 0
    while(number > 0):
        number = number // 10
        count = count + 1
    return count
'''
assert count_digits(9875,10)==(4)
assert count_digits(98759853034,100)==(11)
assert count_digits(1234567,500)==(7)
