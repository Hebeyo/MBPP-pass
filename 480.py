'''Write a python function to find the maximum occurring character in a given string.
'''
def get_max_occuring_char(str1):
    max = -1
    ch = ''
    for i in str1:
        count = str1.count(i)
        if count > max:
            max = count
            ch = i
    return ch
'''
Standard answer: 
def get_max_occuring_char(str1):
  ASCII_SIZE = 256
  ctr = [0] * ASCII_SIZE
  max = -1
  ch = ''
  for i in str1:
    ctr[ord(i)]+=1;
  for i in str1:
    if max < ctr[ord(i)]:
      max = ctr[ord(i)]
      ch = i
  return ch
'''
assert get_max_occuring_char("data") == "a"
assert get_max_occuring_char("create") == "e"
assert get_max_occuring_char("brilliant girl") == "i"
