# Six Scoops
Six Scoops is a terminal-based alternative to a hangman game for kids. This game combines learning with fun. The player tries to guess a word letter by letter before running out of six scoops of ice cream. It is told the player that it is very hot and it is a good idea to get an ice cream. Playing this game is an effective way to encourage kids' interest in learning English. While playing this game, kids will learn easy vocabulary (100 words) about summer. The words contain 3 to 5 letters and are appropriate for young learners.

[Link to live site]()

![Responsive mock-up](assets/images/)

---

## User Stories

**As a user I want to**

- be able to read an introduction when first loading the programm
- choose whether to read the rules to the game or not
- have a bit of time to read the parts of rules
- read the rules without introduction word in terminal
- choose a difficulty level
- be able to go back after choosing the level
- know how many scoops of ice cream I start off with
- be informed if my data input is not valid and how to solve this issue
- see which letters I have already guessed
- see the word being displayed for every correct guess
- be informed how many scoops I have left after a wrong guess
- see a graphic visualising my lost scoops
- learn the word to be guessed after losing the game
- see the full word displayed after completing the game successfully
- know when the game is over (won or lost)
- be able to play the game again after it is finished
- be able to restart the game

**As a site administrator I want to**

- be able to make upgrades to the game (add six letter words, create scoreboard)
- offer the user a short yet entertaining game

---

## Planning

The following flowchart is created with [lucidchart](www.lucidchart.com). It visualizes the planning process for this application. Also, it was adited in PDF editor.

![Flowchart](assets/images/flowchart-six-scoops.jpeg)

---

## Design

As this is simple terminal based application, the design process for the user interface was limited.

Different colour choices  are used in order to highlight and categorise messages to the user.

For example, error messages are displayed in red, while guessed letters are in bright yellow. 

The word itself is displayed blue for every correct guess. 
If the word is not guessed, the user can see the secret word with the blue arrow emoji on the left.

Emojis are used in the introduction throughout the game because the game is for kids.

Ice cream graphic illustration was made by me.

As the kids do not like reading, I colored the important words in the questions or descriptions and put emojis near them.

---

## Features

## Technologies Used

## Bugs

+ **Solved bugs**

1. The ```word_completion``` string looked like one line. And when the guessed letters joined it, letters sticked to each other. The text readability was very poor. So the user may have a bad experience.

  - *Solutions:* added spaces between each underscore character
## Testing

---

## Deployment

This project was deployed with [Heroku](https://dashboard.heroku.com) using Code Institute's mock terminal
as provided with the Python Essentials template.

 - This project requires you to have Python installed on your local PC.

 - Create a local copy of the GitHub repository by following one of the two processes below:

    - Go to the [GitHub Repo page](https://github.com/zhannamatuzak/six-scoops-ice-cream).

    - Click the Code button and download the ZIP file containing the project.
    - Extract the ZIP file to a location on your PC.
 
 - Clone the repository:

    - Open a folder on your computer with the terminal.
    - Run the following command as on the screenshot below:

    `git clone https://github.com/zhannamatuzak/six-scoops-ice-cream.git`

 - Install Python module dependencies:

    - Activate a virtual environment
    'python3 -m venv .venv' then '.venv .venv/bin/activate'

    - Run the command pip install -r requirements.txt:
    'pip install -r requirements.txt

 - Create a [Heroku](https://dashboard.heroku.com) account (if not already existing) to host the project.

 - Create a new app with Heroku by clicking on "Creat a new app":

 ![New app](assets/images/create-app.png)

 - Provide your app name and region:

    - Write your project name. 
    The repository name on GitHub and the Heroku app name do not need to be the same. 
    - Choose your region. 
    If you still have not created  your own GitHub repository to host the code, do it now.

 ![Name, region](assets/images/app-name.png)

 - Add Config Var

    - You must add a Config Var provided by Code Institute for their student in Heroku's Settings.
    - If you do not add this, then your deployment may fail.
    - Also, you can store here your sensitive date, if you have.

 ![Config var](assets/images/app-name.png)

- In Settings:
  
    - add two two buildpacks: Python and NodeJS.
    - Click "Add Buildpack" and choose. Then click "Save Changes".
    - Please note, that the order of buildpacks is important!

 ![Buildpacks](assets/images/buildpacks.png)
    
 - Go to the Deploy section. Here you can choose the deployment method: 

    - Select GitHub.
    - Click "Connect to GitHub".
    - Search for your repository name by clicking "Search". 
    - Then click "Connect" to link your Heroku account to your repository code.
    - Scroll down the page. There are two opeions in this section:
       - set up autonatic deploys;
       - set up manual deploys.
    - If you choose automathic deploys, please click "Enable Automatic Deploys";
    - If you choose manual deploys, please click "Deploy Branch".
    - Wait for instalation.
    - Then you will se the message "Your app was successfully deployed".
    - Click the "View" button which takes to the deployed link.

 ![Connect to GitHub](assets/images/connect-repo.png)

## Credits

## Acknowledgements