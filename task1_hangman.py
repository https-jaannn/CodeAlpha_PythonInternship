import random

words = ["python", "computer", "keyboard", "internet", "program"]
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=== HANGMAN GAME ===")
print("Guess the word one letter at a time.")
print("You can make up to 6 incorrect guesses.")

while wrong_guesses < max_wrong_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word.strip())
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)
    print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try another.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Incorrect guess!")

if wrong_guesses == max_wrong_guesses:
    print("\nGame over! The word was:", secret_word)
