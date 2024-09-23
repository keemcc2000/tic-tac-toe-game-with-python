import tkinter

class TicTacToe:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.resizable(False, False)

        self.playerX = 'X'
        self.playerO = 'O'
        self.current_player = self.playerX
        self.turn = 0
        self.game_over = False

        self.colors = {
            "background": "#2C3E50",  # Dark blue-gray
            "text": "#ECF0F1",        # Light gray
            "accent1": "#3498DB",     # Bright blue
            "accent2": "#E74C3C",     # Bright red
            "highlight": "#F1C40F"    # Yellow
        }

        self.board = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_widgets()
        self.center_window()

    def create_widgets(self):
        self.frame = tkinter.Frame(self.window, bg=self.colors["background"])
        self.label = tkinter.Label(self.frame, text=f"{self.current_player}'s turn", font=("Arial", 20),
                              bg=self.colors["background"], fg=self.colors["text"])
        self.label.grid(row=0, column=0, columnspan=3, sticky="we")

        for row in range(3):
            for col in range(3):
                self.board[row][col] = tkinter.Button(self.frame, text="", font=("Arial", 50, "bold"),
                                                 bg=self.colors["background"], fg=self.colors["accent1"],
                                                 width=4, height=1,
                                                 command=lambda r=row, c=col: self.set_tile(r, c))
                self.board[row][col].grid(row=row+1, column=col)

        self.restart_button = tkinter.Button(self.frame, text="Restart", font=("Arial", 20),
                                        bg=self.colors["background"], fg=self.colors["text"], command=self.new_game)
        self.restart_button.grid(row=4, column=0, columnspan=3, sticky="we")

        self.frame.pack()

    def set_tile(self, row, column):
        if self.board[row][column]["text"] != "" or self.game_over:
            return

        self.board[row][column]["text"] = self.current_player
        self.board[row][column]["fg"] = self.colors["accent1"] if self.current_player == self.playerX else self.colors["accent2"]
        self.turn += 1

        self.current_player = self.playerO if self.current_player == self.playerX else self.playerX
        self.label["text"] = f"{self.current_player}'s turn"

        self.check_winner()

    def check_winner(self):
        winning_combinations = (
            [[(r, c) for c in range(3)] for r in range(3)] +  # Rows
            [[(r, c) for r in range(3)] for c in range(3)] +  # Columns
            [[(i, i) for i in range(3)]] +  # Diagonal
            [[(i, 2-i) for i in range(3)]]  # Anti-diagonal
        )

        for combo in winning_combinations:
            if self.board[combo[0][0]][combo[0][1]]["text"] == \
               self.board[combo[1][0]][combo[1][1]]["text"] == \
               self.board[combo[2][0]][combo[2][1]]["text"] != "":
                self.end_game(f"{self.board[combo[0][0]][combo[0][1]]['text']} is the winner!", combo)
                return

        if self.turn == 9:
            self.end_game("Tie!")

    def end_game(self, message, winning_combo=None):
        self.game_over = True
        self.label.config(text=message, fg=self.colors["highlight"])
        
        if winning_combo:
            for row, col in winning_combo:
                self.board[row][col].config(fg=self.colors["highlight"], bg=self.colors["text"])
        else:
            for row in range(3):
                for col in range(3):
                    self.board[row][col].config(bg=self.colors["text"])

    def new_game(self):
        self.turn = 0
        self.game_over = False
        self.current_player = self.playerX
        self.label.config(text=f"{self.current_player}'s turn", fg="white")

        for row in range(3):
            for col in range(3):
                self.board[row][col]["text"] = ""
                self.board[row][col]["fg"] = self.colors["accent1"]
                self.board[row][col]["bg"] = self.colors["background"]

    def center_window(self):
        self.window.update()
        window_width = self.window.winfo_width()
        window_height = self.window.winfo_height()
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        window_x = int((screen_width - window_width) / 2)
        window_y = int((screen_height - window_height) / 2)

        self.window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()