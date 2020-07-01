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
comp_choice = ""
#computer_wins = ""

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissors':2}
    return rps[choice]


def get_winner(user):
    # Access variables declared after the function so that the variables can be changed inside of the function
    global Wins, user_wins, output, computer_wins, winner
    #print(user)

    comp_choice = random.choice(['rock','paper','scissor'])

    use=choice_to_number(user)
    comp=choice_to_number(comp_choice)
    if(use==comp):
        winner = "It was a tie"
    elif((use-comp)%3==1):
        winner = "You win!"
        user_wins+=1
    else:
        winner = "The computer wins"
        computer_wins+=1

    # Use the output label to write what the computer did and what the result was (win, loss, tie)
    Wins = tk.Label(text = "Users score: " + str(user_wins))
    Computer_wins = tk.Label(text = "Computer's score: " + str(computer_wins))
    Result = tk.Label(text="Your choice: {uc} \n The computer chose: {cc} \n {w}".format(uc=user,cc=comp_choice,w=winner))
    Result.grid(column=1, row=3)
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
