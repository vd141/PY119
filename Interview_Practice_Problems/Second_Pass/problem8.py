def longest_vowel_substring(word):
    '''
    takes a non empty string as an arg

    string consists entirely of lowercase alphabetic chars

    returns the length of the longest vowel substring

    vowels are 'aeiuo'

    data structure:
        - string to store values
        - integer to represent the max global vowel count
        - integer to represent local vowel count

    algorithm:
        - loop through each character of word
        - global max initialized to 0
        - if the letter is a vowel, increase the local vowel count by 1
            - if the local vowel count is greater than the global max, update global max
        - if the letter is a consonant, reset the local vowel count to 0
        - return global max after looping through all characters
    '''

    vowels = 'aeiou'

    global_max = 0
    local_max = 0

    for char in word:
        if char in vowels:
            local_max += 1
            if local_max > global_max:
                global_max = local_max
        else:
            local_max = 0

    return global_max
        
print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

# Second pass (2/5/2025) final time: 7 mins 30 secs