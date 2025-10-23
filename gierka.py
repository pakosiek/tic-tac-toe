import tkinter as tk
from tkinter import messagebox

size = 3    # global variables, size is the size of our game, if it's 3 then the board is 3x3.
buttons = []    # buttons keeps track of our buttons

def button_click(Row, Column): #This function is responsible for overwriting the button with letter X when we click it
    button = buttons[Row][Column]

    if button["text"] == "": # only allow a move if the square is empty
        button["text"] = "X" 
        button.config(state=tk.DISABLED)
        x = check_if_win()
        if x == "Win":
            end_of_the_game_win()
        elif x == "Draw":
            end_of_the_game_draw()
        else:
            bot_move() # if we didn't the bot makes the move
    else:
        pass # if something goes wrong we just pass but it shouldn't happen

def check_if_win(): # function for checking if someone won, lost or drew
    hor = check_horizontally()
    ver = check_vertically()
    diag1 = check_diagonal1()
    diag2 = check_diagonal2()
    if hor == "Win" or ver =="Win" or diag1 == "Win" or diag2 == "Win":
        return "Win"
    elif hor == "Lose" or ver == "Lose" or diag1 == "Lose" or diag2 == "Lose":
        return "Lose"
    # if no one won, check for a draw
    empty = 0   
    for Row in range(size):
        for Column in range(size):
            if buttons[Row][Column]["text"] == "":
                empty += 1
    if empty == 0:
        return "Draw"
    pass

def check_horizontally(): # we check if someone won horizontally
    for Row in range(size):
        How_Many_columns_X = 0
        How_Many_columns_O = 0
        for Column in range(size):
            button = buttons[Row][Column]
            if button["text"] == "X":
                How_Many_columns_X += 1
            elif button["text"] == "O":
                How_Many_columns_O += 1 
        if How_Many_columns_X == size:
            return "Win"
        elif How_Many_columns_O == size:
            return "Lose"
        
def check_vertically(): # we check if someone won vertically
    for Column in range(size):
        How_Many_Rows_X = 0
        How_Many_Rows_O = 0
        for Row in range(size):
            button = buttons[Row][Column]
            if button["text"] == "X":
                How_Many_Rows_X += 1
            elif button["text"] == "O":
                How_Many_Rows_O += 1 
        if How_Many_Rows_X == size:
            return "Win"
        elif How_Many_Rows_O == size:
            return "Lose"

def check_diagonal1(): # we check if someone won by first diagonal
    how_many_X = 0
    how_many_O = 0
    for Row in range(size):
        button = buttons[Row][Row]
        if button["text"] == "X":
            how_many_X += 1
        elif button["text"] == "O":
            how_many_O += 1
    if how_many_X == size:
        return "Win"
    elif how_many_O == size:
        return "Lose"

def check_diagonal2(): # we check if someone won by second diagonal
    how_many_X = 0
    how_many_O = 0
    for Row in range(size):
        button = buttons[Row][(size - 1) - Row]
        if button["text"] == "X":
            how_many_X += 1
        elif button["text"] == "O":
            how_many_O += 1
    if how_many_X == size:
        return "Win"
    elif how_many_O == size:
        return "Lose"

def end_of_the_game_win():  # disables the board and shows the "You won" message
    for Row in range(size):
        for Column in range(size):
            button = buttons[Row][Column]
            button.config(state=tk.DISABLED)
    messagebox.showinfo("The end", "You won!")

def end_of_the_game_lose(): # same as win but it's if bot wins
    for Row in range(size):
        for Column in range(size):
            button = buttons[Row][Column]
            button.config(state=tk.DISABLED)
    messagebox.showinfo("The end", "You Lost!")

def end_of_the_game_draw(): # if we get "Draw" from the function check_if_win we do the same as end_of_the_game_win()
    for Row in range(size):
        for Column in range(size):
            button = buttons[Row][Column]
            button.config(state=tk.DISABLED)
    messagebox.showinfo("The end", "It's a draw!")

def bot_move(): # this funcion makes a bot do a move, and check if we lose or win
    board_state = make_a_board_for_bot()
    best_score = -float('inf')
    best_move = None
    for Row in range(size):
        for Column in range(size):
            if board_state[Row][Column] == "":
                board_state[Row][Column] = "O"
                score = minimax(board_state, False)
                board_state[Row][Column] = ""
                if score > best_score:
                    best_score = score
                    best_move = (Row, Column)
    if best_move:
        Row, Column = best_move
        button = buttons[Row][Column]
        button["text"] = "O"
        x = check_if_win()
        if x == "Lose":
            end_of_the_game_lose()
        elif x == "Draw":
            end_of_the_game_draw()


