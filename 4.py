'''Write a function to find the largest integers from a given list of numbers using heap queue algorithm.
'''
def heap_queue_largest(nums,n):
  largest_nums = []
  for i in range(n):
    largest_nums.append(max(nums))
    nums.remove(max(nums))
  return largest_nums
'''
Standard answer: 
import heapq as hq
def heap_queue_largest(nums,n):
  largest_nums = hq.nlargest(n, nums)
  return largest_nums
'''
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],3)==[85, 75, 65] 
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],2)==[85, 75] 
assert heap_queue_largest( [25, 35, 22, 85, 14, 65, 75, 22, 58],5)==[85, 75, 65, 58, 35]
