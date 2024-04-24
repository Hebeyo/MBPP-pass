'''Write a function to sort the given array without using any sorting algorithm. the given array consists of only 0, 1, and 2.
'''
def sort_by_dnf(arr, n):
  count0 = 0
  count1 = 0
  count2 = 0
  for i in range(n):
    if arr[i] == 0:
      count0 += 1
    elif arr[i] == 1:
      count1 += 1
    else:
      count2 += 1
  for i in range(count0):
    arr[i] = 0
  for i in range(count0, count0 + count1):
    arr[i] = 1
  for i in range(count0 + count1, n):
    arr[i] = 2
  return arr
'''
Standard answer: 
def sort_by_dnf(arr, n):
  low=0
  mid=0
  high=n-1
  while mid <= high:
    if arr[mid] == 0:
      arr[low], arr[mid] = arr[mid], arr[low]
      low = low + 1
      mid = mid + 1
    elif arr[mid] == 1:
      mid = mid + 1
    else:
      arr[mid], arr[high] = arr[high], arr[mid]
      high = high - 1
  return arr
'''
assert sort_by_dnf([1,2,0,1,0,1,2,1,1], 9) == [0, 0, 1, 1, 1, 1, 1, 2, 2]
assert sort_by_dnf([1,0,0,1,2,1,2,2,1,0], 10) == [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
assert sort_by_dnf([2,2,1,0,0,0,1,1,2,1], 10) == [0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
