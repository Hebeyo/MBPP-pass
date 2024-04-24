'''Write a function to move all the numbers in it to the given string.
'''
def move_num(test_str):
  res = ''
  dig = ''
  for ele in test_str:
    if ele.isdigit():
      dig += ele
    else:
      res += ele
  res += dig
  return (res)
'''
Standard answer: 
def move_num(test_str):
  res = ''
  dig = ''
  for ele in test_str:
    if ele.isdigit():
      dig += ele
    else:
      res += ele
  res += dig
  return (res) 
'''
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
assert move_num('Avengers124Assemble') == 'AvengersAssemble124'
assert move_num('Its11our12path13to14see15things16do17things') == 'Itsourpathtoseethingsdothings11121314151617'
