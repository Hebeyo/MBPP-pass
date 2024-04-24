'''Write a function to check whether the entered number is greater than the elements of the given array.
'''
def check_greater(arr, number):
  for i in arr:
    if number < i:
      return 'No, entered number is less than those in the array'
  return 'Yes, the entered number is greater than those in the array'
'''
Standard answer: 
def check_greater(arr, number):
  arr.sort()
  if number > arr[-1]:
    return ('Yes, the entered number is greater than those in the array')
  else:
    return ('No, entered number is less than those in the array')
'''
assert check_greater([1, 2, 3, 4, 5], 4) == 'No, entered number is less than those in the array'
assert check_greater([2, 3, 4, 5, 6], 8) == 'Yes, the entered number is greater than those in the array'
assert check_greater([9, 7, 4, 8, 6, 1], 11) == 'Yes, the entered number is greater than those in the array'
