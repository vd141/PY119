def nearest_prime_sum(integers):
    '''
    takes list of integers

    determines the minimum integer value that can be appended to the list
    so the sum of all the elements equal the closest prime number that is greater
    than the current sum of the numbers

    data structure:
        - none

    algorithm:
        - get sum of list
            - sum function
        - find next closest prime number
            - starting at the sum, check each value until a prime is found
            - determine if candidate is prime (helper)
                - number is prime if its only factors are 1 and itself
                - loop through numbers 1 to sqrt of the number. if any of those
                  evenly divide the number, return False. otherwise, return True
        - get difference between that prime number and the sum
        - return that difference
    '''

    list_sum = sum(integers)
    prime_candidate = list_sum + 1

    while not is_prime(prime_candidate):
        prime_candidate += 1

    return prime_candidate - list_sum


def is_prime(number):
    '''
    number is prime if its only factors are 1 and itself

    loop through numbers 1 to sqrt of the number. if any of them evenly divide
    the number, return False. otherwise, return True
    '''

    if number == 1:
        return False

    root = int(number ** (1 / 2))

    for candidate in range(2, root + 1):
        if number % candidate == 0:
            return False
    
    return True

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

# first pass (2/4/2025) final time: 14 mins 8 secs

