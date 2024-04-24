'''Write a function to remove words from a given list of strings containing a character or string.
'''
def remove_words(list1, charlist):
    new_list = []
    for line in list1:
        new_words = ' '.join([word for word in line.split() if not any([phrase in word for phrase in charlist])])
        new_list.append(new_words)
    return new_list
'''
Standard answer: 
def remove_words(list1, charlist):
    new_list = []
    for line in list1:
        new_words = ' '.join([word for word in line.split() if not any([phrase in word for phrase in charlist])])
        new_list.append(new_words)
    return new_list
'''
assert remove_words(['Red color', 'Orange#', 'Green', 'Orange @', "White"],['#', 'color', '@'])==['Red', '', 'Green', 'Orange', 'White']
assert remove_words(['Red &', 'Orange+', 'Green', 'Orange @', 'White'],['&', '+', '@'])==['Red', '', 'Green', 'Orange', 'White']
assert remove_words(['Red &', 'Orange+', 'Green', 'Orange @', 'White'],['@'])==['Red &', 'Orange+', 'Green', 'Orange', 'White']
