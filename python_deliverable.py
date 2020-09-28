# Exercise 01: Vowel or Consonant
letter = input('Please enter a letter of the alphabet: ')
useful_letter = letter.lower()

if useful_letter[0] in 'aeiou':
    print(f'{letter[0]} is a vowel')
elif useful_letter == 'y':
    print(f"depending on the context, {letter} can be used as a consonant or a vowel")
else:
    print('{letter} is a consonant')

# Exercise 02: Length of Phrase: 
while True:
    letter = input('Please enter a word or phrase: ')
    print(f'What you entered is {len(letter)} characters long')
    another = input('add a another? (y/n) ')
    if another == 'y':
        continue
    else:
        break

# Exercise 03: Calculate Dog Years

age = int(input('How old is your dog in human years? '))

if age <= 2:
    dog_years = age * 10
else:
    dog_years = 20 + (age - 2) * 7
    
print(f"The dog's age in dog years is {dog_years}.")