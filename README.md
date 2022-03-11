# Versión en Español

## Juego del ahorcado
Este repositorio contiene una implementación del juego del ahorcado realizada para el curso de Python intermedio: Comprehensions, lambdas y manejo de Errores en Platzi.

El juego es una implementación sencilla con todas las funcionalidades requeridas para el juego tales como: el registro de palabras ya intentadas, manejo de entradas invalidas, visualización del juego usando arte ASCII y renicio del juego si el jugador quisiera seguir jugando.

## Manejo del juego del ahorcado
El juego puedo iniciarse de dos maneras. La primera es haciendo uso del script

```
py play.py
```
Este script inicia el juego y pregunta al usuario si quiere jugar el juego del ahorcado en español o en ingles. La segunda manera es directamente iniciar el juego en español o en ingles como se muestra en las siguiente lineas:

```
py hangman_spanish.py
py hangman_english.py 
```
## Jugando el juego del ahorcado
Al iniciar el juego una palabra es tomada aleatoriamente de la base de datos de palabras. El jugador tiene ocho intentos para poder adivinar la palabra. Cuando se acaba la ronda, el juego preguntará al usuario si el quiere seguir jugando o no. **Nota:** En la versión en español las vocales con tildes son diferentes a sus versiones sin tildes, ejemplo, la vocal "e" es diferente a "é". Esto hace el juego mas retador!.

## Modificar listado de palabras
El listado de palabras puede modificarse en el archivo:
```
./base_de_datos/data.txt
```
para la versión en español y en el archivo:
```
./data_base/data.txt
```
para la versión en ingles.
#

# English Version

## Hangman game
This repository contains an implementation of the hangman game done during the course: "Curso de Python intermedio: Comprehensions, lambdas y manejo de Errores" in Platzi.

The game is a simple implementation with all the required functionalities such as: keeping a register of previously used letters, invalid entry management, visualization of the game using ASCII art, and a reset function to start the game over again.

## Management of the hangman game
The game can be initiated in two ways. The first one is running the script
```
py play.py
```
This script starts the game and ask the player if he/she wants to play the game in Spanish or English. The second option is running the game either in Spanish or English, using the following lines:
```
py hangman_spanish.py
py hangman_english.py 
```

## Playing the hangman game
At the beginning of the game, a word is chosen randomly from the database of words. The player has eight tries to guess the word. At the end of each round, the game will ask the player if he/she wants to keep playing or not. **Note:** In the Spanish version, the vowels with accents are different from those without accents, e.g., the vowel "e" is different from "é." This makes the game harder!

## Modify the lists of words
The list of words can be modified in the file:
```
./base_de_datos/data.txt
```
for the Spanish version, and in the file:
```
./data_base/data.txt
```
for the English version.

