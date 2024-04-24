'''Write a function to calculate the sum of all digits of the base to the specified power.
'''
def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])
'''
Standard answer: 
def power_base_sum(base, power):
    return sum([int(i) for i in str(pow(base, power))])
'''
assert power_base_sum(2,100)==115
assert power_base_sum(8,10)==37
assert power_base_sum(8,15)==62
