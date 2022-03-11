import random
import os
from hangman_figures.hangman_figures import hangman_figures


def read_data(filepath="./base_de_datos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def keep_playing():
        while True:
            keep_playing = input("¿Quieres jugar de nuevo? (S/N): ").strip().upper()
            if keep_playing == "N":
                keep_playing = False
                break
            elif keep_playing == "S":
                keep_playing = True
                break
            else:
                print("¡Ingrese una opción válida!")
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
        os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
        print("¡Adivina la palabra!")
        if (len(hangman_figures) - 1 - failures) == 1:
            print(f"Tienes {len(hangman_figures) - 1 - failures} oportunidad restante.")
        else:
            print(f"Tienes {len(hangman_figures) - 1 - failures} oportunidades restantes.")
        print(hangman_figures[failures])
        print("\n")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        
        while True:
            letter = input("Ingresa una letra: ").strip().upper()
            if letter in guessed_words:
                print("Ya intentaste la letra " + letter + ".")
            else:
                if letter.isalpha() == True and len(letter) == 1:
                    guessed_words.append(letter)
                    break
                elif letter.isalpha() == True and len(letter) > 1:
                    print("¡Sólo puedes ingresar una letra a la vez!")
                else:
                    print("¡Sólo puedes ingresar letras del alfabeto!")


        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        else:
            failures += 1
        

        if "_" not in chosen_word_list_underscores:
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
            print("¡Ganaste! La palabra era " + chosen_word + ".\n")
            break


        if failures == (len(hangman_figures) - 1):
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
            print("¡Perdiste! La palabra era " + chosen_word + ".")
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
