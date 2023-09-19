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


alphabet = set(string.ascii_uppercase)  # stores letters A-Z
scoops = 5  # number ice cream scoops that can be lost


def choose_level(level):
    """
    Chooses level based on user input
    """
    if level == "1":
        print(
            f"{Style.NORMAL}{Fore.LIGHTBLUE_EX}Easy:",
            f"{Style.RESET_ALL}Get your  easily cause it is 🔥.\n"
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
        user_level = choose_level(chosen_level)

        if validate_level(chosen_level):
            select_words(words, user_level)
            break
    word_list = select_words(words, user_level)

    return word_list


def select_words(words, level):
    """
    Selects words by length and gathers into three lists
    depending on user level choice
    """

    if level == "easy":
        easy = [word for word in words if len(word) == 3]
        return easy
    elif level == "medium":
        medium = [word for word in words if len(word) == 4]
        return medium
    elif level == "hard":
        hard = [word for word in words if len(word) == 5]
        return hard


def get_word(words):
    """
    Chooses randomly a word from the chosen words list
    and returns it in uppercase
    """
    word = random.choice(words)
    return word.upper()


def validate_letter(letter):
    """
    Validates user input if letter is in alphabet
    """
    try:
        if letter not in alphabet:
            raise ValueError(
                f"Please enter a single letter from A to Z. "
                f"You typed {Fore.YELLOW}{letter}{Style.RESET_ALL}"
            )
    except ValueError as e:
        print(f"{Fore.RED}Invalid data: {e}{Fore.RESET}.\n")
        return False
    return True


def start_game():
    """
    Runs and updates game development, provides 
    feedback to the user until the game is over.
    """
    # variables
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []  # stores letters guessed by user
    guessed_words = []
    print("Let's play!")
    # prints a number of scoops and displays the word to guess
    print(intro.display_scoops(scoops))
    print(f"{Fore.LIGHTBLUE_EX}{word_completion}")
    print("\n")
    # a while loop to handle the users input
    while not guessed and scoops > 0:
        print(
            f"You've guessed these letters so far: "
            f"{Style.BRIGHT}{Fore.YELLOW}{' '.join(guessed_letters)}\n"
        )
        guess = users_letter()
        # checks if a guessed letter has already been guessed or belongs to the word
        if len(guess) == 1 and guess.isalpha():
            if guess not in word:
                scoops_number()
                guessed_letters.append(guess)
            else:
                print("Good job!,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        #
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed the word", guess)
            elif guess != word:
                print(guess, "is not in the word.")
                scoops_number()
                guessed_words.append(guess)
            else:
                guessed: True
                word_completion = word
        else:
            print(f"{Fore.RED}It is not a valid guess.")
        print(intro.display_scoops(scoops))
        print(f"{Fore.LIGHTBLUE_EX}{word_completion}")
        print("\n")
    # shows the end of the game: user wins or loses
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print(f"Sorry, you have only a cone left 😢 The word was " +
              word + " Maybe next time!")


def users_letter():
    """
    Asks a user to type a letter and checks if it is in the word
    """
    while True:
        guess = input("Please guess a letter:\n").upper()
        if validate_letter(guess):
            break
    return guess


def scoops_number():
    """
    Decrements scoops for each wrong guess
    """
    global scoops
    scoops -= 1
    print(
        f"Wrong letter! You have {Style.BRIGHT}{Fore.YELLOW}{scoops}{Style.RESET_ALL} scoops of 🍦 left.\n")


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
            print(f"{Fore.RED}Invalid choice. Please enter 'Y' or 'N'.")


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


def restart_game():
    """
    Asks player whether he wants to play again or quit this game.
    """
    while True:
        print(f"Do you want to play {Style.BRIGHT}{Fore.YELLOW}again?(Y/N)")
        choice = input().upper().strip()
        if choice == "Y":
            main()
            return True
        elif choice == "N":
            print("Bye! Hope, you did like the ice scream 🍦!")
            return False
        else:
            print("{Fore.RED}Invalid choice. Please enter 'Y' or 'N'.")


def main():
    """
    Runs entire application 
    """
    global word_list, word, level
    run_intro()
    game_rules()
    word_list = user_level()
    word = get_word(word_list)
    start_game()
    restart_game()


if __name__ == "__main__":
    main()
