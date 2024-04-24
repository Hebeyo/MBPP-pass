'''Write a function to find the n - expensive price items from a given dataset using heap queue algorithm.
'''
def expensive_items(items,n):
  res = []
  for i in range(n):
    max = 0
    for j in range(len(items)):
      if items[j]['price'] > max:
        max = items[j]['price']
        index = j
    res.append(items[index])
    items.pop(index)
  return res
'''
Standard answer: 
import heapq
def expensive_items(items,n):
  expensive_items = heapq.nlargest(n, items, key=lambda s: s['price'])
  return expensive_items
'''
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-2', 'price': 555.22}]
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09}],2)==[{'name': 'Item-2', 'price': 555.22},{'name': 'Item-1', 'price': 101.1}]
assert expensive_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-2', 'price': 555.22}]
