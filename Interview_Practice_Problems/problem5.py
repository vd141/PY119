def most_common_char(sentence):
    '''
    take a string argument and returns the character that occurs most often in
    the string. if there are multiple characters with teh same greatest frequency,
    return the one that appears first in teh string. when counting characters, 
    consider uppercase and lowercase versions to be the same

    input: sentence of chars
    output: most frequently occuring char (lowercase)

    data structure:
        - none

    algorithm:
        - convert all letters in string to lowercase (case does not matter)
        - loop through each character in the string
        - count the number of times that character appears in the string
        - if the count is greater than the current count, designate that character
          as the max count character
        - return max count character
    '''

    max_count_char = ''
    max_count = 0
    lowercase_sentence = sentence.lower()

    for char in lowercase_sentence:
        char_count = lowercase_sentence.count(char)
        if char_count > max_count:
            max_count_char = char
            max_count = char_count

    return max_count_char


print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

# First pass (2/3/2025) final time: 10 mins, 0 secs