'''Write a function to compute maximum product of three numbers of a given array of integers using heap queue algorithm.
'''
def maximum_product(nums):
  import heapq
  a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
  return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])
'''
Standard answer: 
def maximum_product(nums):
    import heapq
    a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
    return max(a[0] * a[1] * a[2], a[0] * b[0] * b[1])
'''
assert maximum_product( [12, 74, 9, 50, 61, 41])==225700
assert maximum_product([25, 35, 22, 85, 14, 65, 75, 25, 58])==414375
assert maximum_product([18, 14, 10, 9, 8, 7, 9, 3, 2, 4, 1])==2520
