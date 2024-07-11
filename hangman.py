from replit import clear
import random
import hangman_art
import hangman_words
chosen_word = random.choice(hangman_words.word_list)

display = []
for letter in chosen_word:
    display += "_"

lives = 6
print(hangman_art.logo)
while "_" in display:
    guess = input("Guess a letter:").lower()
    clear()
    position = 0 
    for letter in chosen_word:
        if letter == guess:
            display[position] = guess
        position += 1
    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in the word. You lose a life.")
    if lives == 0:
        print(hangman_art.stages[0])
        print(f"You lose! The word was {chosen_word}.")
        break
    if "_" not in display:
        print(*display, sep = ' ')
        print(hangman_art.stages[lives])
        print("You win!")
        break
    print(f"lives = {lives}")
    print(*display, sep = ' ')
    print(hangman_art.stages[lives])
    
