'''Write a function to reverse strings in a given list of string values.
'''
def reverse_string_list(stringlist):
    result = []
    for string in stringlist:
        result.append(string[::-1])
    return result
'''
Standard answer: 
def reverse_string_list(stringlist):
    result = [x[::-1] for x in stringlist]
    return result
'''
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']
