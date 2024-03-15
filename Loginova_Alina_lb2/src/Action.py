from enum import IntEnum


class Move(IntEnum):
    L = -1,
    R = 1,
    N = 0


class Action:

    def __init__(self, new_val, move, new_state):
        self.new_val = new_val
        self.move = move
        self.new_state = new_state

