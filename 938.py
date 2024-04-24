'''Write a function to find three closest elements from three sorted arrays.
'''
def find_closet(A, B, C, p, q, r): 
    diff = 1000000000
    res_i = 0
    res_j = 0
    res_k = 0
    i = 0
    j = 0
    k = 0
    while(i < p and j < q and k < r): 
        minimum = min(A[i], min(B[j], C[k])) 
        maximum = max(A[i], max(B[j], C[k])); 
        if maximum-minimum < diff: 
            res_i = i 
            res_j = j 
            res_k = k 
            diff = maximum - minimum; 
        if diff == 0: 
            break
        if A[i] == minimum: 
            i = i+1
        elif B[j] == minimum: 
            j = j+1
        else: 
            k = k+1
    return A[res_i],B[res_j],C[res_k]
'''
Standard answer: 
import sys 

def find_closet(A, B, C, p, q, r): 
	diff = sys.maxsize 
	res_i = 0
	res_j = 0
	res_k = 0
	i = 0
	j = 0
	k = 0
	while(i < p and j < q and k < r): 
		minimum = min(A[i], min(B[j], C[k])) 
		maximum = max(A[i], max(B[j], C[k])); 
		if maximum-minimum < diff: 
			res_i = i 
			res_j = j 
			res_k = k 
			diff = maximum - minimum; 
		if diff == 0: 
			break
		if A[i] == minimum: 
			i = i+1
		elif B[j] == minimum: 
			j = j+1
		else: 
			k = k+1
	return A[res_i],B[res_j],C[res_k]
'''
assert find_closet([1, 4, 10],[2, 15, 20],[10, 12],3,3,2) == (10, 15, 10)
assert find_closet([20, 24, 100],[2, 19, 22, 79, 800],[10, 12, 23, 24, 119],3,5,5) == (24, 22, 23)
assert find_closet([2, 5, 11],[3, 16, 21],[11, 13],3,3,2) == (11, 16, 11)
