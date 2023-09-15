# import section
import random  # generates random numbers
import string  # module for string (ascii, emojis) manipulation
from time import sleep  # time delay for print statements
from words import words  # imports word list from word.py
import intro
import colorama
from colorama import Fore, Back, Style, init  # adds color to terminal text

init(autoreset=True)  # sets text to its default values


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


def main():
    """
    Runs entire application 
    """
    run_intro()
    game_rules()


if __name__ == "__main__":
    main()
