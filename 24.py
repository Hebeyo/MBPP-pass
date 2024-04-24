'''Write a function to convert the given binary number to its decimal equivalent.
'''
def binary_to_decimal(binary):
    decimal = 0
    i = 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)
'''
Standard answer: 
def binary_to_decimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return (decimal)
'''
assert binary_to_decimal(100) == 4
assert binary_to_decimal(1011) == 11
assert binary_to_decimal(1101101) == 109
