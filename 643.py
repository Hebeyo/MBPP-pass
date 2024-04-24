'''Write a function that matches a word containing 'z', not at the start or end of the word.
'''
def text_match_wordz_middle(text):
    import re
    patterns = '\Bz\B'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')
'''
Standard answer: 
import re
def text_match_wordz_middle(text):
        patterns = '\Bz\B'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
assert text_match_wordz_middle("pythonzabc.")==('Found a match!')
assert text_match_wordz_middle("xyzabc.")==('Found a match!')
assert text_match_wordz_middle("  lang  .")==('Not matched!')
