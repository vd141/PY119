def repeated_substring(word):
    '''
    takes a nonempty string (s)

    returns a tuple consisting of a string (t) and an integer (k)

    s == t * k

    t should be the shortest possible substring
    k should be the largest possible number

    string argument consists entirely of lowercase alphabetic letters

    input is a set of repeating characters. what is the shortest set of repeating
    characters

    data structure:
        - output tuple
        - candidate short string

    algorithm:
        - find the shortest repeatable string
        - test substrings starting from length 1 (the first letter) up until the
          full length of the word
        - if the input length is divisible by the substring length, then we can
          test that substring
            - divide input length by substring length (this is the factor)
            - multiply the substring by the factor to see if it equates the input
            - if it does, return the substring and factor
        - increase the substring length by 1
    '''

    for length in range(1, len(word) + 1):
        if len(word) % length == 0:
            substring = word[:length]
            factor = len(word) / length
            if substring * int(factor) == word:
                return (substring, factor)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

# second pass (2/5/2025) final tie: 13 mins 12 secs