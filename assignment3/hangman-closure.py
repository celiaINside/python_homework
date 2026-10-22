# Task 4: Closure Practice
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        guesses.append(letter)
        display_word = ""
    
        for letter in secret_word:
                if letter in guesses:
                    display_word += letter
                else: 
                    display_word += ("_")
        print (display_word)
        return all(letter in guesses for letter in secret_word)

    return hangman_closure



