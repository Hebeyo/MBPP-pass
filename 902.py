'''Write a function to combine two dictionaries by adding values for common keys.
'''
def add_dict(d1,d2):
    for key in d2:
        if key in d1:
            d1[key] = d1[key] + d2[key]
        else:
            d1[key] = d2[key]
    return d1
'''
Standard answer: 
from collections import Counter
def add_dict(d1,d2):
   add_dict = Counter(d1) + Counter(d2)
   return add_dict
'''
assert add_dict({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})==({'b': 400, 'd': 400, 'a': 400, 'c': 300}) 
assert add_dict({'a': 500, 'b': 700, 'c':900},{'a': 500, 'b': 600, 'd':900})==({'b': 1300, 'd': 900, 'a': 1000, 'c': 900}) 
assert add_dict({'a':900,'b':900,'d':900},{'a':900,'b':900,'d':900})==({'b': 1800, 'd': 1800, 'a': 1800})
