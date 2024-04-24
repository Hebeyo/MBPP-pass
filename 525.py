'''Write a python function to check whether two given lines are parallel or not.
'''
def parallel_lines(line1, line2):
    if line1[0]/line1[1] == line2[0]/line2[1]:
        return True
    else:
        return False
'''
Standard answer: 
def parallel_lines(line1, line2):
  return line1[0]/line1[1] == line2[0]/line2[1]
'''
assert parallel_lines([2,3,4], [2,3,8]) == True
assert parallel_lines([2,3,4], [4,-3,8]) == False
assert parallel_lines([3,3],[5,5]) == True
