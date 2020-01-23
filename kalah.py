class Kalah:

    def __init__(self, holes, seeds):
        self.current_player = 0
        self.board = [0 if i == holes or i == 2*holes + 1 else seeds for i in range((holes + 1) * 2)]

    def status(self):
        return tuple(self.board)

    def play(self, hole):
        if self.current_player == 0 and len(self.board)/2-1 < hole < len(self.board)-1:
            raise IndexError
            # return "Hole number too large"
        if self.current_player == 1 and 0 <= hole < len(self.board)/2-1:
            raise IndexError
            # return "Hole number too small"
        start = hole+1
        end = start + self.board[hole]
        self.board[hole] = 0
        for i in range(start, end):
            self.board[i] += 1
