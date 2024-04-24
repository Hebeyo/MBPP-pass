'''Write a function to find the difference of first even and odd number of a given list.
'''
def diff_even_odd(list1):
    even = False
    odd = False
    for i in list1:
        if i%2==0:
            even = i
            break
    for i in list1:
        if i%2!=0:
            odd = i
            break
    return even-odd
'''
Standard answer: 
def diff_even_odd(list1):
    first_even = next((el for el in list1 if el%2==0),-1)
    first_odd = next((el for el in list1 if el%2!=0),-1)
    return (first_even-first_odd)
'''
assert diff_even_odd([1,3,5,7,4,1,6,8])==3
assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
assert diff_even_odd([1,5,7,9,10])==9
