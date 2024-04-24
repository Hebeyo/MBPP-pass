'''Write a function to remove lowercase substrings from a given string by using regex.
'''
import re
def remove_lowercase(str1):
  remove_lower = lambda text: re.sub('[a-z]', '', text)
  result =  remove_lower(str1)
  return (result)
'''
Standard answer: 
import re
def remove_lowercase(str1):
  remove_lower = lambda text: re.sub('[a-z]', '', text)
  result =  remove_lower(str1)
  return (result)
'''
assert remove_lowercase('KDeoALOklOOHserfLoAJSIskdsf') == 'KDALOOOHLAJSI'
assert remove_lowercase('ProducTnamEstreAmIngMediAplAYer') == 'PTEAIMAAY'
assert remove_lowercase('maNufacTuredbYSheZenTechNolOGIes') == 'NTYSZTNOGI'
