from random import randint

# num = randint(1,101)
# x = 0
# guess_list = [0]
# quit = True
# while quit:
#     guess = int(input('Guess the number which is between 0-100\n'))
#     guess_list.append(guess)
#     if guess < 1 or guess > 100:
#         print('OUT OF BOUNDS')
#         x += 1
#     elif guess == num:
#         x += 1
#         print('You guessed the number correctly at your ' + str(x) + '. guess!')
#         quit = False
#     elif (num - 10 <= guess <= num + 10) and x == 0:
#         print('WARM!')
#         x += 1
#     elif (num - 10 > guess > num + 10) and x == 0:
#         print('COLD!')
#         x += 1
#     elif x != 0 and ((guess_list[-2] > guess > num)or(num > guess > guess_list[-2])):
#         print('WARMER!')
#         x += 1
#     elif x != 0 and ((guess > guess_list[-2] > num)or(num > guess_list[-2] > guess)):
#         print('COLDER!')
#         x += 1
#     else:
#         x += 1

num = randint(1,101)
guesses = [0]
while True:
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess?\n"))
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
    guesses.append(guess)
    if guesses[-2]:
        if abs(num - guess) < abs(num - guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
    else:
        if abs(num - guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
