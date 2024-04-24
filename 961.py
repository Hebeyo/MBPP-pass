'''Write a function to convert a roman numeral to an integer.
'''
def roman_to_int(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
    int_val = 0
    i=0
    while i < len(s):
        if i+1<len(s) and s[i:i+2] in rom_val:
            int_val += rom_val[s[i:i+2]]
            i+=2
        else:
            int_val += rom_val[s[i]]
            i+=1
    return int_val
'''
Standard answer: 
def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
'''
assert roman_to_int('MMMCMLXXXVI')==3986
assert roman_to_int('MMMM')==4000
assert roman_to_int('C')==100
