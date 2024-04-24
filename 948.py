'''Write a function to get an item of a tuple.
'''
def get_item(tup1,index):
  item = tup1[index]
  return item
'''
Standard answer: 
def get_item(tup1,index):
  item = tup1[index]
  return item
'''
assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),3)==('e')
assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-4)==('u')
assert get_item(("w", 3, "r", "e", "s", "o", "u", "r", "c", "e"),-3)==('r')
