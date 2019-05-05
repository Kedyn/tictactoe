from .piece import PIECE
import random
import time


class AI:
    def __init__(self, piece):
        self.piece = piece

        if piece == PIECE.X:
            self.opponents_piece = PIECE.O
        else:
            self.opponents_piece = PIECE.X

    def getBoardCopy(self, board):
        # Make a copy of the board list and return it.
        boardCopy = []
        for i in board:
            boardCopy.append(i)
        return boardCopy

    def move(self, board):  # makes the ai move to where it wants based  on the minimax algorithm
        move = self.getComputerMove(board, self.piece)

        # make a variable that will be known for this class
        #self.boardClone = self.getBoardCopy(board)

        board[move] = self.piece

        return board  # This function call is the one that knows what our board looks like, this MUST RETURN a list that will make that move in the board

    def isSpaceFree(self, board, move):
        # Return True if the passed move is free on the passed board.
        return board[move] == 0

    def makeMove(self, board, letter, move):
        board[move] = letter

    def getComputerMove(self, board, computerLetter):

        # Here is the algorithm for our Tic-Tac-Toe AI:
        # First, check if we can win in the next move.
        for i in range(0, 9):
            boardCopy = self.getBoardCopy(board)
            if self.isSpaceFree(boardCopy, i):
                self.makeMove(boardCopy, computerLetter, i)
                if self.isWinner(boardCopy, computerLetter):
                    return i

        # Check if the player could win on their next move and block them.
        for i in range(0, 9):
            boardCopy = self.getBoardCopy(board)
            if self.isSpaceFree(boardCopy, i):
                self.makeMove(boardCopy,  self.opponents_piece, i)
                if self.isWinner(boardCopy, self.opponents_piece):
                    return i

        # Try to take the center, if it is free.
        if self.isSpaceFree(board, 4):
            return 4

        # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(board, [0, 2, 6, 8])
        if move != None:
            return move

        # Move on one of the sides.
        return self.chooseRandomMoveFromList(board, [1, 3, 5, 7])

    def chooseRandomMoveFromList(self, board, moveList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []

        for i in moveList:
            if self.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def isWinner(self, bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use "bo" instead of "board" and "le" instead of "letter" so we don't have to type as much.

        return ((bo[0] == le and bo[1] == le and bo[2] == le) or  # Across the top
                # Across the middle
                (bo[3] == le and bo[4] == le and bo[5] == le) or
                # Across the bottom
                (bo[6] == le and bo[7] == le and bo[8] == le) or
                # Down left side
                (bo[0] == le and bo[3] == le and bo[4] == le) or
                # Down middle side
                (bo[1] == le and bo[4] == le and bo[7] == le) or
                # Down right side
                (bo[2] == le and bo[5] == le and bo[8] == le) or
                (bo[0] == le and bo[4] == le and bo[8] == le) or  # Diagonal
                (bo[2] == le and bo[4] == le and bo[6] == le))    # Diagonal
