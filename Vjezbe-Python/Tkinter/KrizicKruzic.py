
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Krizic Kruzic")
root.resizable(False, False)

mainframe = ttk.Frame(root, padding="20 20 20 20")
mainframe.grid(row=0, column=0, sticky="NSEW")

title_label = ttk.Label(mainframe, text="Krizic-Kruzic", font=("Segoe UI", 24, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

board_frame = ttk.Frame(mainframe)
board_frame.grid(row=1, column=0, columnspan=3)

# Style for the buttons
style = ttk.Style()
style.configure("TicTacToe.TButton", font=("Segoe UI", 25, "bold"))

buttons = [[None for _ in range(3)] for _ in range(3)]
current_player = ["X"]
game_over = [False]

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] != "" and all(buttons[i][j]["text"] == buttons[i][0]["text"] for j in range(3)):
            return buttons[i][0]["text"]
        if buttons[0][i]["text"] != "" and all(buttons[j][i]["text"] == buttons[0][i]["text"] for j in range(3)):
            return buttons[0][i]["text"]
    if buttons[0][0]["text"] != "" and all(buttons[d][d]["text"] == buttons[0][0]["text"] for d in range(3)):
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] != "" and all(buttons[d][2-d]["text"] == buttons[0][2]["text"] for d in range(3)):
        return buttons[0][2]["text"]
    return None

def is_draw():
    return all(buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

def end_game(message):
    game_over[0] = True
    for row in range(3):
        for col in range(3):
            buttons[row][col].state(["disabled"])
    messagebox.showinfo("Game Over", message)

def on_button_click(row, col):
    if game_over[0]:
        return
    btn = buttons[row][col]
    if btn["text"] == "":
        btn.config(text=current_player[0])
        winner = check_winner()
        if winner:
            end_game(f"Pobjednik je: {winner}!")
        elif is_draw():
            end_game("Neriješeno!")
        else:
            current_player[0] = "O" if current_player[0] == "X" else "X"

def reset_game():
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="")
            buttons[row][col].state(["!disabled"])
    current_player[0] = "X"
    game_over[0] = False

for row in range(3):
    for col in range(3):
        btn = ttk.Button(
            board_frame,
            text="",
            width=6,
            style="TicTacToe.TButton",
            command=lambda r=row, c=col: on_button_click(r, c)
        )
        btn.grid(row=row, column=col, padx=8, pady=8, ipadx=8, ipady=8)
        buttons[row][col] = btn

reset_button = ttk.Button(mainframe, text="Reset", command=reset_game)
reset_button.grid(row=2, column=0, columnspan=3, pady=(20, 0))

root.mainloop()
