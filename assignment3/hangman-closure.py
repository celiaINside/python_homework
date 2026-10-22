# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        display_word = ""
    
        for char in secret_word:
                if letter in guesses:
                    display_word += letter
                else: 
                    display_word += ("_")
        print (display_word)
        return all(letter in guesses for letter in secret_word)

    return hangman_closure

secret_word = input("Enter the secret word: ")
game = make_hangman(secret_word)

while True:
    guess = input("Guess a letter: ")
    if game(guess):
        print("You guessed the word!")
        break