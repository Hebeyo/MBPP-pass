'''Write a function to calculate the sum of series 1²+2²+3²+….+n².
'''
def series_sum(number):
    total = 0
    for i in range(1, number+1):
        total += i*i
    return total
'''
Standard answer: 
def series_sum(number):
 total = 0
 total = (number * (number + 1) * (2 * number + 1)) / 6
 return total
'''
assert series_sum(6)==91
assert series_sum(7)==140
assert series_sum(12)==650
