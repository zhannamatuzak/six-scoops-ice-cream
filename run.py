# import section
import random  # generates random numbers
import string  # module for string (ascii, emojis) manipulation
from time import sleep  # time delay for print statements
from words import words  # imports word list from word.py
import intro
import colorama
from colorama import Fore, Back, Style, init  # adds color to terminal text

init(autoreset=True)  # sets text to its default values


def choose_level(level):
    """
    Chooses level based on user input
    """
    if level == 1:
        print(
            f"{Style.NORMAL}{Fore.LIGHTBLUE_EX}Easy:",
            f"{Style.RESET_ALL}Get your 🍦 easily cause it is 🔥.\n"
        )
        return "easy"
    elif level == 2:
        print(
            f"{Fore.LIGHTYELLOW_EX}Medium:",
            f"{Style.RESET_ALL}Get your 🍦 smartly cause it is 🔥.\n"
        )
        return "medium" 
    elif level == 3:
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
        if (value != 1) and (value != 2) and (value != 3):
            raise ValueError(
                f"Please only enter 1, 2 or 3. You typed this "
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
        chosen_level = int(input(input_text))
        level = choose_level(chosen_level)

        if validate_level(chosen_level):
            select_words(words, level)
            break
    word_list = select_words(words, level)

    return word_list


def select_words(words, level):
    """
    Selects words by length into three lists
    depending on user level choice
    """
    if level == "Easy":
        easy = [word for word in words if len(word) < 4]
        return easy
    elif level == "Medium":
        Medium = [word for word in words if len(word) < 5]
        return Medium
    elif level == "Hard":
        hard = [word for word in words if len(word) < 6]
        return hard
    

def game_rules():
    """
    Function to ask the player if he wants to read the game rules
    """
    while True:
        print(f"Do you want to read the game {Style.BRIGHT}{Fore.YELLOW}rules?(Y/N)")
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
    print("Welcome!")
    print(f"Here you can get the Extra Large treat\nwith Six {Fore.LIGHTYELLOW_EX}Scoops of Ice Cream.\n")
    print("🍦🍦🍦🍦🍦🍦\n")
    sleep(1)
    print("Oh, it is not that easy. But yummy! 🤤\n")
    sleep(0.5)
    print(
        f"Here are the rules on how to get your {Style.BRIGHT}Extra Large treat!\n")
    

def main():
    """
    Runs entire application 
    """
    run_intro()
    game_rules()
    word_list = user_level()


if __name__ == "__main__":
    main()
