'''Write a python function to convert octal number to decimal number.
'''
def octal_To_Decimal(n):  
    num = n; 
    dec_value = 0; 
    base = 1; 
    temp = num; 
    while (temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
        dec_value += last_digit*base; 
        base = base * 8; 
    return dec_value;
'''
Standard answer: 
def octal_To_Decimal(n):  
    num = n; 
    dec_value = 0; 
    base = 1; 
    temp = num; 
    while (temp): 
        last_digit = temp % 10; 
        temp = int(temp / 10); 
        dec_value += last_digit*base; 
        base = base * 8; 
    return dec_value; 
'''
assert octal_To_Decimal(25) == 21
assert octal_To_Decimal(30) == 24
assert octal_To_Decimal(40) == 32
