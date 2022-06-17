from cell import Cell_backend
import random
class Cells_engine:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells_backend = self.create_cells()

    def create_cells(self):
        cells = [[None] * self.cols for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                cells[row][col] = Cell_backend()
        return cells

    def create_mines(self, no_of_mines):
        for _ in range(no_of_mines):
            row, col = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            
            while self.cells_backend[row][col].get_is_mine():
                row, col = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
            
            self.cells_backend[row][col].set_is_mine(True)

    def move_mind_pos(self, row, col):
        self.cells_backend[row][col].set_is_mine(False)
        new_row, new_col = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
        
        while self.cells_backend[new_row][new_col].get_is_mine() or (new_row == row and new_col == col):
            new_row, new_col = random.randint(0, self.rows - 1), random.randint(0, self.cols - 1)
        
        self.cells_backend[new_row][new_col].set_is_mine(True)

    def reset_no_of_surronding_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.cells_backend[row][col].get_is_mine():
                    self.cells_backend[row][col].set_no_of_sur_mines(0)

    def count_surronding_mines_for_cell(self, row, col):
        no_of_sur_mines = 0
        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                if self.cells_backend[i][j].get_is_mine():
                    no_of_sur_mines += 1
        self.cells_backend[row][col].set_no_of_sur_mines(no_of_sur_mines)

    def count_surronding_mines_for_all(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.count_surronding_mines_for_cell(row, col)

    def get_neighbours_cords(self, row, col):
        neighbours_cords = []
        for i in range(max(0, row - 1), min(self.rows, row + 2)):
            for j in range(max(0, col - 1), min(self.cols, col + 2)):
                neighbours_cords.append([i,j])
        return neighbours_cords