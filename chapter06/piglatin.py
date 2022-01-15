# english to piglatin
# if word begins with vowel, the word yay is added to the end of it
# if word begins with a consonant or consonant cluster, that is moved to the end of the word followed by ay


print('enter message in english:')
message = input()

VOWELS = ('a','e','i','o','u','y')

piglatin = []
for word in message.split():
    # seperate nonletters at start
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    # if no letters, just append nonletter word and go to next word
    if len(word) == 0:
        piglatin.append(prefix_non_letters)
        continue
    # seperate nonletters at end
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]
    # remember case
    was_upper = word.isupper()
    was_title = word.istitle()
    word = word.lower()
    # seperate consonants at start
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]
    #add pig latin to end
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'
    # set word back to uppercase or title case
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
    # add the non-letters back to start or end
    piglatin.append(prefix_non_letters + word + suffix_non_letters)

# join all words
print(' '.join(piglatin))