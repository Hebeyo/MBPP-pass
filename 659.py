'''Write a python function to print duplicants from a list of integers.
'''
def Repeat(x):
    size = len(x)
    repeated = []
    for i in range(size):
        for j in range(i+1, size):
            if x[i] == x[j] and x[i] not in repeated:
                repeated.append(x[i])
    return repeated
'''
Standard answer: 
def Repeat(x): 
    _size = len(x) 
    repeated = [] 
    for i in range(_size): 
        k = i + 1
        for j in range(k, _size): 
            if x[i] == x[j] and x[i] not in repeated: 
                repeated.append(x[i]) 
    return repeated 
'''
assert Repeat([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]) == [20, 30, -20, 60]
assert Repeat([-1, 1, -1, 8]) == [-1]
assert Repeat([1, 2, 3, 1, 2,]) == [1, 2]
