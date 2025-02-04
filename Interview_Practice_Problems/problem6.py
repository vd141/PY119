def count_letters(a_string):
    '''
    takes a string argument and returns a dict object in which the keys represent
    the lowercase letters in the string, and the values represent how often the
    corresponding letter occurs in the string

    input: string
    output: character count dict

    implicit:
        - keys are lowercase alphabetic characters only

    data strucutres:
        - output dict

    algorithm:
        - loop through each character in the string
        - check if it is alphabetic and lowercase
        - if it is, add the letter to the dict and increase the count to 1. if
           the letter already exists, increment the count by 1

    '''

    count_dict = {}

    for char in a_string:
        if char.isalpha() and char.lower() == char:
            count_dict[char] = count_dict.get(char, 0) + 1
    return count_dict




expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})

# first pass (2/3/2025) final time: 10 mins

