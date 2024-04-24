'''Write a function to search an element in the given array by using binary search.
'''
def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return False
'''
Standard answer: 
def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
'''
assert binary_search([1,2,3,5,8], 6) == False
assert binary_search([7, 8, 9, 10, 13], 10) == True
assert binary_search([11, 13, 14, 19, 22, 36], 23) == False
