def count_substrings(parent_string, substring):
    '''
    takes two string arguments and returns the number of times the second string
    occurs in the first substring

    overlapping strings don't count

    i know there is a built in string method that counts the number of occurrences
    of a substring in a string

    let's assume the problem wants us to do this algorithmically

    input: parent string, substring
    output: substring count in parent

    overlapping strings don't count

    data structure;
        - none

    algorithm:
        - loop through the parent string up until len(parent) - len(substring)
            - create a starting index and an end index for the slice window
        - create a slice of the parent string equal to the length of substring
        - compare the slice to the substring
        - if they are the same, increase the substring count by 1
            - shift the starting index of the next slice to the first character
              after the current slice's last character
        - continue until the end of the parent string
    '''

    start_index = 0
    end_index = start_index + len(substring)
    substring_count = 0

    while end_index <= len(parent_string):
        slice_ = parent_string[start_index:end_index]
        if slice_ == substring:
            substring_count += 1
            start_index = end_index
            end_index += len(substring)
            continue
        start_index += 1
        end_index += 1
        
    return substring_count


    # return str1.count(str2)

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

# first attempt (2/3/2025) final time: 19 mins 00 secs