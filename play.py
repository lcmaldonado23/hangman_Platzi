import hangman_spanish
import hangman_english

def main():
    print("Bienvenido al juego del ahorcado / Welcome to the hangman game.")
    while True:
        language = input("¿Quieres jugar en Español o Ingles? / Do you want to play in Spanish or English? (ESP/ENG): ").strip().upper()
        if language == "ESP":
            language = True
            break
        elif language == "ENG":
            language = False
            break
        else:
            print("¡Ingrese una opción válida! / Please enter a valid option!")

    if language == True:
        hangman_spanish.main()
    elif language == False:
        hangman_english.main()  
    else:
        print("¡Opción invalida! / Invalid option!")  

if __name__ == "__main__":
    main()