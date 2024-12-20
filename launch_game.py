import os
from random import randint


def play_game():
    reset_seen_words()
    print_welcome_menu()


def print_welcome_menu():
    print("\n" + "*" * 50)
    print("        Welcome to my Memory Game         ")
    print("A series of words will be presented to you.")
    print("The goal is to indicate whether the word has appeared before or not.")
    print("   You earn 1 point for each correct answer. Good luck brotha!")
    print("Press Ctrl+C to exit the game.")
    print("Press 1 to start the game.")
    print("Press 2 to reset the record.")
    print("*" * 50 + "\n")
    choice = input()
    if choice == "1":
        new_round(0)
    if choice == "2":
        reset_record()
        print_welcome_menu()
    elif choice != "1":
        print("Invalid choice, please try again.")
        clear_screen()
        print_welcome_menu()

def ask_is_word_seen(word) -> bool:
    top = "Have you seen this word?"
    print(top)
    print(word)
    choice = input("1: SEEN 2: NEW\n")
    if choice in ["1", "2"]:
        return choice == "1"
    else:
        clear_screen()
        print("PLEASE FOCUS, enter '1' for SEEN or '2' for NEW")
        return ask_is_word_seen(word)


def loose_game(score):
    clear_screen()
    record = load_record()
    print("YOU DIED")
    if score > record:
        save_record(score)
        print("NEW RECORD!")
    print(f"FINAL SCORE: {score}\nOLD RECORD: {record}")
    display_try_again_screen()


def is_word_seen(word):
    with open("resources/seen_words_list.txt", 'r', encoding='utf-8') as seen_words_list_fr:
        return word + '\n' in seen_words_list_fr.readlines()


def get_random_word():
    with open("resources/word_list.txt", "r", encoding="utf-8") as word_list_fr:
        return random_choice(word_list_fr.readlines())


def win_round(score):
    clear_screen()
    score += 1
    new_round(score)


def add_word_to_seen_words(word):
    with open('resources/seen_words_list.txt', "a", encoding="utf-8") as seen_word_list_fw:
        seen_word_list_fw.write(word + '\n')


def load_record():
    try:
        with open('resources/record.txt', 'r', encoding='utf-8') as record_file:
            return int(record_file.readline().strip())
    except FileNotFoundError:
        return 0


def save_record(record):
    with open('resources/record.txt', 'w', encoding='utf-8') as record_file:
        record_file.write(str(record))


def new_round(score):
    word = get_random_word()
    try:
        choice = ask_is_word_seen(word)
        answer = is_word_seen(word)
        if choice == answer:
            add_word_to_seen_words(word)
            win_round(score)
        else:
            loose_game(score)
    except KeyboardInterrupt:
        print("\nGame interrupted.")
        exit()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def reset_seen_words():
    with open('resources/seen_words_list.txt', 'w', encoding='utf-8'):
        pass


def random_choice(choices):
    return choices[randint(0, len(choices) - 1)].strip()


def display_try_again_screen():
    choice = input("TRY AGAIN? (Y/n) ")
    if choice.lower() == "n":
        print("SEE YA!")
        exit()
    else:
        clear_screen()
        play_game()


def reset_record():
    save_record(0)
    print("Record reset to 0.")

if __name__ == "__main__":
    play_game()
