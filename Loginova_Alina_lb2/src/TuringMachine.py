from enum import Enum


class States(Enum):
    Q0 = 0,
    Q1 = 1,
    Q2 = 2,
    Q3 = 3,
    Q4 = 4,
    Q5 = 5,
    Q6 = 6,
    Q7 = 7,
    Qt = 8


class TuringMachine:

    def __init__(self, tape, table):
        self.tape = tape
        self.pointer = 0
        self.state = States.Q0
        self.table = table

    def __make_step(self):
        action = self.table.get_action(self.state, self.tape[self.pointer])
        self.tape[self.pointer] = action.new_val
        self.pointer += action.move
        self.state = action.new_state

    def __delete_zeros(self):
        for index, value in enumerate(self.tape):
            if value == '0' and self.tape[index+1] in ('0', '1', '2'):
                self.tape[index] = ' '
            elif value in ('+', '-', '1', '2'):
                return

    def process(self):
        while self.state != States.Qt:
            self.__make_step()
        self.__delete_zeros()

    def print_tape(self):
        print(''.join(self.tape))
