def closest_numbers(integers):
    '''
    returns a tuple of two numbers that are closest together in value.
    if there are multiple pairs that are equally close, return the pair
    that occurs first in the list

    input: list of integers
    output: tuple of closest pair

    implicit: 
        - numbers can be positive
        - numbers in the tuple are in the order they appear
        - list will always have at least two integers
        - there are no duplicate values in the list

    explicit: 
        - return the pair that occurs first in the list

    data structure: 
        - none at the moment
    
    algorithm:
        - loop through all values
        - compare each value to the rest of the values, finding the difference between each one.
        - if a difference is lower than the current difference, those two numbers will be in the tuple
        - append the two pairs to a list
        - convert the list to a tuple and return it
    '''

    pair = [None, None]
    min_diff = float('inf')

    for idx, elem in enumerate(integers):
        for idx_remaining, elem_remaining in enumerate(integers[idx + 1:]):
            if abs(elem - elem_remaining) < min_diff:
                min_diff = abs(elem - elem_remaining)
                pair[0], pair[1] = elem, elem_remaining
    return tuple(pair)

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

# First attempt (2/3/2025) final time: 17 mins 30 secs