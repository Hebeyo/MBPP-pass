'''Write a python function to calculate the product of the unique numbers of a given list.
'''
def unique_product(list_data):
    unique_list = []
    for i in list_data:
        if i not in unique_list:
            unique_list.append(i)
    product = 1
    for i in unique_list:
        product *= i
    return product
'''
Standard answer: 
def unique_product(list_data):
    temp = list(set(list_data))
    p = 1
    for i in temp:
        p *= i
    return p
'''
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
assert unique_product([1, 2, 3, 1,]) == 6
assert unique_product([7, 8, 9, 0, 1, 1]) == 0
