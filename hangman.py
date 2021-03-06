import random, string, sys
from xml.sax.handler import all_properties
from words import words

def main():
    hangman()

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def display_stages(lives_left):
    stages = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+
    O   |
        |
        |
       ====''','''      
    +---+
    O   |
    |   |
        |
       ===''','''
    +---+
    O   |
   /|   |
        |
       ===''','''
    +---+
    O   |
   /|\  |
        |
       ===''','''
    +---+
    O   |
   /|\  |
   /    |
       ===''','''
    +---+
    O   |
   /|\  |
   / \  |
       === '''     
    ]
    return stages[abs(lives_left-6)]

def restart():
    user_input = input('\nPlay again?(y/n): ')
    if user_input.lower() == 'y':
        hangman()
    else:
        sys.exit()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives != 0:
        print(display_stages(lives))
        # letters used
        print('\nYou have', lives, 'lives left and have used these letters: ', ' '.join(used_letters))

        # current word (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list) + '\n')
        
        
        # get user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1 # Take away a life if wrong
                print('Letter is not in word.\n')
    
        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again.')
     
    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(display_stages(lives))
        print('You died, sorry. The word was', word)
        restart()

    else:
        print('You guessed the word!')
        restart()

if __name__ == '__main__':
    main()