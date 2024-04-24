'''Write a function to extract the maximum numeric value from a string by using regex.
'''
def extract_max(input):
  import re
  numbers = re.findall('\d+',input)
  numbers = map(int,numbers)
  return max(numbers)
'''
Standard answer: 
import re 
def extract_max(input): 
	numbers = re.findall('\d+',input) 
	numbers = map(int,numbers) 
	return max(numbers)
'''
assert extract_max('100klh564abc365bg') == 564
assert extract_max('hello300how546mer231') == 546
assert extract_max('its233beenalong343journey234') == 343
