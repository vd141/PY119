def smaller_numbers_than_current(numbers):
    '''
    takes a list of numbers as an argument

    for each number determine how many numbers in the list are smaller than it,
    and place the answer in a list. return the resulting list

    only count unique values that are lower

    implicit: input list always has at least 1 element, elements are integers,
    explicit: only count unique values that are lower

    inputs: list of numbers
    outputs: list of numbers smaller than each number in input list

    data structures: 
        - list comprehension of numbers smaller than current number
        - set of that list (for unique values)

    algorithm:
        - create a parent list to store results of counts
        - loop through each value of the input list
        - for each value, find all numbers in original list less than that number
        - of those numbers, only count the unique ones
        - store unique count in the parent list
    '''

    parent_list = []

    for element in numbers:
        less_than = [lesser for lesser in numbers if lesser < element]
        less_than = set(less_than)
        parent_list.append(len(less_than))

    return parent_list

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

# Attempt 1 (2/2/2025) final time: 9 min 13 secs
    # could use some intermediate testing before running final solution