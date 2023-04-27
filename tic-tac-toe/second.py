import tkinter as tk


# A class to represent the Tic Tac Toe game board
class TicTacToe:
    def __init__(self):
        self.board = ['-'] * 9
        self.human_marker = 'X'
        self.computer_marker = 'O'

    # Check if the game board is full
    def is_board_full(self):
        return '-' not in self.board

    # Check if the game is over
    def is_game_over(self):
        return self.is_board_full() or self.check_winner(self.human_marker) or self.check_winner(self.computer_marker)

    # Check if the given marker has won the game
    def check_winner(self, marker):
        return ((self.board[0] == marker and self.board[1] == marker and self.board[2] == marker) or
                (self.board[3] == marker and self.board[4] == marker and self.board[5] == marker) or
                (self.board[6] == marker and self.board[7] == marker and self.board[8] == marker) or
                (self.board[0] == marker and self.board[3] == marker and self.board[6] == marker) or
                (self.board[1] == marker and self.board[4] == marker and self.board[7] == marker) or
                (self.board[2] == marker and self.board[5] == marker and self.board[8] == marker) or
                (self.board[0] == marker and self.board[4] == marker and self.board[8] == marker) or
                (self.board[2] == marker and self.board[4] == marker and self.board[6] == marker))

    # Make the given move on the game board
    def make_move(self, position, marker):
        self.board[position] = marker


# Create a Tkinter GUI for the Tic Tac Toe game
class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.board = TicTacToe()
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=("Helvetica", 20), width=3, height=1,
                               command=lambda position=i: self.play_turn(position))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)
        self.status = tk.Label(self.root, text="", font=("Helvetica", 20))
        self.status.grid(row=3, column=0, columnspan=3)

    # Get the symbolic representation of the given marker
    def get_symbol(self, marker):
        if marker == self.board.human_marker:
            return "X"
        elif marker == self.board.computer_marker:
            return "O"
        else:
            return " "

    # Display the current state of the game board
    def display_board(self):
        for i in range(9):
            self.buttons[i].config(text=self.get_symbol(self.board.board[i]))

    # Reset the game board and status message
    def reset_board(self):
        self.board = TicTacToe()
        self.status.config(text="")
        self.display_board()

    # Play the human player's turn and update the game board and status message
    def play_turn(self, position):
        if self.board.board[position] == "-":
            self.board.make_move(position, self.board.human_marker)
            self.display_board()
            if self.board.is_game_over():
                self.end_game()
                return
            self.status.config(text="Computer is thinking...")
            self.root.after(1000, self.play_computer_turn)

    # Play the computer player's turn and update the game board and status message
    def play_computer_turn(self):
        position = self.board.get_computer_move()
        self.board.make_move(position, self.board.computer_marker)
        self.display_board()
        if self.board.is_game_over():
            self.end_game()
            return
        self.status.config(text="")

    # End the game and display the winner or tie message
    def end_game(self):
        if self.board.check_winner(self.board.human_marker):
            self.status.config(text="You win!")
        elif self.board.check_winner(self.board.computer_marker):
            self.status.config(text="Computer wins!")
        else:
            self.status.config(text="It's a tie!")
        self.root.after(1000, self.reset_board)


# Create and run the GUI object
if __name__ == '__main__':
    gui = TicTacToeGUI()
    gui.root.mainloop()