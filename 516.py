'''Write a function to sort a list of elements using radix sort.
'''
def radix_sort(nums):
    RADIX = 10
    placement = 1
    max_digit = max(nums)

    while placement < max_digit:
      buckets = [list() for _ in range( RADIX )]
      for i in nums:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        for i in buck:
          nums[a] = i
          a += 1
      placement *= RADIX
    return nums
'''
Standard answer: 
def radix_sort(nums):
    RADIX = 10
    placement = 1
    max_digit = max(nums)

    while placement < max_digit:
      buckets = [list() for _ in range( RADIX )]
      for i in nums:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        for i in buck:
          nums[a] = i
          a += 1
      placement *= RADIX
    return nums
'''
assert radix_sort([15, 79, 25, 68, 37]) == [15, 25, 37, 68, 79]
assert radix_sort([9, 11, 8, 7, 3, 2]) == [2, 3, 7, 8, 9, 11]
assert radix_sort([36, 12, 24, 26, 29]) == [12, 24, 26, 29, 36]
