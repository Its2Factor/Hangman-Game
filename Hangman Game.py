import random
import string


def play_hangman():
    word_list = ["raining", "cloudy", "windy", "foggy", "hot", "cold", "snowy",
                 "hail", "warm", "sunny", "overcast", "thunder", "lightning"]
    word = random.choice(word_list)

    attempts = 6
    guessed_letters = []
    current_state = "_" * len(word)

    while attempts > 0:
        if attempts == 6:
            print("\nCurrent State:", current_state)
        else:
            print("Current State:", current_state)

        print("Attempts Left:", attempts)
        print("Guessed Letters:", guessed_letters)

        guess = input("Enter your guess: ").lower()

        print()

        if len(guess) != 1 or guess not in string.ascii_lowercase or guess in guessed_letters:
            print("Try a different letter.")
            continue

        new_state = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_state += guess
            else:
                new_state += current_state[i]

        current_state = new_state

        if current_state == word:
            print("Congratulations! You guess the word correctly:", (str(word)).capitalize())
            break

        if guess not in word:
            attempts -= 1
            guessed_letters.append(guess)

        if attempts == 0:
            print("You lost, the word was:", word)
            break

    play_again = input("\nWould you like to play again: YES / NO? ").lower() == 'y'
    if play_again:
        play_hangman()


play_hangman()
