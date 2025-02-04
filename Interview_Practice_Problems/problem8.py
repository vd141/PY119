def longest_vowel_substring(string):
    '''
    input is nonempty string

    consists entirely of lowercase alphabetic characters

    returns length of the longest vowel substring

    vowels are 'aeiou'

    input: string of lowercase letters
    output: integer of the longest vowel substring

    data structure:
        - string representing vowels

    algorithm:
        - loop through each letter of input
        - if the letter is a vowel, increase vowel count
            - if the vowel count is greater than the max vowel count, update
              the max vowel count
        - if the letter is not a vowel, reset vowel count to zero
        - return the max vowel count
    '''

    max_vowel_count = 0
    vowel_count = 0

    vowels = 'aeiou'


    for char in string:
        if char not in vowels:
            vowel_count = 0
        else:
            vowel_count += 1
            if vowel_count >= max_vowel_count:
                max_vowel_count = vowel_count
    
    return max_vowel_count

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

# first aattempt (2/3/2025) final time: ??? (under 10 mins)
# could use some testing