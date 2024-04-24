'''Write a function to get the word with most number of occurrences in the given strings list.
'''
def most_occurrences(test_list):
  wrd = {}
  for sub in test_list:
    for word in sub.split():
      if word not in wrd:
        wrd[word] = 1
      else:
        wrd[word] += 1
  max_occ = max(wrd, key=wrd.get)
  return max_occ
'''
Standard answer: 
from collections import defaultdict 

def most_occurrences(test_list):
  temp = defaultdict(int)
  for sub in test_list:
    for wrd in sub.split():
      temp[wrd] += 1
  res = max(temp, key=temp.get)
  return (str(res)) 
'''
assert most_occurrences(["UTS is best for RTF", "RTF love UTS", "UTS is best"] ) == 'UTS'
assert most_occurrences(["Its been a great year", "this year is so worse", "this year is okay"] ) == 'year'
assert most_occurrences(["Families can be reunited", "people can be reunited", "Tasks can be achieved "] ) == 'can'
