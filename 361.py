'''Write a function to remove empty lists from a given list of lists.
'''
def remove_empty(list1):
  remove_empty = [x for x in list1 if x]
  return remove_empty
'''
Standard answer: 
def remove_empty(list1):
  remove_empty = [x for x in list1 if x]
  return remove_empty
'''
assert remove_empty([[], [], [], 'Red', 'Green', [1,2], 'Blue', [], []])==['Red', 'Green', [1, 2], 'Blue']
assert remove_empty([[], [], [],[],[], 'Green', [1,2], 'Blue', [], []])==[ 'Green', [1, 2], 'Blue']
assert remove_empty([[], [], [], 'Python',[],[], 'programming', 'language',[],[],[], [], []])==['Python', 'programming', 'language']
