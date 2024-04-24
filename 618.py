'''Write a function to divide two lists using map and lambda function.
'''
def div_list(nums1,nums2):
  result = []
  for i in range(len(nums1)):
    result.append(nums1[i]/nums2[i])
  return result
'''
Standard answer: 
def div_list(nums1,nums2):
  result = map(lambda x, y: x / y, nums1, nums2)
  return list(result)
'''
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
assert div_list([3,2],[1,4])==[3.0, 0.5]
assert div_list([90,120],[50,70])==[1.8, 1.7142857142857142]
