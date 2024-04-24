'''Write a python function to find the length of the shortest word.
'''
def len_log(list1):
    min=len(list1[0])
    for i in list1:
        if len(i)<min:
            min=len(i)
    return min
'''
Standard answer: 
def len_log(list1):
    min=len(list1[0])
    for i in list1:
        if len(i)<min:
            min=len(i)
    return min
'''
assert len_log(["win","lose","great"]) == 3
assert len_log(["a","ab","abc"]) == 1
assert len_log(["12","12","1234"]) == 2
