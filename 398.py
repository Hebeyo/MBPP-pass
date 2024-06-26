'''Write a function to compute the sum of digits of each number of a given list.
'''
def sum_of_digits(nums):
    result = 0
    for n in nums:
        if isinstance(n, int):
            result += sum(int(el) for el in str(n) if el.isdigit())
        elif isinstance(n, list):
            result += sum_of_digits(n)
    return result
'''
Standard answer: 
def sum_of_digits(nums):
    return sum(int(el) for n in nums for el in str(n) if el.isdigit())
'''
assert sum_of_digits([10,2,56])==14
assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
assert sum_of_digits([10,20,-4,5,-70])==19
