'''Write a function to sort the given array by using counting sort.
'''
def counting_sort(my_list):
    max_value = 0
    for i in range(len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]
    buckets = [0] * (max_value + 1)
    for i in my_list:
        buckets[i] += 1
    i = 0
    for j in range(max_value + 1):
         for a in range(buckets[j]):
             my_list[i] = j
             i += 1
    return my_list
'''
Standard answer: 
def counting_sort(my_list):
    max_value = 0
    for i in range(len(my_list)):
        if my_list[i] > max_value:
            max_value = my_list[i]
    buckets = [0] * (max_value + 1)
    for i in my_list:
        buckets[i] += 1
    i = 0
    for j in range(max_value + 1):
         for a in range(buckets[j]):
             my_list[i] = j
             i += 1
    return my_list
'''
assert counting_sort([1,23,4,5,6,7,8]) == [1, 4, 5, 6, 7, 8, 23]
assert counting_sort([12, 9, 28, 33, 69, 45]) == [9, 12, 28, 33, 45, 69]
assert counting_sort([8, 4, 14, 3, 2, 1]) == [1, 2, 3, 4, 8, 14]
