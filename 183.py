'''Write a function to count all the distinct pairs having a difference of k in any array.
'''
def count_pairs(arr, n, k):
  count = 0
  for i in range(n):
    for j in range(i+1, n):
      if arr[i] - arr[j] == k or arr[j] - arr[i] == k:
        count += 1
  return count
'''
Standard answer: 
def count_pairs(arr, n, k):
  count=0;
  for i in range(0,n):
    for j in range(i+1, n):
      if arr[i] - arr[j] == k or arr[j] - arr[i] == k:
        count += 1
  return count
'''
assert count_pairs([1, 5, 3, 4, 2], 5, 3) == 2
assert count_pairs([8, 12, 16, 4, 0, 20], 6, 4) == 5
assert count_pairs([2, 4, 1, 3, 4], 5, 2) == 3
