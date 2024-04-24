'''Write a function to convert an integer into a roman numeral.
'''
def int_to_roman(num):
    val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
    syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num
'''
Standard answer: 
def int_to_roman( num):
        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        syb = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num
'''
assert int_to_roman(1)==("I")
assert int_to_roman(50)==("L")
assert int_to_roman(4)==("IV")
