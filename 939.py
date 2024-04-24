'''Write a function to sort a list of dictionaries using lambda function.
'''
def sorted_models(models):
  sorted_models = sorted(models, key = lambda x: x['color'])
  return sorted_models
'''
Standard answer: 
def sorted_models(models):
 sorted_models = sorted(models, key = lambda x: x['color'])
 return sorted_models
'''
assert sorted_models([{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':2, 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}])==[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]
assert sorted_models([{'make':'Vivo', 'model':20,'color':'Blue'},{'make': 'oppo','model':17,'color':'Gold'},{'make':'Apple','model':11,'color':'red'}])==([{'make':'Vivo', 'model':20,'color':'Blue'},{'make': 'oppo','model':17,'color':'Gold'},{'make':'Apple','model':11,'color':'red'}])
assert sorted_models([{'make':'micromax','model':40,'color':'grey'},{'make':'poco','model':60,'color':'blue'}])==([{'make':'poco','model':60,'color':'blue'},{'make':'micromax','model':40,'color':'grey'}])
