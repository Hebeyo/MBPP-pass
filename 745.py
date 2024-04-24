'''Write a function to find numbers within a given range where every number is divisible by every digit it contains.
'''
def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum,endnum+1):
        str_i = str(i)
        for j in str_i:
            if j == '0' or i % int(j) != 0:
                break
        else:
            result.append(i)
    return result
'''
Standard answer: 
def divisible_by_digits(startnum, endnum):
    return [n for n in range(startnum, endnum+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
'''
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
assert divisible_by_digits(20,25)==[22, 24]
