def greatest_product(digits):
    '''
    argument consists of numeric digits only

    computes the greatest product of four consec digits in the string

    argument will always have more than 4 digits

    data structure:
        - none
    
    algorithm:
        - test each combo of 4 consecutive numbers
            - increment indexes by 1 each loop
            - increment until the end index is greater than the len of digits
        - get product of each 4 consecutive numbers
            - create a helper function
            - create a range from the indices, loop through the range and multiply it to
              the cumulative product, upate cumulative product each loop
        - if the cumulative product is greater than the existing max, update the max

    '''

    max_ = float('-inf')

    start_index = 0
    end_index = start_index + 4

    while end_index <= len(digits):
        slice_prod = cumulative_product(digits[start_index: end_index])
        if slice_prod > max_:
            max_ = slice_prod
        start_index += 1
        end_index += 1

    return max_

def cumulative_product(slice_of_four):
    cum_prod = 1

    for digit in slice_of_four:
        cum_prod *= int(digit)

    return cum_prod

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

# first attempt (2/4/2025) final time: 15 mins, 35 secs