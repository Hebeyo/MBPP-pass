'''Write a function to extract specified size of strings from a give list of string values.
'''
def extract_string(str, l):
    res = []
    for e in str:
        if len(e) == l:
            res.append(e)
    return res
'''
Standard answer: 
def extract_string(str, l):
    result = [e for e in str if len(e) == l] 
    return result
'''
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']
