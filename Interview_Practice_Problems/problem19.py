def odd_fellow(integers):
    '''
    returns the integer in the list that appears an odd number of times

    there will always be exactly one such integer in the input list
    
    integers list will always have at least one element

    data structure:
        none

    algorithm:
        - get all unique numbers (to cut down on number of iterations)
            - get a set of integers, turn that into a list (iterable)
        - loop through all unique numbers
        - count the number of occurrences in the input list
        - if the number of occurrences is odd, return that number
    '''

    unique_numbers = list(set(integers))

    for num in unique_numbers:
        if integers.count(num) % 2 != 0:
            return num
        
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

# first attempt (2/4/2025) final time: 5 mins??