import os
from random import choice
from sketches import HANGMANPICS
import unicodedata

def clear():
    os.system("clear")

def opening_file():
    with open("./hangman_file/data.txt") as f:
        my_list = [i.strip() for i in f]
        return my_list
        # f.close()

def strip_accents(text):

    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    return str(text)

def run():
    clear()
    # opening_file()
    
    chosen_word = choice(opening_file())
    no_accents = strip_accents(chosen_word)
    unknown_word = [i for i in chosen_word] # Each letter as an element in the list.
    print(unknown_word)
    underscore_word = [i.replace(i, "_") for i in chosen_word] # Each letter replaced by a "_".
    unknown_text = " ".join(underscore_word) # Concantes all the letters with a space betweeen each one.
    continues = 7      
    list_used_letters = []

    while chosen_word != "".join(underscore_word):

        if continues == 0:
            clear()
            print("YOU LOSE! 😲 The word was: " + chosen_word.capitalize() + " 👀")
            print("")
            print("GAME OVER 😭")
            print("")
            break        
        
        c = HANGMANPICS[7 - continues]
        used_letters = " ".join(list_used_letters)
        clear()
        # print(chosen_word)
        print(f'CONTINUES: {continues}')
        print(c)
        print("")
        print("Guess the word! 📝")
        print(unknown_text)
        print("")
        print("Letters used: " + used_letters)
        print("")
        letter = input("Type a letter: ")

        try:
            if len(letter.strip()) == 0:
                raise Exception("Blank is not allowed. Please type a letter. Press Enter.")
            elif len(letter) > 1:
                raise Exception("Please just type one letter. Press Enter.")
            elif letter.isnumeric() == True:
                raise Exception("Numbers are not allowed, please use only a letter. Press Enter.")
            elif letter in list_used_letters:
                raise Exception("Letter already used. Please use another letter. Press Enter.")

            for i in letter:
                list_used_letters.append(i)
            # list_used_letters = list_used_letters.append(letter)
            letter = strip_accents(letter)

            for a, b in enumerate(no_accents):
                if letter == b:
                    underscore_word[a] = chosen_word[a] # letter
                    unknown_text = " ".join(underscore_word)

                else:
                    continue
            
            if letter not in unknown_word:
                continues -= 1

        except Exception as ex:
            print(input(ex))          
                      
    else:
        clear()
        print("🏆 YOU WON!  The word was: ✨ " + chosen_word.capitalize() +  " ✨" )
        print("")    

if __name__ == '__main__':
    run()