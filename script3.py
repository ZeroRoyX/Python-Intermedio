import random
import os


def read_data(filepath="./hangman_file/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def run():
    data = read_data(filepath="./hangman_file/data.txt")
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    print(chosen_word_list)
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    print(chosen_word_list_underscores)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        # print(idx, letter)
        # print(letter_index_dict.get(letter))
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
            # print(letter_index_dict)
        letter_index_dict[letter].append(idx)
        # print(letter_index_dict)
        # print(letter_index_dict.get(letter))
    
    # while True:
    #     os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
    #     print("¡Adivina la palabra!")
    for element in chosen_word_list:
        # print(element)
        print(element, end="")

    # print("\n")

        # letter = input("Ingresa una letra: ").strip().upper()
        # assert letter.isalpha(), "Solo puedes ingresar letras"

        # if letter in chosen_word_list:
        #     for idx in letter_index_dict[letter]:
        #         chosen_word_list_underscores[idx] = letter
        
        # if "_" not in chosen_word_list_underscores:
        #     os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
        #     print("¡Ganaste! La palabra era", chosen_word)
        #     break


if __name__ == '__main__':
    run()
