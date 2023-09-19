"""
ASCII art illustration for the game 
obtained from:
http://www.patorjk.com/software/taag/#p=display&h=1&f=Big&t=
"""

LOGO = """
                             🍦🍦🍦🍦🍦🍦
   _____  _____ __   __   _____   _____  ____    ____   _____    _____ 
  / ____||_   _|\ \ / /  / ____| / ____|/ __ \  / __ \ |  __ \  / ____|
 | (___    | |   \ V /  | (___  | |    | |  | || |  | || |__) || (___  
  \___ \   | |    > <    \___ \ | |    | |  | || |  | ||  ___/  \___ \ 
  ____) | _| |_  / . \   ____) || |____| |__| || |__| || |      ____) |
 |_____/ |_____|/_/ \_\ |_____/  \_____|\____/  \____/ |_|     |_____/
 """

RULES = """
=========
📜 RULES
=========

✅ Select your skill level. 

✅ The word you have to guess will get longer 
as your skill level increases.

✅ Levels
Easy Level: Short words (3 letters) for beginners. 
Medium Level: 4-letter words for those seeking a challenge.
Hard Level: 5-letter challenging words for experts.

✅ Then try and guess the word one letter at a time 
before you lose all six scoops of ice cream.

✅ Here is a hint.
All words are related to summer.

✅ You will start off with 6 scoops of ice cream. 

✅ For each wrong guess you lose one scoop.
And you can play until your cane is empty.
Do not lose! 😢 beacuse it is 🔥 outside.

Cheer up! You can try again 😉, 
simply restart the game.
Just press the RUN PROGRAM at the top.
Good luck! 😎
"""

def display_scoops(scoops):
    stages = [
            """ 
            ________
            \      /
             \    /
              \  /
               \/
               """,
             """
             ( ) ( )
             ________
             \      /
              \    /
               \  /
                \/
               """,

               """ 
            ( ) ( ) ( )
             ________
             \      /
              \    /
               \  /
                \/
               """,

               """
                ( )
            ( ) ( ) ( )
             ________
             \      /
              \    /
               \  /
                \/
               """,

               """
             ( )( )
           ( ) ( ) ( )
            ________
            \      /
             \    /
              \  /
               \/
               """,
              """
               ( )
             ( )( )
           ( ) ( ) ( )
            ________
            \      /
             \    /
              \  /
               \/
               """,
            ]
    return stages[scoops]