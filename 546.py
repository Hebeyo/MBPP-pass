'''Write a function to find the last occurrence of a character in a string.
'''
def last_occurence_char(string,char):
 flag = -1
 for i in range(len(string)):
     if(string[i] == char):
         flag = i
 if(flag == -1):
    return None
 else:
    return flag + 1
'''
Standard answer: 
def last_occurence_char(string,char):
 flag = -1
 for i in range(len(string)):
     if(string[i] == char):
         flag = i
 if(flag == -1):
    return None
 else:
    return flag + 1
'''
assert last_occurence_char("hello world",'l')==10
assert last_occurence_char("language",'g')==7
assert last_occurence_char("little",'y')==None
