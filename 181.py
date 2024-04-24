'''Write a function to find the longest common prefix in the given set of strings.
'''
def common_prefix(arr, n):
  prefix = arr[0]
  for i in range(1, n):
    j = 0
    while j < len(prefix) and j < len(arr[i]) and prefix[j] == arr[i][j]:
      j += 1
    prefix = prefix[:j]
  return prefix
'''
Standard answer: 
def common_prefix_util(str1, str2): 
	result = ""; 
	n1 = len(str1) 
	n2 = len(str2) 
	i = 0
	j = 0
	while i <= n1 - 1 and j <= n2 - 1: 
		if (str1[i] != str2[j]): 
			break
		result += str1[i] 
		i += 1
		j += 1
	return (result) 
def common_prefix (arr, n): 
	prefix = arr[0] 
	for i in range (1, n): 
		prefix = common_prefix_util(prefix, arr[i]) 
	return (prefix) 
'''
assert common_prefix(["tablets", "tables", "taxi", "tamarind"], 4) == 'ta'
assert common_prefix(["apples", "ape", "april"], 3) == 'ap'
assert common_prefix(["teens", "teenager", "teenmar"], 3) == 'teen'
