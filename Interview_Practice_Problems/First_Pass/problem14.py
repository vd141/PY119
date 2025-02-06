def seven_eleven(num):
    '''
    takes a single integer argument and returns the sum of all the mlutiples of
    7 or 11 that are less than the argument. if a number is a multiple of 7 and
    11, count it once.

    input: number
    output: count of multiples

    data structure:
        - set of multiples of 7 under the num
        - set of multiples of 11 under the num

    algorithm:
        - find all multiples of 7 under the num and store in a set
        - find all multiples of 11 under the num and store in a set
        - return the length of the union of those two sets
    '''

    mult_of_7 = {num for num in range(1, num) if num % 7 == 0}
    mult_of_11 = {num for num in range(1, num) if num % 11 == 0}

    return sum(mult_of_7.union(mult_of_11))

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

# first attempt (2/4/2025) final time: 4 mins, 15 secs