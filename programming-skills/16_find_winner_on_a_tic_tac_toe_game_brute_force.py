class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        board = [[0] * n for _ in range(n)]

        def checkRow(row, player_id):
            for col in range(n):
                if board[row][col] != player_id:
                    return False
            return True

        def checkCol(col, player_id):
            for row in range(n):
                if board[row][col] != player_id:
                    return False
            return True
        
        def checkDiagonal(player_id):
            for row in range(n):
                if board[row][row] != player_id:
                    return False
            return True

        def checkAntiDiagonal(player_id):
            for row in range(n):
                if board[row][n - 1 - row] != player_id:
                    return False
            return True

        player = 1

        for move in moves:
            row, col = move
            board[row][col] = player

            if checkRow(row, player) or checkCol(col, player) or (row == col and checkDiagonal(player)) or (row + col == n - 1 and checkAntiDiagonal(player)):
                return "A" if player == 1 else "B"

            player *= -1

        return "Draw" if len(moves) == n * n else "Pending"