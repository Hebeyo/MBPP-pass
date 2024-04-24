'''Write a function to substaract two lists using map and lambda function.
'''
def sub_list(nums1,nums2):
  result = list(map(lambda x, y: x - y, nums1, nums2))
  return (result)
'''
Standard answer: 
def sub_list(nums1,nums2):
  result = map(lambda x, y: x - y, nums1, nums2)
  return list(result)
'''
assert sub_list([1, 2, 3],[4,5,6])==[-3,-3,-3]
assert sub_list([1,2],[3,4])==[-2,-2]
assert sub_list([90,120],[50,70])==[40,50]
