'''Write a python function to find the difference between highest and least frequencies in a given array.
'''
def find_Diff(arr,n):
  arr.sort()
  count = 0
  max_count = 0
  min_count = n
  for i in range(0, n - 1):
    if arr[i] == arr[i + 1]:
      count += 1
      continue
    else:
      max_count = max(max_count, count)
      min_count = min(min_count, count)
      count = 0
  return max_count - min_count
'''
Standard answer: 
def find_Diff(arr,n): 
    arr.sort()  
    count = 0; max_count = 0; min_count = n 
    for i in range(0,(n-1)): 
        if arr[i] == arr[i + 1]: 
            count += 1
            continue
        else: 
            max_count = max(max_count,count) 
            min_count = min(min_count,count) 
            count = 0
    return max_count - min_count 
'''
assert find_Diff([1,1,2,2,7,8,4,5,1,4],10) == 2
assert find_Diff([1,7,9,2,3,3,1,3,3],9) == 3
assert find_Diff([1,2,1,2],4) == 0
