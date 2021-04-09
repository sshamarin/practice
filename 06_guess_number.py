import random
number = random.randint(14,88)
print('try guess a number from 14 to 88. you\'ll have 5 tryes')
print()

for i in range(1,6):
    guess = int(input())

    if guess > number:
        print('try %s. too high' % i)
    elif guess < number:
        print('try %s. too low' % i)
    else:
        print()
        print('exactly! %s' % number)
        print('you guessed %s for %s tryes' % (number, i))
        break
print()
if guess != number:
    print('lol not. it was %s' % number)
