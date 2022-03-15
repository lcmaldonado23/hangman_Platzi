import random
import os
from hangman_figures.hangman_figures import hangman_figures


clearConsole =lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def read_data(filepath="./data_base/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def keep_playing():
        while True:
            keep_playing = input("¿Do you want to play again? (Y/N): ").strip().upper()
            if keep_playing == "N":
                keep_playing = False
                break
            elif keep_playing == "Y":
                keep_playing = True
                break
            else:
                print("¡Please enter a valid option!")
        return keep_playing


def hangman_game():
    data = read_data()
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
    

    failures = 0
    guessed_words = []
    while True:
        clearConsole()
        print("¡Guess the word!")
        if (len(hangman_figures) - 1 - failures) == 1:
            print(f"You have {len(hangman_figures) - 1 - failures} opportunity left.")
        else:
            print(f"You have {len(hangman_figures) - 1 - failures} opportunities left.")        
        print(hangman_figures[failures])
        print("\n")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        
        while True:
            letter = input("Enter a letter: ").strip().upper()
            if letter in guessed_words:
                print("You have already tried " + letter + ".")
            else:
                if letter.isalpha() == True and len(letter) == 1:
                    guessed_words.append(letter)
                    break
                elif letter.isalpha() == True and len(letter) > 1:
                    print("¡You can only enter one letter at a time!")
                else:
                    print("¡You can only enter one alphabet letters!")


        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        else:
            failures += 1
        

        if "_" not in chosen_word_list_underscores:
            clearConsole()
            print("¡You won! The word was " + chosen_word + ".\n")
            break


        if failures == (len(hangman_figures) - 1):
            clearConsole()
            print("¡You lost! The word was " + chosen_word + ".")
            print(hangman_figures[failures])
            print("\n")
            break      


def main():
    playing = True
    while playing == True:
        hangman_game()
        playing = keep_playing()


if __name__ == '__main__':
    main()
