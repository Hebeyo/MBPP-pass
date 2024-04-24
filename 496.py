'''Write a function to find the smallest integers from a given list of numbers using heap queue algorithm.
'''
def heap_queue_smallest(nums,n):
  import heapq as hq
  hq.heapify(nums)
  smallest_nums = [hq.heappop(nums) for _ in range(n)]
  return smallest_nums
'''
Standard answer: 
import heapq as hq
def heap_queue_smallest(nums,n):
  smallest_nums = hq.nsmallest(n, nums)
  return smallest_nums
'''
assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 25, 58],3)==[14, 22, 25] 
assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 25, 58],2)==[14, 22]
assert heap_queue_smallest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[14, 22, 22, 25, 35]
