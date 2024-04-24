'''Write a function to filter a dictionary based on values.
'''
def dict_filter(dict,n):
  result = {}
  for key, value in dict.items():
    if value >= n:
      result[key] = value
  return result
'''
Standard answer: 
def dict_filter(dict,n):
 result = {key:value for (key, value) in dict.items() if value >=n}
 return result
'''
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},170)=={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},180)=={ 'Alden Cantrell': 180, 'Pierre Cox': 190}
assert dict_filter({'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190},190)=={ 'Pierre Cox': 190}
