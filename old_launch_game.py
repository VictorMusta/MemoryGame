## most optimized version made by me, the used on have been optimized with chatGPT.
import os

from random import randint


def play_game():
    with open('resources/seen_words_list.txt', 'w', encoding='utf-8') as used_words_fw:
        used_words_fw.writelines('')
    new_round(0)


def ask_is_word_seen(word) -> int:
    top = "Have you seen this word?"
    print(top)
    print(word)
    choice = input("1: SEEN 2: NEW\n")
    if choice == "1":
        return True
    if choice == "2":
        return False
    else:
        os.system("clear")
        print("please focus, type '1' for SEEN or '2' for NEW")
        return ask_is_word_seen(word)


def loose_game(score):
    os.system("clear")
    print("YOU DIED")
    print("FINAL SCORE: " + str(score))
    print("TRY AGAIN?")
    choice = input("Y/n")
    if choice == "n":
        print("SEE YA!")
        exit()
    else:
        play_game()


def is_word_seen(word):
    with open("resources/seen_words_list.txt", 'r', encoding='utf-8') as seen_words_list_fr:
        words = seen_words_list_fr.readlines()
        if word in words:
            return True
    return False


def get_random_word():
    with open("resources/word_list.txt", "r", encoding="utf-8") as word_list_fr:
        words = word_list_fr.readlines()
        return words[randint(0, len(words) - 1)]


def win_round(score):
    score += 1
    new_round(score)


def add_word_to_seen_words(word):
    with open('resources/seen_words_list.txt', "a", encoding="utf-8") as seen_word_list_fw:
        seen_word_list_fw.writelines(word)


def new_round(score):
    word = get_random_word()
    choice = ask_is_word_seen(word)
    answer = is_word_seen(word)
    if choice == answer:
        os.system("clear")
        add_word_to_seen_words(word)
        win_round(score)
    else:
        os.system("clear")
        loose_game(score)
