def even_substrings(digits):
    '''
    takes a string of digits as an arg

    returns the number of even-numbered substrings that can be formed

    input: string of digits
    output: number of even numbers

    data structure:
        - list of all possible substrings

    algorithm:
        - initialize the count of even numbers
        - create all possible substrings
            - create all possible substrings of length 1, 2, ... len(digits)

        - convert all substrings to ints
        - loop through all possible substrings and determine if they are even
            - if they are, increase the count of substrings
        - return count

        
    '''

    even_count = 0

    all_possible = all_substrings(digits)

    int_possible = [sub for sub in all_possible if int(sub) % 2 == 0]

    return len(int_possible)



def all_substrings(digits):
    # helper function:
    #             - initialize list of all possible substrings (empty)
    #             - create all possible substrings of length 1, 2, ... len(digits)
    #             - for each length, grab all slices of that length from digits
    #             - add each slice to the list of all possible substrings
    #             - use a while loop bc number of slices of that length in digits is unknown
    #             - exit condition is if the ending index of the slice is greater than the length of digits
    #             - return list of all possible substrings

    all_possible = []

    for length in range(1, len(digits) + 1):
        start_index = 0
        end_index = start_index + length
        while end_index <= len(digits):
            a_slice = digits[start_index: end_index]
            all_possible.append(a_slice)
            start_index += 1
            end_index += 1

    return all_possible

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

# Second attempt (2/5/2025) final time: 14 mins 52 secs