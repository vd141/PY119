def distinct_multiples(string_):
    '''
    returns the count of distinct case-insensitive alphabetic characters and
    digits that occur more than once in the string

    input string contains only alphanumeric characters

    input: string
    output: count of characters that occur more than once

    data structures:
        - list of unique characters in string
        - casefold version of string

    algorithm:
        - convert string into casefold
        - get unique characters from list
        - loop through unique characters and count occurrence in casefold string
        - if count is greater than or equal to 2, increment counter
    '''

    distinct = 0
    casefold_str = string_.casefold()
    unique_chars = list(set(string_))

    for char in unique_chars:
        if casefold_str.count(char) >= 2:
            distinct += 1

    return distinct

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

# first pass (2/4/2025) final time: 5 mins?

