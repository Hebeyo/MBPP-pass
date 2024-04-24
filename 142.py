'''Write a function to count the same pair in three given lists.
'''
def count_samepair(list1,list2,list3):
    result = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            result += 1
    return result
'''
Standard answer: 
def count_samepair(list1,list2,list3):
    result = sum(m == n == o for m, n, o in zip(list1,list2,list3))
    return result
'''
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==4
assert count_samepair([1,2,3,4,2,6,7,8],[2,2,3,1,2,6,7,8],[2,1,3,1,2,6,7,8])==5
