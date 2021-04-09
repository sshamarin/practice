import random, sys, time
print(('paper, rock, scissors').upper())
wins = 0
loses = 0
ties = 0
tryes = 1

try:
    while True:
        print(f'Round number {tryes}: {wins} wins, {loses} loses, {ties} ties.')

        # If the player has entered r, p, or s, the execution breaks out of the loop.
        # Otherwise, the program reminds the player to enter r, p, s, or q and
        # goes back to the start of the loop.

        while True:
            guess = input('Make your move: (r)ock, (p)aper, (s)cissors or (q)uit: ')
            print()
            if guess == 'q':
                sys.exit()
            if guess == 'r' or guess == 'p' or guess == 's':
                break
            print('Illegal symbol. Type one of r, p, s or q')
            print()

        # reaction on player's turn
        if guess == 'r':
            print('Rock vs... ')
        elif guess == 'p':
            print('Parer vs... ')
        elif guess == 's':
            print('Scissors vs... ')

        time.sleep(1)

        random_number = random.randint(1,3)
        if random_number == 1:
            comp_turn = 'r'
            print(('Rock!').upper())
        elif random_number == 2:
            comp_turn = 's'
            print(('Scissors!').upper())
        elif random_number == 3:
            comp_turn = 'p'
            print(('Paper!').upper())

        if guess == comp_turn:
            print('It\'s a tie!')
            ties += 1
        elif guess == 'r' and comp_turn == 's':
            print('You win!')
            wins += 1
        elif guess == 'r' and comp_turn == 'p':
            print('You lose :()')
            loses += 1
        elif guess == 's' and comp_turn == 'p':
            print('You win!')
            wins += 1
        elif guess == 's' and comp_turn == 'r':
            print('You lose :(')
            loses += 1
        elif guess == 'p' and comp_turn == 'r':
            print('You win!')
            wins += 1
        elif guess == 'p' and comp_turn == 's':
            print('You lose :()')
            loses += 1

        tryes += 1

except KeyboardInterrupt:
    print()
    print('Bye!')
    sys.exit()
