class Kalah:

    def __init__(self, holes, seeds):
        self.current_player = 0

    def status(self):
        stat = (4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0)
        return stat

    def play(self, hole_num):
        if self.current_player == 0 and 6 < hole_num < 13:
            return "Hole number too large"
        if self.current_player == 1 and 0 <= hole_num < 6:
            return "Hole number too small"
