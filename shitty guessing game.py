import random
print('I am thinking of a number between 1 and 100 inclusive.\n To start, please enter a number')
answer = random.randint(1,100)
correctGuess = False
tries = 0
while not correctGuess:
    tries += 1
    guess = int(input())
    if guess < 1 or guess > 100:
        print('Can you read it fucking says 1 to 100 inclusive')
    elif guess > answer:
        print('Too high!')
    elif guess < answer:
        print('Too low!')
    else:
        print(f'Ding, ding, ding! You guessed the number! The number was {answer}\n You guessed the answer in {tries} tries!')
        print('Type Y to play again')
        if input() == 'Y':
            answer = random.randint(1,100)
            tries = 0
            continue
        else:
            break
            exit 
