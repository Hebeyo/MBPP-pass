'''Write a function to find out the minimum no of swaps required for bracket balancing in the given string.
'''
def swap_count(s):
	chars = s
	count_left = 0
	count_right = 0
	swap = 0
	imbalance = 0; 
	for i in range(len(chars)):
		if chars[i] == '[':
			count_left += 1
			if imbalance > 0:
				swap += imbalance
				imbalance -= 1
		elif chars[i] == ']':
			count_right += 1
			imbalance = (count_right - count_left) 
	return swap
'''
Standard answer: 
def swap_count(s):
	chars = s
	count_left = 0
	count_right = 0
	swap = 0
	imbalance = 0; 
	for i in range(len(chars)):
		if chars[i] == '[':
			count_left += 1
			if imbalance > 0:
				swap += imbalance
				imbalance -= 1
		elif chars[i] == ']':
			count_right += 1
			imbalance = (count_right - count_left) 
	return swap
'''
assert swap_count("[]][][") == 2
assert swap_count("[[][]]") == 0
assert swap_count("[[][]]][") == 1
