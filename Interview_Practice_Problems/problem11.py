def repeated_substring(word):
    '''
    returns a tuple consisting of a string (s) and an integer (k).

    word = s * k such that k is maximized (s is minimized)

    string argument consists entirely of lowercase alphabetic letters

    input: word with repeated substrings
    output: tuple of repeated substring and number of times repeated

    data structure: 
        - output tuple

    algorithm:
        - test each substring that can be made from the input word, starting 
          with the smallest one
          - starting from length of 1 to length of the entire word
        - substrings are created from left to right
            - if the length of the word can be divided by the length of the substring,
              then the substring can be tested
            - return the substring and length immediately when the input word can
              be built from it
    '''

    for sub_len in range(1, len(word) + 1):
        sub = word[0: sub_len]
        factor = len(word) / len(sub)
        is_factor = len(word) % len(sub) == 0
        if is_factor:
            if int(factor) * sub == word:
                return (sub, factor)


print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

# first attempt (2/3/2025) final time: 12min 17 secs
# testing good, but be sure to explain the thought process when correcting