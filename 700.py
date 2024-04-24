'''Write a function to count the number of elements in a list which are within a specific range.
'''
def count_range_in_list(li, min, max):
	ctr = 0
	for x in li:
		if min <= x <= max:
			ctr += 1
	return ctr
'''
Standard answer: 
def count_range_in_list(li, min, max):
	ctr = 0
	for x in li:
		if min <= x <= max:
			ctr += 1
	return ctr
'''
assert count_range_in_list([10,20,30,40,40,40,70,80,99],40,100)==6
assert count_range_in_list(['a','b','c','d','e','f'],'a','e')==5
assert count_range_in_list([7,8,9,15,17,19,45],15,20)==3
