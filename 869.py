'''Write a function to remove sublists from a given list of lists, which are outside a given range.
'''
def remove_list_range(list1, leftrange, rigthrange):
   result = []
   for i in list1:
      if min(i)>=leftrange and max(i)<=rigthrange:
         result.append(i)
   return result
'''
Standard answer: 
def remove_list_range(list1, leftrange, rigthrange):
   result = [i for i in list1 if (min(i)>=leftrange and max(i)<=rigthrange)]
   return result
'''
assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],13,17)==[[13, 14, 15, 17]]
assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],1,3)==[[2], [1, 2, 3]]
assert remove_list_range([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]],0,7)==[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7]]
