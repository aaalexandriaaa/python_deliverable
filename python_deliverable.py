# Exercise 01: Vowel or Consonant
print('EXERCISE 1')
letter = input('Please enter a letter of the alphabet: ')
useful_letter = letter.lower()

if useful_letter[0] in 'aeiou':
    print(f'{letter[0]} is a vowel')
elif useful_letter == 'y':
    print(f"depending on the context, {letter} can be used as a consonant or a vowel")
else:
    print(f'{letter} is a consonant')

# Exercise 02: Length of Phrase: 
print('EXERCISE 2')
while True:
    letter = input('Please enter a word or phrase: ')
    print(f'What you entered is {len(letter)} characters long')
    another = input('add a another? (y/n) ')
    if another == 'y':
        continue
    else:
        break

# Exercise 03: Calculate Dog Years
print('EXERCISE 3')
age = int(input('How old is your dog in human years? '))

if age <= 2:
    dog_years = age * 10
else:
    dog_years = 20 + (age - 2) * 7
    
print(f"The dog's age in dog years is {dog_years}.")

# Exercise 04: What Kind of Triangle
print('EXERCISE 4')
a = int(input('Enter the length of side a of the triangle: '))
b = int(input('Enter the length of side b of the triangle: '))
c = int(input('Enter the length of side c of the triangle: '))

if a == b == c:
    type = "an equilateral"
elif (a == b) or (a == c) or (b == c):
    type = "an isosceles"
else:
    type = "a scalene"

print(f'A triangle with sides of {a}, {b}, & {c} units is {type} triangle.')


# Exercise 05: Fibonacci Sequence
print('EXERCISE 5')
a = 0
print(f'term: 1 / number: {a}')
b = 1
print(f'term: 2 / number: {b}')
term = 3
while term <= 50:
    num = a + b # 1 / 2 / 
    print(f'term: {term} / number: {num}') # 3/1; 
    a = b  
    b = num
    term += 1 

# Exercise 06: Season 
print('EXERCISE 6')
month = input('Please enter the first 3 letters of the month: ').upper()
day = int(input('Please enter the day of the month: '))
season = "nonsense"
if month in ("JAN", "FEB"):
        season = 'Winter'
elif month in ("APR", "MAY"):
        season = 'Spring'
elif month in ("JUL", "AUG"):
        season = 'Summer'
elif month in ("OCT", "NOV"):
        season = 'Fall'
elif month == "DEC":
    if day >= 21:
        season = 'Winter'
    else:
        season = 'Fall'
elif month == "MAR":
    if day < 20:
        season = 'Winter'
    else:
        season = 'Spring'
elif month == "JUN":
    if day < 21:
        season = 'Spring'
    else:
        season = 'Summer'
elif month == 'SEP':
    if day < 22:
        season = 'Summer'
    else:
        season = 'Fall'
print(f'{month} {day} is in {season}')