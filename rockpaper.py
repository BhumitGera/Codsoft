from tkinter import *
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Opponent wins!"

def handle_choice(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)

    result_label.config(text=f"You chose {user_choice}\nOpponent chose {computer_choice}\n{result}")

    if result == "You win!":
        user_score.set(user_score.get() + 1)
    elif result == "Opponent wins!":
        computer_score.set(computer_score.get() + 1)

root=Tk()
root.title("Rock Paper Scissors Game")
root.geometry("300x340+300+50")

instruction_label = Label(root, text="Choose rock, paper, or scissors:",font=('times new roman',17),bg='black',fg='white')
instruction_label.place(x=0 , y=10)

user_score =IntVar()
computer_score =IntVar()

user_score.set(0)
computer_score.set(0)

user_score_label =Label(root, text="Your Score: ")
user_score_label.place(x=115 , y=50)
user_score_display =Label(root, textvariable=user_score)
user_score_display.place(x=140 , y=70)

computer_score_label =Label(root, text="Opponent Score: ")
computer_score_label.place(x=100 , y=90)
computer_score_display =Label(root, textvariable=computer_score)
computer_score_display.place(x=140 , y=110)

result_label =Label(root, text="")
result_label.place(x=85 , y=130)

rock_button =Button(root, text="Rock", command=lambda: handle_choice("rock"))
paper_button = Button(root, text="Paper", command=lambda: handle_choice("paper"))
scissors_button =Button(root, text="Scissors", command=lambda: handle_choice("scissors"))

rock_button.place(x=129 , y=190)
paper_button.place(x=127 , y=220)
scissors_button.place(x=121 , y=250)

def reset_scores():
    user_score.set(0)
    computer_score.set(0)

reset_button =Button(root, text="Reset Scores", command=reset_scores)
reset_button.place(x=108 , y=290)

root.mainloop()