import tkinter as tk
from tkinter import messagebox
import random

def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose {computer_choice}.\n{result}")

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Paper' and computer == 'Rock') or \
         (user == 'Scissors' and computer == 'Paper'):
        return "You win!"
    else:
        return "You lose!"

app = tk.Tk()
app.title("Rock-Paper-Scissors")

tk.Label(app, text="Choose your move:").pack()

tk.Button(app, text="Rock", command=lambda: play('Rock')).pack()
tk.Button(app, text="Paper", command=lambda: play('Paper')).pack()
tk.Button(app, text="Scissors", command=lambda: play('Scissors')).pack()

app.mainloop()