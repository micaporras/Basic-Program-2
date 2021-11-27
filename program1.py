# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

# Function for asking an input
def get_input():
    my_string = input("Sentence: ")
    return my_string

my_string = get_input()
# Counting the words
word_count = 1
for word in my_string:
    if word == ' ':
        word_count = word_count + 1
    else:
        word_count = word_count + 0
print(f"Words: {word_count}")
# Counting the vowels
vowel_count = 0
for vowel in my_string:
    if vowel in 'AEIOUaeiou':
        vowel_count = vowel_count + 1
    else:
        vowel_count =  vowel_count + 0
print(f"Vowels: {vowel_count}")
# Counting consonants
conso_count = 0
for consonants in my_string:
    if consonants in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
        conso_count = conso_count + 1
    else:
        conso_count =  conso_count + 0
print(f"Consonants: {conso_count}")