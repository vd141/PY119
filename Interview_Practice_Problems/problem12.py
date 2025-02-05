def is_pangram(sentence):
    '''
    returns True if the string is a pangram, False if it is not

    pangrams are sentences that contain every letter of the alphabet at least once

    case is irrelevant

    ignore non alphabetic characters

    data structure:
        - set to store alphabet
        - set to store all unique characters in the alphabet

    algorithm:
        - convert sentence into a set of characters
        - convert alphabet string into a set
        - find the intersection of the two. if the intersection of the two
          is equal to the alphabet set, return True. otherwise, return false
    '''

    unique_chars = set(sentence)
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')

    return True if unique_chars.intersection(alphabet_set) == alphabet_set else False

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

# first attempt (2/4/2025) final time: 6 mins, 13 secs