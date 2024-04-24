'''Write a python function to check whether the length of the word is even or not.
'''
def word_len(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%2==0: 
            return True  
        else:
          return False
'''
Standard answer: 
def word_len(s): 
    s = s.split(' ')   
    for word in s:    
        if len(word)%2==0: 
            return True  
        else:
          return False
'''
assert word_len("program") == False
assert word_len("solution") == True
assert word_len("data") == True
