class Cell_backend:
    def __init__(self):
        self.label = None
        self.is_visited = False
        self.is_flag = False
        self.is_mine = False
        self.no_of_sur_mines = 0

    def get_is_visited(self):
        return self.is_visited

    def get_is_flag(self):
        return self.is_flag

    def get_is_mine(self):
        return self.is_mine

    def get_no_of_sur_mines(self):
        return self.no_of_sur_mines

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def set_is_visited(self, bol):
        self.is_visited = bol

    def set_is_flag(self, bol):
        self.is_flag = bol

    def set_is_mine(self, bol):
        self.is_mine = bol

    def set_no_of_sur_mines(self, no_of_sur_mines):
        self.no_of_sur_mines = no_of_sur_mines




