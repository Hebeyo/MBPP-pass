'''Write a function to remove specific words from a given list.
'''
def remove_words(list1, removewords):
    for word in list(list1):
        if word in removewords:
            list1.remove(word)
    return list1
'''
Standard answer: 
def remove_words(list1, removewords):
    for word in list(list1):
        if word in removewords:
            list1.remove(word)
    return list1  
'''
assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'],['white', 'orange'])==['red', 'green', 'blue', 'black']
assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'],['black', 'orange'])==['red', 'green', 'blue', 'white']
assert remove_words(['red', 'green', 'blue', 'white', 'black', 'orange'],['blue', 'white'])==['red', 'green', 'black', 'orange']
