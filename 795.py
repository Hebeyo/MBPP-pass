'''Write a function to find the n - cheap price items from a given dataset using heap queue algorithm.
'''
def cheap_items(items,n):
  res = []
  for i in range(n):
    min = 100000
    for j in range(len(items)):
      if items[j]['price'] < min:
        min = items[j]['price']
        index = j
    res.append(items[index])
    items.pop(index)
  return res
'''
Standard answer: 
import heapq
def cheap_items(items,n):
  cheap_items = heapq.nsmallest(n, items, key=lambda s: s['price'])
  return cheap_items
'''
assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],1)==[{'name': 'Item-1', 'price': 101.1}]
assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}],2)==[{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}]
assert cheap_items([{'name': 'Item-1', 'price': 101.1},{'name': 'Item-2', 'price': 555.22}, {'name': 'Item-3', 'price': 45.09},{'name': 'Item-4', 'price': 22.75}],1)==[{'name': 'Item-4', 'price': 22.75}]
