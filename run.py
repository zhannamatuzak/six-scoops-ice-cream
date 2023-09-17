# import section
import random  # generates random numbers
import string  # module for string (ascii, emojis) manipulation
import sys
from time import sleep  # time delay for print statements
from words import words  # imports word list from word.py
import intro
import colorama
from colorama import Fore, Back, Style, init  # adds color to terminal text

init(autoreset=True)  # sets text to its default values

scoops = 5


def choose_level(level):
    """
    Chooses level based on user input
    """
    if level == "1":
        print(
            f"{Style.NORMAL}{Fore.LIGHTBLUE_EX}Easy:",
            f"{Style.RESET_ALL}Get your 🍦 easily cause it is 🔥.\n"
        )
        return "easy"
    elif level == "2":
        print(
            f"{Fore.LIGHTYELLOW_EX}Medium:",
            f"{Style.RESET_ALL}Get your 🍦 smartly cause it is 🔥.\n"
        )
        return "medium"
    elif level == "3":
        print(
            f"{Fore.LIGHTRED_EX}Hard:",
            f"{Style.RESET_ALL}Strain your brain to get 🍦 cause it is 🔥.\n"
        )
        return "hard"


def validate_level(value):
    """
    Checks if user input for level choice equals 1, 2 or 3
    """
    try:
        if (value != "1") and (value != "2") and (value != "3"):
            raise ValueError(
                f"Please only enter 1, 2 or 3. You typed "
                f"{Style.BRIGHT}{Fore.YELLOW}{value}{Style.RESET_ALL}"
            )
    except ValueError as e:
        print(f"{Fore.RED}Invalid data: {e}, please try again\n")
        return False
    return True


def user_level():
    """
    Gets user level value and generates word list accordingly
    """
    while True:
        input_text = f"{Fore.GREEN}Choose your level:\n\n 1. Easy\n 2. Medium\n 3. Hard\n {Style.RESET_ALL}"
        chosen_level = input(input_text)
        level = choose_level(chosen_level)

        if validate_level(chosen_level):
            select_words(words, level)
            break
    word_list = select_words(words, level)

    return word_list


def select_words(words, level):
    """
    Selects words by length and gathers into three lists
    depending on user level choice
    """
    if level == "Easy":
        easy = [word for word in words if len(word) < 4]
        return easy
    elif level == "Medium":
        medium = [word for word in words if len(word) < 5]
        return medium
    elif level == "Hard":
        hard = [word for word in words if len(word) < 6]
        return hard


def get_valid_word(words):
    """
    Chooses randomly a word from the chosen words list
    and returns it in uppercase
    """
    word = random.choice(words)
    return word.upper()


def game_rules():
    """
    Function to ask the player if he wants to read the game rules
    """
    while True:
        print(
            f"Do you want to read the game {Style.BRIGHT}{Fore.YELLOW}rules?(Y/N)")
        answer = input().upper().strip()
        if answer == "Y":
            print(intro.RULES)
            return True
        elif answer == "N":
            print("Let's get started!\n")
            return False
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")


def run_intro():
    """
    Displays logo and welcoming message
    """
    print(f"{Style.BRIGHT}{Fore.RED}{intro.LOGO}")
    typewriter("Welcome!")
    sleep(1)
    typewriter(
        f"Here you can get the Extra Large treat\nwith Six Scoops of Ice Cream.\n")
    typewriter("🍦🍦🍦🍦🍦🍦\n")
    sleep(1)
    typewriter("Oh, it is not that easy. But yummy! 🤤\n")
    sleep(0.5)
    typewriter(
        f"Here are the rules on how to get your Extra Large treat!\n")


def typewriter(text, color=Fore.WHITE):
    """
    Function to add a typewriter effect to print statements.
    """
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        sleep(.02)
    print()


def main():
    """
    Runs entire application 
    """
    global word_list
    run_intro()
    game_rules()
    word_list = user_level()


if __name__ == "__main__":
    main()
