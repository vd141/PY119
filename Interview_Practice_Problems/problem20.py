def what_is_different(numbers):
    '''
    all numbers in input are the same except one

    find and return the number in the list that differs from the rest

    data structure: list of unique numbers

    algorithm:
        - get unique numbers
        - loop through list of unique nubmers
        - if the count of the number is 1 in the original list, return that 
          number
    '''

    unique_numbers = list(set(numbers))

    for num in unique_numbers:
        if numbers.count(num) == 1:
            return num

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)

# first pass (2/4/2025) final time: 5 mins?