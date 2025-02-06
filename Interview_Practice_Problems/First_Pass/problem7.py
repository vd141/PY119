def pairs(integers):
    '''
    takes a list of integers as an argument and returns the number of identical
    pairs of integers in that list

    if the list is empty or contains exactly one value, return 0

    count each complete pair once

    input: list of integers
    output: number of pairs

    data structure:
        - list of unique numbers

    algorithm:
        - get a list of unique numbers
        - for each number in that list, count how many times it occurs
        - determine the number of pairs by using floor division with the
          integer 2
        - add that number to the tally
        - return the tally

    '''

    unique = list(set(integers))

    total_pairs = 0

    for num in unique:
        count = integers.count(num)
        total_pairs += count // 2

    return total_pairs


print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

# first attempt (2/3/2025) final time: 7 mins 42 secs

