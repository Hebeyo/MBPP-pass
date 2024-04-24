'''Write a function to count occurrence of a character in a string.
'''
def count_char(string,char):
 count = 0
 for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
 return count
'''
Standard answer: 
def count_char(string,char):
 count = 0
 for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
 return count
'''
assert count_char("Python",'o')==1
assert count_char("little",'t')==2
assert count_char("assert",'s')==2
