import random
import tkinter as tk
import tkinter
from random import randint

window = tkinter.Tk()
#window.geometry("400*300")
window.title("RPS")
user = ""
winner = ""
Wins = ""
#NOTE: A function that determines whether the user wins or not
#      Passes the user's choice (based on what button they click)to the parameter
def get_winner(user):
    # Access variables declared after the function so that the variables can be changed inside of the function
    global Wins, user_wins, output, computer_wins, winner
    #print(user)
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
        # if computers_play == "rock":
        #     winner = "It was a tie!"
        if computers_play == "paper":
            winner = "The computer won."
        elif computers_play == "sicssors":
            winner = "You won!"
    elif user == "paper":
        # if computers_play == "paper":
        #     winner = "It was a tie!"
        if computers_play == "scissors":
            winner = "The computer won."
        elif computers_play == "rock":
            winner = "You won!"
    elif user == "scissors":
        # if computers_play == "scissors":
        #     winner = "It was a tie!"
        if computers_play == "rock":
            winner = "The computer won."
        elif computers_play == "paper":
            winner = "You won!"

    if user == computers_play:
        winner = "It was a tie! "

    # If the user wins, increase win by 1
    if winner == "You won!":
        user_wins += 1
    if winner == "The computer won.":
        computer_wins += 1
    # Use the output label to write what the computer did and what the result was (win, loss, tie)
    Wins = tk.Label(text = "Users score: " + str(user_wins))
    Computer_wins = tk.Label(text = "Computer's score: " + str(computer_wins))
    outcome = tk.Label(text="The computer chose: " + computers_play + "\n" + winner)
    outcome.grid(column=1, row=3)
    Wins.grid(column=1, row=2)
    Computer_wins.grid(column=1, row=4)


# Use these functions as "command" for each button
# def pass_s():
#     get_winner("scissors")
# def pass_r():
#     get_winner("rock")
# def pass_p():
#     get_winner("paper")

#Variable to count the number of wins the user gets
user_wins = 0
computer_wins = 0


#START CODING HERE

def user_is_rock():
    user = "rock"
    get_winner(user)



def user_is_paper():
    user = "paper"
    get_winner(user)


def user_is_scissors():
    user = "scissors"
    get_winner(user)


# 1. Create 3 buttons for each option (rock, paper, scissors)
button1 = tk.Button(
    text="Rock",
    width=25,
    height=5,
    bg="black",
    fg="blue",
    command = user_is_rock


)


button2 = tk.Button(
    text="Paper",
    width=25,
    height=5,
    bg="black",
    fg="blue",
    command = user_is_paper
)


button3 = tk.Button(
    text="Scissors",
    width=25,
    height=5,
    bg="black",
    fg="blue",
    command = user_is_scissors
)



# 2. Create 2 labels for the result and the number of wins
Results = tk.Label(text="Results")
#Wins = tk.Label(text = user_wins)

# 3. Arrange the buttons and labels using grid
button1.grid(column=0,row=1)
button2.grid(column=0, row=2)
button3.grid(column=0,row=3)
Results.grid(column=1, row=1)
button1.grid(column=0, row=7, padx=10, pady=20)
button2.grid(column=0, row=14, padx=10, pady=20)
button3.grid(column=0, row=21, padx=10, pady=20)


#Wins.grid(column=1, row=2)




window.mainloop()
