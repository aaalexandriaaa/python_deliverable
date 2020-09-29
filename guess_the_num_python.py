from random import random

difficulty = input('Choose your difficulty: Easy, Medium, or Hard: ').lower()

if difficulty == 'easy':
    highest_num = 10
elif difficulty == 'medium':
    highest_num = 100
elif difficulty == 'hard':
    highest_num = 1000
else:
    num_range = 0
    print("Please input 'small', 'medium', or 'large'")

lowest_num = 1
random_num = 1 + int(highest_num*random())
print(random_num)
guess = int(input(f'Please choose number between {lowest_num} & {highest_num}: '))
user_guesses = []
while guess != random_num:
    user_guesses.append(guess)
    wrong = ("too high" if guess > random_num else "too low")
    guess = int(input(f'Sorry! That guess is {wrong}. You have tried: {user_guesses}. Try another number: '))
print(f'Congratulations! Your guess of {guess} is correct!')