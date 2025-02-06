def count_substrings(str1, str2):
    '''
    takes two string args and returns the number of times that the second string 
    occurs in the first string

    overlapping strings don't count

    the second argument is never empty

    input: 2 strings
    output: count of 2nd in 1st

    implicit: all letters are lowercase

    data structures:
        - sliding window indexes (integers)

    algorithm:
        - initialize str2 count to 0
        - build a sliding window of chars from str1 to compare to str1
            - get length of str2 (this is the length of the sliding window)
            - assign starting index of window
            - assign ending index of window
            - compare slice of the str1 to str2
                - if they are equal, 
                    - increase the counter by 1
                    - set the new window starting index to be the end of the current window
                    - set the new window ending index to be the length of the second arg + starting index
                - else:
                    - increase the start and end index by 1
        - break the loop when the ending index of the window is greater than the length of the first string
    '''

    count = 0
    start_index = 0
    end_index = start_index + len(str2)

    while end_index <= len(str1):
        slice = str1[start_index: end_index]
        if slice == str2:
            count += 1
            start_index, end_index = end_index, end_index + len(str2)
        else:
            start_index += 1
            end_index += 1
    
    return count

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

# Second pass (2/5/2024) final time: 10 mins 58 secs