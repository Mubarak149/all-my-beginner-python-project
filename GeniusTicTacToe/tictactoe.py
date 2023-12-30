import random as rd
import math

class Tictactoe:
    def __init__(self,n_board):
        self.n_board = n_board
        self._board = [" " for _ in range(self.n_board**2)]
        self.board_squareroot = int(math.sqrt(len(self._board)))
        self._spot_letter = ["X","O"]
        self.player_spot_letter = ""
        self.computer_spot_letter = ""


    def create_board(self):
        board = [self._board[(i * self.board_squareroot): (i + 1) * self.board_squareroot] for i in range(self.board_squareroot)]
        for i in board:
            print("-----"*len(i))
            print(" | "+" | ".join(i) + " |")
        print("-----" * len(i))

    def print_board(self):
#       check if there is no letter in the board and print numbers in the board spot
        if not ("X" in self._board or "O" in self._board):
            print("use number to move your spot")
            for i in range(len(self._board)):
                self._board[i] = str(i + 1)
            self.create_board()
            self._board = [" " for _ in range(self.n_board ** 2)]
        else:
            self.create_board()

    def player_move(self,letter,ind):
#       check if there is 2 spot letter and remove the one player choose else give him one

        if self.computer_spot_letter == "":
            self.player_spot_letter = letter
            self._spot_letter.remove(letter)
            self.computer_spot_letter = self._spot_letter[0]

        ind = ind - 1
        letter = self.player_spot_letter


        try:
            if self._board[ind] == " ":
                self._board[ind] = letter

            else:
                print("the spot is not available")
                try:
                    move = int(input("Make a move again: "))
                    self.player_move(letter, move)
                except IndexError:
                    print("no available spot")
                    return
        except IndexError:
            print("invalid spot number!")
            move = int(input("Make a move again: "))
            self.player_move(letter, move)

    def computer_move(self):
#       computer move, choosing from 0 to number of element in the board
        ind = rd.randint(0,len(self._board)-1)
#       giving a computer spot letter if its empty
        if self.computer_spot_letter == "":
            self.computer_spot_letter = self._spot_letter[rd.randint(0,1)]
            self._spot_letter.remove(self.computer_spot_letter)
            self.player_spot_letter = self._spot_letter[0]

        if self._board[ind] == " ":
            self._board[ind] = self.computer_spot_letter
        else:
            try:
                self.computer_move()
            except RecursionError:
                print("Computer Say:","no available spot")
                return

    def genius_computer_move(self):
        best_score = -10
        best_move = 0
        for ind, elm in enumerate(self._board):
            if self._board[ind] == " ":
                self._board[ind] = self.computer_spot_letter
                score = self.minimax(False)
                self._board[ind] = " "
                if score > best_score:
                    best_score = score
                    best_move =  ind
        self._board[best_move] = self.computer_spot_letter

    def minimax(self,is_maximizing):
        self.print_board()
        if self.check_winner(self.computer_spot_letter):
            return 1
        elif self.check_winner(self.player_spot_letter):
            return -1
        elif self.check_draw():
            return 0
        if is_maximizing:
            best_score = -10
            for ind, elm in enumerate(self._board):
                if self._board[ind] == " ":
                    self._board[ind] = self.computer_spot_letter
                    score = self.minimax(False)
                    self._board[ind] = " "
                    if score > best_score:
                        best_score = score
            return best_score
        else:
            best_score = 10
            for ind, elm in enumerate(self._board):
                if self._board[ind] == " ":
                    self._board[ind] = self.player_spot_letter
                    score = self.minimax(True)
                    self._board[ind] = " "
                    if score < best_score:
                        best_score = score
            return best_score

    def check_winner(self,letter):
        lenght_row = self.n_board # length of row can be 2, 3, 4, 5 depending on the given number from user
        lenght_col = self.n_board
        lenght_dig = self.n_board # they all contain the same value is just for simplicity
        rows = [self._board[(i * lenght_row): (i + 1) * lenght_row] for i in range(lenght_row)]
        columns = [self._board[n::lenght_col] for n in range(lenght_col)]
#   to take right hand diag ind must start from 0 to end of elm to take left ind must start from last elm in a row
        diagonals = [self._board[n * (lenght_dig-1)::lenght_col+(1-(n*2))] for n in range(2)]
        diagonals[1].pop() # last elm is bug thats why i remove it
#       iterating each list of row to see whether all the value inside it are the same
        for row in rows:
            filtered_row = list(filter(lambda elm:elm == letter,row))
            if len(filtered_row) == lenght_row:
                return letter
        for col in columns:
            filtered_col = list(filter(lambda elm:elm == letter,col))
            if len(filtered_col) ==  lenght_col:
                return letter
        for diag in diagonals:
            filtered_diag = list(filter(lambda elm: elm == letter, diag))
            if len(filtered_diag) >= lenght_dig:
                return letter

        return None

    def check_draw(self):
        if " " not in self._board:
            return "Tie"

t = Tictactoe(3)

t.print_board()
while True:
    move = int(input("Move: "))
    t.player_move("X",move)
    t.print_board()
    if t.check_winner("X") == "X":
        print("you win")
        break
    t.genius_computer_move()
    t.print_board()
    if t.check_winner(t.computer_spot_letter) == t.computer_spot_letter:
        print("you loose")
        break
    if t.check_draw() == "Tie":
        print("Draw")
        break