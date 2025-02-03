def minimum_sum(integers):
    '''
    takes a list of integers

    function shoudl return the minimum sum of 5 consecutive numbers in the list

    if the list contains fewer than 5 elements, return None

    input: list of integers
    output: minimum sum (integer)

    data structures:
        - a list containing all sums of 5 consecutive integers

    algorithm:
        - return None if len of the input list is less than 5
        - sum the first five elements in the list
            - first index of the window is 0, last index is 4 (starting index + 4)
        - append that sum to the list of sums
        - move to the next combination of five consecutive elements and get
          their sum
            - incrase the first index by 1
            - if the last index is greater than or equal to the length of the
              list, break out of the loop
        - append that sum to the list of sums
        - continue until the end of the list is reached
        - once the loop is broken, find the minimum value of all sums and return
          it
    '''

    if len(integers) < 5:
        return

    all_sums = []

    for start_idx in range(len(integers)):
        end_idx = start_idx + 5
        if end_idx > len(integers):
            break
        current_sum = sum(integers[start_idx: end_idx])
        all_sums.append(current_sum)

    return min(all_sums)

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

# Attempt 1 (2/2/2025): final time: 15 mins, 22 seconds