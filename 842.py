'''Write a function to find the number which occurs for odd number of times in the given array.
'''
def get_odd_occurence(arr, arr_size):
  for i in range(0, arr_size):
    count = 0
    for j in range(0, arr_size):
      if arr[i] == arr[j]:
        count += 1
    if (count % 2 != 0):
      return arr[i]
  return -1
'''
Standard answer: 
def get_odd_occurence(arr, arr_size):
  for i in range(0, arr_size):
    count = 0
    for j in range(0, arr_size):
      if arr[i] == arr[j]:
        count += 1
    if (count % 2 != 0):
      return arr[i]
  return -1
'''
assert get_odd_occurence([2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2], 13) == 5
assert get_odd_occurence([1, 2, 3, 2, 3, 1, 3], 7) == 3
assert get_odd_occurence([5, 7, 2, 7, 5, 2, 5], 7) == 5
