from .piece import PIECE


class AI:
    def __init__(self, piece):
        self.piece = piece

        if piece == PIECE.X:
            self.opponents_piece = PIECE.O
        else:
            self.opponents_piece = PIECE.X

    def move(self, board):
        best = [-9, -1]

        for piece in self.getEmptyIndexies(board):
            board[piece] = self.piece

            value = self.minimax(board, False)

            board[piece] = PIECE.NONE

            if value[0] > best[0]:
                best = [value[0], piece]

        if best[1] != -1:
            board[best[1]] = self.piece

        return board

    def minimax(self, board, maximize):
        empty_indexies = self.getEmptyIndexies(board)

        if len(empty_indexies) == 0:
            return [self.getBoardScoreForPiece(board, self.piece), board]

        if maximize:
            best = [-9, board]

            for piece in empty_indexies:
                new_board = board.copy()
                new_board[piece] = self.piece
                value = self.minimax(new_board, False)

                if value[0] > best[0]:
                    best = value

            return best
        else:
            worst = [9, board]

            for piece in empty_indexies:
                new_board = board.copy()
                new_board[piece] = self.opponents_piece
                value = self.minimax(new_board, True)

                if value[0] < worst[0]:
                    worst = value

            return worst

    def getEmptyIndexies(self, board):
        return [item for item, piece in enumerate(board) if piece == PIECE.NONE]

    def getBoardScoreForPiece(self, board, piece):
        winner = self.getWinner(board)

        if piece == winner:
            return 7
        elif PIECE.NONE == winner:
            return 0
        return -7

    def getWinner(self, board):
        if board[0] == board[1] and board[1] == board[2]:
            return board[0]
        elif board[0] == board[3] and board[3] == board[6]:
            return board[0]
        elif board[0] == board[4] and board[4] == board[8]:
            return board[0]
        elif board[1] == board[4] and board[4] == board[7]:
            return board[1]
        elif board[2] == board[4] and board[4] == board[6]:
            return board[2]
        elif board[2] == board[5] and board[5] == board[8]:
            return board[2]
        elif board[3] == board[4] and board[4] == board[5]:
            return board[3]
        elif board[6] == board[7] and board[7] == board[8]:
            return board[6]
