import tkinter as tk
from tkinter import messagebox

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    if any(' ' in row for row in board):
        return None
    return 'Tie'

def minimax(board, depth, is_max):
    if check_winner(board) == 'X':
        return -1
    if check_winner(board) == 'O':
        return 1
    if check_winner(board) == 'Tie':
        return 0

    if is_max:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    max_eval = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                eval = minimax(board, 0, False)
                board[i][j] = ' '
                if eval > max_eval:
                    max_eval = eval
                    move = (i, j)
    return move

def make_move(i, j):
    if board[i][j] == ' ':
        buttons[i][j].config(text='X', state='disabled')
        board[i][j] = 'X'
        if check_winner(board) is None:
            move = best_move(board)
            if move is not None:
                i, j = move
                buttons[i][j].config(text='O', state='disabled')
                board[i][j] = 'O'
            if check_winner(board) == 'O':
                messagebox.showinfo("Game Over", "You lose!")
            elif check_winner(board) == 'Tie':
                messagebox.showinfo("Game Over", "It's a tie!")
        else:
            if check_winner(board) == 'X':
                messagebox.showinfo("Game Over", "You win!")
            elif check_winner(board) == 'Tie':
                messagebox.showinfo("Game Over", "It's a tie!")

def restart_game():
    global board
    board = create_board()
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ', state='normal')

root = tk.Tk()
root.title("Unbeatable Tic-Tac-Toe")

buttons = [[None, None, None] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', font=('normal', 20), width=5, height=2,
                                  command=lambda i=i, j=j: make_move(i, j))
        buttons[i][j].grid(row=i, column=j)

restart_button = tk.Button(root, text='Restart', font=('normal', 15), command=restart_game)
restart_button.grid(row=3, column=0, columnspan=3)

board = create_board()

root.mainloop()

