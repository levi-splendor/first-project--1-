
def guessing_game(secret_number, max_attempts):
    print('Guess the secret number between 1 and 100!')
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input(f'Attempt {attempts + 1}/{max_attempts}: '))
            attempts += 1
            if guess == secret_number:
                print('Correct!')
                break
            elif guess > secret_number:
                print('Too high')
            else:
                print('Too low')
        except:
            print('Invalid input')
    print(f'You used {attempts} attempts.')

guessing_game(42, 7)
