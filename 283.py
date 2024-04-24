'''Write a python function to check whether the frequency of each digit is less than or equal to the digit itself.
'''
def validate(n):
    for i in range(10):
        temp = n
        count = 0
        while (temp):
            if (temp % 10 == i):
                count+=1
            if (count > i):
                return False
            temp //= 10
    return True
'''
Standard answer: 
def validate(n): 
    for i in range(10): 
        temp = n;  
        count = 0; 
        while (temp): 
            if (temp % 10 == i): 
                count+=1;  
            if (count > i): 
                return False
            temp //= 10; 
    return True
'''
assert validate(1234) == True
assert validate(51241) == False
assert validate(321) == True