def make_a_board_for_bot(): # it makes the board for bot same as in our panel
    board_state = []
    for Row in range(size):
        row_state = []
        for Column in range(size):
            row_state.append(buttons[Row][Column]["text"])
        board_state.append(row_state)
    return board_state

def minimax(board, is_maximazing): #the main function for bot functinability, it makes the decision about where to place "O" as the bot
    result = check_board_winner(board)
    if result == "Win":
        return -10
    if result == "Lose":
        return +10
    if result == "Draw":
        return 0
    
    if is_maximazing:
        best_score = -float('inf')
        for Row in range(size):
            for Col in range(size):
                if board[Row][Col] == "":
                    board[Row][Col] = "O"
                    score = minimax(board, False)
                    board [Row][Col] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for Row in range(size):
            for Col in range(size):
                if board[Row][Col] == "":
                    board[Row][Col] = "X"
                    score = minimax(board, True)
                    board[Row][Col] = ""
                    best_score = min(score, best_score)
        return best_score
    
def check_board_winner(board): #the same function as check_if_win but for bot to know which is the best move
    hor = check_horizontally_board(board)
    ver = check_vertically_board(board)
    diag1 = check_diagonal1_board(board)
    diag2 = check_diagonal2_board(board)
    if hor == "Win" or ver =="Win" or diag1 == "Win" or diag2 == "Win":
        return "Win"
    elif hor == "Lose" or ver == "Lose" or diag1 == "Lose" or diag2 == "Lose":
        return "Lose"
    # if no one won, check for a draw
    empty = 0   
    for Row in range(size):
        for Column in range(size):
            if board[Row][Column] == "":
                empty += 1
    if empty == 0:
        return "Draw"
    pass

def check_horizontally_board(board): # we make the second part of our checks, just for a bot to know when someone wins or loses
    for Row in range(size):
        How_Many_columns_X = 0
        How_Many_columns_O = 0
        for Column in range(size):
            if board[Row][Column] == "X":
                How_Many_columns_X += 1
            elif board[Row][Column] == "O":
                How_Many_columns_O += 1 
        if How_Many_columns_X == size:
            return "Win"
        elif How_Many_columns_O == size:
            return "Lose"
        
def check_vertically_board(board):
    for Column in range(size):
        How_Many_Rows_X = 0
        How_Many_Rows_O = 0
        for Row in range(size):
            if board[Row][Column] == "X":
                How_Many_Rows_X += 1
            elif board[Row][Column] == "O":
                How_Many_Rows_O += 1 
        if How_Many_Rows_X == size:
            return "Win"
        elif How_Many_Rows_O == size:
            return "Lose"

def check_diagonal1_board(board):
    how_many_X = 0
    how_many_O = 0
    for Row in range(size):
        if board[Row][Row] == "X":
            how_many_X += 1
        elif board[Row][Row] == "O":
            how_many_O += 1
    if how_many_X == size:
        return "Win"
    elif how_many_O == size:
        return "Lose"

def check_diagonal2_board(board):
    how_many_X = 0
    how_many_O = 0
    for Row in range(size):
        if board[Row][(size - 1) - Row] == "X":
            how_many_X += 1
        elif board[Row][(size - 1) - Row] == "O":
            how_many_O += 1
    if how_many_X == size:
        return "Win"
    elif how_many_O == size:
        return "Lose"

def restart_game(): # if we click restart button this function resets all buttons
    for Row in range(size):
        for Column in range(size):
            button = buttons[Row][Column]
            button["text"] = ""
            button.config(state=tk.NORMAL)

def make_a_board(root): # this function makes a board for our game
    for Row in range(size):
        row_buttons = []
        for Column in range(size):
            button = tk.Button(root, text="", font=('Arial', 36), width=4, height=2,
                                                     command=lambda r=Row, c=Column:button_click(r,c))
            button.grid(row = Row, column = Column, padx=2, pady=2)
            row_buttons.append(button)
        buttons.append(row_buttons)

    restart_button = tk.Button(root, text="Restart", command=restart_game) 
    restart_button.grid(row=size, column=0, columnspan=size, sticky="nsew")

if __name__ == "__main__": # standard python entry point
    root = tk.Tk()
    root.title("tic tac toe")
    make_a_board(root)
    root.mainloop()
