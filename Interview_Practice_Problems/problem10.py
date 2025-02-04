def even_substrings(superstring):
    '''
    returns the number of even-numbered substrings that can be formed

    if a substring occurs more than once, count each occurrence as a separate
    substring

    input: string of digits
    output: count of even substrings

    inplicit: input string will always have a number, digits is a string of int
    explicit: if a substring occurs more than once, count each occurrence as a separate
        substring

    data structures:
        - list to store substring

    algorithm:
        - create all possible substrings
            - substrings can be length 1 up to length parent string
            - loop through all possible lengths
            - create all slices of a particular length and add that to the
              substring list
                - use the length to determine size of slice (end index) -> use
                  helper
                - helper will take the input string and slice length and return
                  all possible combos of that slice length
        - convert each possible substring into a int
        - divide int by 2 to determine if even
        - if even, add to the even count
    '''

    all_substrings = []

    for possible_lengths in range(1, len(superstring) + 1):
        all_substrings.extend(get_slice_of_length(possible_lengths, superstring))
    
    return len([int(substring) for substring in all_substrings if int(substring) % 2 == 0])

def get_slice_of_length(slice_length, superstring):
    '''
    create start index, create end index, add all slices to a list, return list
    '''

    possible_slices = []

    start_index = 0
    end_index = start_index + slice_length

    while end_index <= len(superstring):
        possible_slices.append(superstring[start_index: end_index])
        start_index += 1
        end_index += 1

    return possible_slices

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

# first attempt (2/3/2025) final time; 15 minutes 50 secs
# testing good