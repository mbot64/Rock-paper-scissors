import random
import tkinter as tk
import tkinter
from random import randint

#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(call):

    # Access variables declared after the function so that the variables can be changed inside of the function
    global wins, win, output

    # 1. Create random integer 1-3 to use as computer's play
    computers_play = randint(1,3)

    # 2. Using if-statements, assign the computer to a choice (rock, paper, scissors) using the random integer generated
    if computers_play == 1:
        computers_play = "rock"
    elif computers_play == 2:
        computers_play = "paper"
    elif computers_play == 3:
        computers_play = "scissors"

    # 3. Determine the winner based on what the user chose and what the computer chose
    if user == "rock":
        if computers_play == "rock":
            winner = "It was a tie! "
        elif computers_play == "paper":
            winner = "The computer won. "
        elif computers_play == "sicssors":
            winner = "You won! "
    elif user == "paper":
        if computers_play == "paper":
            winner = "It was a tie! "
        elif computers_play == "scissors":
            winner = "The computer won. "
        elif computers_play == "rock":
            winner = "You won! "
    elif user == "scissors":
        if computers_play == "scissors":
            winner = "It was a tie! "
        elif computers_play == "rock":
            winner = "The computer won. "
        elif computers_play == "paper":
            winner = "You won! "
    # If the user wins, increase win by 1
    if winner == "You won!":
        win = win + 1
    # Use the output label to write what the computer did and what the result was (win, loss, tie)
    outcome = tk.Label(text="The computer chose: " + computers_play + "\n" + winner)


# Use these functions as "command" for each button
def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")

window = tkinter.Tk()

#Variable to count the number of wins the user gets
win = 0


#START CODING HERE

# 1. Create 3 buttons for each option (rock, paper, scissors)
rock = tk.Button(
    text="Rock",
    width=25,
    height=5,
    bg="black",
    fg="white",
)

paper = tk.Button(
    text="Paper",
    width=25,
    height=5,
    bg="black",
    fg="white",
)

scissors = tk.Button(
    text="Scissors",
    width=25,
    height=5,
    bg="black",
    fg="white",
)

# 2. Create 2 labels for the result and the number of wins
Results = tk.Label(text="The result is")
Wins = tk.Label(text = win)

# 3. Arrange the buttons and labels using grid

window.mainloop()
