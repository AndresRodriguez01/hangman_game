import random

# Constants
FILE_PATH = "words.txt"

# Hangman visuals for each incorrect guess
def hangman_visual(wrong_guesses):
    visuals = [
        # 0 wrong guesses:
        """
    ------
    |    |
    |
    |
    ...
        """,
        # 1 wrong guesses:
        """
    ------
    |    |
    |    O
    ...
        """,
        # 2 wrong guesses:
        """
    ------
    |    |
    |    O
    |    |
    ...
        """,
        # 3 wrong guesses:
        """
    ------
    |    |
    |    O
    |   /|
    ...
        """,
        # 4 wrong guesses:
        """
    ------
    |    |
    |    O
    |   /|\\
    ...
        """,
        # 5 wrong guesses:
        """
    ------
    |    |
    |    O
    |   /|\\
    |   /
    ...
        """,
        # 6 wrong guesses:
        """
    ------
    |    |
    |    O
    |   /|\\
    |   / \\
    ...
        """
    ]
    return visuals[wrong_guesses]

# Load words from a file, split by a given delimiter, and return as a list
def read_words_from_file(file_path, delimiter):
    with open(file_path, 'r') as file:
        content = file.read()
        words = list(content.split(delimiter))
    return words

# Create and return a list of blanks corresponding to the word's letters
def make_blanks_for_word(word):
    return ["_"] * len(word)

# Let the user guess a letter and check if it's in the word.
# Update the display word accordingly and return whether the guess was correct.
def check_letter_in_word(word, dis):
    while True:
        guess = input("Please guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Please enter a valid letter.")

    correct_guess = False
    for index, letter in enumerate(word):
        if letter == guess:
            dis[index] = guess
            correct_guess = True

    # Notify the user of the result of their guess
    if correct_guess:
        print(guess + " was a correct guess")
    else:
        print(guess + " was an incorrect guess")
    return correct_guess

# Main gameplay loop
def play_hangman():
    user_mistakes = 0
    # Load words and select a random word
    file_words = read_words_from_file(FILE_PATH,',')
    random_word = random.choice(file_words)
    display_word = make_blanks_for_word(random_word)
    print(random_word)

    while True:
        correct_guess = check_letter_in_word(random_word, display_word)
        
        print(display_word)
        print(hangman_visual(user_mistakes))

        if not correct_guess:
            user_mistakes += 1
            print(hangman_visual(user_mistakes))

        # Game Over condition
        if user_mistakes == 6:
            print(hangman_visual(user_mistakes))
            print("GAME OVER")
            break

        # Win condition
        if ''.join(display_word) == random_word:
            print("You won, congratulations")
            break

# Start the game
play_hangman()
