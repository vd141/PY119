def equal_sum_index(integers):
    '''
    return the index N for which all numbers with an index less than N sum to
    the same value as the numbers with an index greater than N. IF there is no
    index that would make this happen, return -1

    if given a list with multiple answers, return the index with the smallest
    value

    sum of integers to left of index 0 is 0. sum of integers to right of last
    element is 0

    data structures:
        - sum of left slice
        - sum of right slice

    algorithms:
        - current sum to left of first index is 0
        - current sum to the right of first index is sum of all but first element
        - index is 0
        - compare sums
        - if the sums are the same, return the index
        - if the sums are not the same, increment the middle index
        - return -1 as a catch all (if the sums are never equal)
    '''

    middle_index = 0
    left_sum = 0
    right_sum = sum(integers[middle_index + 1:])

    while middle_index < len(integers):
        if left_sum == right_sum:
            return middle_index
        middle_index += 1
        left_sum = sum(integers[:middle_index])
        right_sum = sum(integers[middle_index + 1:])

    return -1
        
print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

# first pass (2/4/2025) final time: 11 mins 54 secs