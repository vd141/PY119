def to_weird_case(sentence):
    '''
    takes a string argument (sentence) and reutrns a copy of the string with
    every second character in every third word converted to uppercase

    other characters should remain the same

    input: sentence (words separated by spaces)
    output: sentence with second letter of every third word capitalized

    implicit: words are separated by spaces, words are alphabetic

    data structures:
        - string to hold every third word that we will perform the capitalization
          on

    algorithm:
        - loop through every word in the input sentence. append that word to a
          new empty sentence list
        - if the word is a third word, this is the word we will be operating on
            - go through each character of the word. add each letter to an empty
              string
            - if the character is a second character, capitalize that letter before
            adding it to the empty string
        - append that new third word to the empty sentence list
    '''

    new_sentence = []

    words = sentence.split()

    for idx, word in enumerate(words):
        if (idx + 1) % 3 == 0:
            new_word = ''
            for idx, letter in enumerate(word):
                if (idx + 1) % 2 == 0:
                    letter = letter.upper()
                new_word += letter
            new_sentence.append(new_word)
        else:
            new_sentence.append(word)
    
    return ' '.join(new_sentence)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

# First attempt (2/2/2025) final time: 16 mins 34 secs