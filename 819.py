'''Write a function to count the frequency of consecutive duplicate elements in a given list of numbers.
'''
def count_duplic(lists):
    if not lists:
        return [],[]
    element = [lists[0]]
    frequency = [1]
    for i in range(1,len(lists)):
        if lists[i] == lists[i-1]:
            frequency[-1] += 1
        else:
            element.append(lists[i])
            frequency.append(1)
    return element,frequency
'''
Standard answer: 
def count_duplic(lists):
    element = []
    frequency = []
    if not lists:
        return element
    running_count = 1
    for i in range(len(lists)-1):
        if lists[i] == lists[i+1]:
            running_count += 1
        else:
            frequency.append(running_count)
            element.append(lists[i])
            running_count = 1
    frequency.append(running_count)
    element.append(lists[i+1])
    return element,frequency

'''
assert count_duplic([1,2,2,2,4,4,4,5,5,5,5])==([1, 2, 4, 5], [1, 3, 3, 4])
assert count_duplic([2,2,3,1,2,6,7,9])==([2, 3, 1, 2, 6, 7, 9], [2, 1, 1, 1, 1, 1, 1])
assert count_duplic([2,1,5,6,8,3,4,9,10,11,8,12])==([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
