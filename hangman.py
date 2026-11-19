import random
words = ["robotics", "blockchain", "chatbot", "cybersecurity", "algorithm"]
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []
print("===== TECHNOLOGY HANGMAN =====")
print("Guess the hidden technology word!")
print("Word:", " ".join(guessed_word))
print("Attempts remaining:", attempts)
while attempts > 0 and "_" in guessed_word:
    guess = input("Guess a letter: ").lower().strip()
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Enter only one letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong guess!")
    print("Word:", " ".join(guessed_word))
    print("Attempts remaining:", attempts)
if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word!")
    print("The word was:", word)
else:
    print("\nGame Over! You ran out of attempts.")
    print("The correct word was:", word)
