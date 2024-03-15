from TuringMachine import TuringMachine, States
from ActionTable import ActionTable
from Action import Action, Move

turing_machine = TuringMachine(list(input()),
                               ActionTable(
                                   {
                                       States.Q0:
                                           {
                                               '0': Action('0', Move.R, States.Q0),
                                               '1': Action('1', Move.R, States.Q0),
                                               '2': Action('2', Move.R, States.Q0),
                                               '+': Action('+', Move.R, States.Q1),
                                               '-': Action('-', Move.R, States.Q2),
                                               ' ': Action(' ', Move.R, States.Q0)
                                           },
                                       States.Q1:
                                           {
                                               '0': Action('0', Move.N, States.Qt),
                                               '1': Action('1', Move.L, States.Q3),
                                               '2': Action('2', Move.L, States.Q4),
                                               ' ': Action(' ', Move.R, States.Q1)
                                           },
                                       States.Q2:
                                           {
                                               '0': Action('0', Move.N, States.Qt),
                                               '1': Action('1', Move.L, States.Q5),
                                               '2': Action('2', Move.L, States.Q6),
                                               ' ': Action(' ', Move.R, States.Q2)
                                           },
                                       States.Q3:
                                           {
                                               '0': Action('1', Move.N, States.Qt),
                                               '1': Action('2', Move.N, States.Qt),
                                               '2': Action('0', Move.L, States.Q7),
                                               '+': Action('+', Move.L, States.Q3),
                                               '-': Action('-', Move.L, States.Q3),
                                               ' ': Action(' ', Move.L, States.Q3)
                                           },
                                       States.Q4:
                                           {
                                               '0': Action('2', Move.N, States.Qt),
                                               '1': Action('0', Move.L, States.Q7),
                                               '2': Action('1', Move.L, States.Q7),
                                               '+': Action('+', Move.L, States.Q4),
                                               '-': Action('-', Move.L, States.Q4),
                                               ' ': Action(' ', Move.L, States.Q4)
                                           },
                                       States.Q5:
                                           {
                                               '0': Action('2', Move.L, States.Q5),
                                               '1': Action('0', Move.N, States.Qt),
                                               '2': Action('1', Move.N, States.Qt),
                                               '+': Action('+', Move.L, States.Q5),
                                               '-': Action('-', Move.L, States.Q5),
                                               ' ': Action(' ', Move.L, States.Q5)
                                           },
                                       States.Q6:
                                           {
                                               '0': Action('1', Move.L, States.Q5),
                                               '1': Action('2', Move.L, States.Q5),
                                               '2': Action('0', Move.N, States.Qt),
                                               '+': Action('+', Move.L, States.Q6),
                                               '-': Action('-', Move.L, States.Q6),
                                               ' ': Action(' ', Move.L, States.Q6)
                                           },
                                       States.Q7:
                                           {
                                               '0': Action('1', Move.N, States.Qt),
                                               '1': Action('2', Move.N, States.Qt),
                                               '2': Action('0', Move.L, States.Q7),
                                               ' ': Action('1', Move.N, States.Qt)
                                           }
                                   }))

turing_machine.process()
turing_machine.print_tape()
