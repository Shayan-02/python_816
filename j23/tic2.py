import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=('normal', 40), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_button_click(self, index):
        if self.board[index] == " " and self.current_player == "X":
            self.board[index] = "X"
            self.buttons[index].config(text="X")
            if self.check_winner("X"):
                messagebox.showinfo("Tic Tac Toe", "You win!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O"
                self.computer_move()

    def computer_move(self):
        available_moves = [i for i, spot in enumerate(self.board) if spot == " "]
        move = random.choice(available_moves)
        self.board[move] = "O"
        self.buttons[move].config(text="O")
        if self.check_winner("O"):
            messagebox.showinfo("Tic Tac Toe", "Computer wins!")
            self.reset_game()
        elif " " not in self.board:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            self.reset_game()
        else:
            self.current_player = "X"

    def check_winner(self, player):
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)

    def reset_game(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()