def unscramble(word1, word2):
    '''
    takes two strings as arguments, returns True if some portion of chars
    in the first string can be rearrange to match chars in the second.

    Otherwise, function should return false

    both string arguments should contain lowercase alphabetic chars. neither string will be empty

    data structure:

    algorithm:
        - the count of each letter in the first string should match the count
          of each letter in the second string
        - loop through each letter of the second string
        - if the count of every letter in the second string is greater than
          the count of that letter in the first string, return True
        - otherwise, return false
    '''

    for letter in word2:
        if word2.count(letter) > word1.count(letter):
            return False
    
    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)

# first pass (2/4/2025) final time: 5 mins, 14 secs