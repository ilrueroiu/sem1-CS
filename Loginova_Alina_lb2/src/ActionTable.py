class ActionTable:

    def __init__(self, table):
        self.table = table

    def get_action(self, state, value):
        return self.table[state][value]
