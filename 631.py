'''Write a function to replace whitespaces with an underscore and vice versa in a given string by using regex.
'''
def replace_spaces(text):
  text =text.replace (" ", "_")
  return (text)
  text =text.replace ("_", " ")
  return (text)
'''
Standard answer: 
import re
text = 'Python Exercises'
def replace_spaces(text):
  text =text.replace (" ", "_")
  return (text)
  text =text.replace ("_", " ")
  return (text)
'''
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces('The Avengers') == 'The_Avengers'
assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'
