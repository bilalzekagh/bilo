class TicTacToeModel:

    def __init__(self, board):
        self._board = board

    def __str__(self):
        return f"Board data: {self._board}"

    def StoreMove(self, position, player):
        pass


# =========================
# LIST VERSION
# =========================
class TicTacToeList(TicTacToeModel):

    def __init__(self):
        board = [["","",""],
                 ["","",""],
                 ["","",""]]
        super().__init__(board)

    def StoreMove(self, position, player):
        if position >= 1 and position <= 9:
            row = (position - 1) // 3
            col = (position - 1) % 3

            if self._board[row][col] == "":
                self._board[row][col] = player
                return True
        return False


# =========================
# DICT VERSION
# =========================
class TicTacToeDict(TicTacToeModel):

    def __init__(self):
        board = {1: " ", 2: " ", 3: " ",
                 4: " ", 5: " ", 6: " ",
                 7: " ", 8: " ", 9: " "}
        super().__init__(board)

    def StoreMove(self, position, player):
        if position >= 1 and position <= 9:
            if self._board[position] == " ":
                self._board[position] = player
                return True
        return False


# =========================
# TESTING
# =========================

print("DICT VERSION TEST")
tttboardD = TicTacToeDict()

tttboardD.StoreMove(1, "X")
tttboardD.StoreMove(5, "O")
tttboardD.StoreMove(1, "O")  # should fail (already taken)

print(tttboardD)


print("\nLIST VERSION TEST")
tttboardL = TicTacToeList()

tttboardL.StoreMove(1, "X")
tttboardL.StoreMove(5, "O")
tttboardL.StoreMove(1, "O")  # should fail

print(tttboardL)