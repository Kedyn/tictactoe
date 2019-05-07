from .piece import PIECE


class AI:
    def __init__(self, piece):
        self.piece = piece

        if piece == PIECE.X:
            self.opponents_piece = PIECE.O
        else:
            self.opponents_piece = PIECE.X

    def move(self, board):
        best = self.minimax(board, len(self.getEmptyIndexies(board)), True)
        print(self.getEmptyIndexies(board))
        print(board)
        if best[1] != -1:
            board[best[1]] = self.piece

        return board

    def minimax(self, board, depth, maximize):
        empty_indices = self.getEmptyIndexies(board)

        if len(empty_indices) == 0 or self.getBoardScoreForPiece(board) != 0 or depth == 0:
            return [self.getBoardScoreForPiece(board), -1]

        if maximize:
            best = [-9, -1]

            for cell in empty_indices:
                board[cell] = self.piece

                value = self.minimax(board, depth - 1, False)

                if value[0] > best[0]:
                    best[0] = value[0]

                    best[1] = cell

                board[cell] = PIECE.NONE

            return best
        else:
            worst = [9, -1]

            for cell in empty_indices:
                board[cell] = self.opponents_piece

                value = self.minimax(board, depth - 1, True)

                if value[0] < worst[0]:
                    worst[0] = value[0]

                    worst[1] = cell

                board[cell] = PIECE.NONE

            return worst

    def getEmptyIndexies(self, board):
        return [item for item, piece in enumerate(board) if piece == PIECE.NONE]

    def getBoardScoreForPiece(self, board):
        winner = self.getWinner(board)

        if self.piece == winner:
            return 7
        elif self.opponents_piece == winner:
            return -7
        return 0

    def getWinner(self, board):
        if board[0] == board[1] and board[1] == board[2] and board[0] != PIECE.NONE:
            return board[0]
        elif board[0] == board[3] and board[3] == board[6] and board[0] != PIECE.NONE:
            return board[0]
        elif board[0] == board[4] and board[4] == board[8] and board[0] != PIECE.NONE:
            return board[0]
        elif board[1] == board[4] and board[4] == board[7] and board[1] != PIECE.NONE:
            return board[1]
        elif board[2] == board[4] and board[4] == board[6] and board[2] != PIECE.NONE:
            return board[2]
        elif board[2] == board[5] and board[5] == board[8] and board[2] != PIECE.NONE:
            return board[2]
        elif board[3] == board[4] and board[4] == board[5] and board[3] != PIECE.NONE:
            return board[3]
        elif board[6] == board[7] and board[7] == board[8] and board[6] != PIECE.NONE:
            return board[6]

        return PIECE.NONE
