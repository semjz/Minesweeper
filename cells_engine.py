from cell import Cell
import random
class Cells_engine:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.cells = self.create_cells()

    def create_cells(self):
        cells = [[None] * self.cols for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                cells[row][col] = Cell()
        return cells

    def createMines(self, no_of_mines):
        for i in range(no_of_mines):
            row, col = random.randint(0, self.rows - 1),random.randint(0, self.cols - 1)
            
            while self.cells[row][col].get_is_mine():
                row, col = random.randint(0, self.rows - 1),random.randint(0, self.cols - 1)
            
            self.cells[row][col].set_is_mine(True)

    def countSurrondingMines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                no_of_sur_mines = 0
                if self.cells[row][col].get_no_of_sur_mines() == 0:
                    if 0 < row and 0 < col and self.cells[row-1][col-1].get_is_mine():
                        no_of_sur_mines += 1
                    
                    if 0 < row and self.cells[row-1][col].get_is_mine():
                        no_of_sur_mines += 1
                    
                    if 0 < row and col < self.cols - 1 and self.cells[row-1][col+1].get_is_mine():	
                        no_of_sur_mines += 1
                    
                    if 0 < col and self.cells[row][col-1].get_is_mine():
                        no_of_sur_mines += 1	
                    
                    if col < self.cols - 1 and self.cells[row][col+1].get_is_mine():	
                        no_of_sur_mines += 1
                    
                    if row < self.rows - 1 and 0 < col and self.cells[row+1][col-1].get_is_mine():
                        no_of_sur_mines += 1
                    
                    if row < self.rows - 1 and self.cells[row+1][col].get_is_mine():	
                        no_of_sur_mines += 1
                    
                    if row < self.rows - 1 and col < self.cols - 1 and self.cells[row+1][col+1].get_is_mine():	
                        no_of_sur_mines += 1
                    
                    self.cells[row][col].set_no_of_sur_mines(no_of_sur_mines)

    def getNeighbours(self, row, col):
        if row == 0 and col == 0:
            return [[1,0],[1,1],[0,1]]
        if row == 0  and col == self.cols - 1:
            return [[0,col-1],[1,col-1],[1,col]]
        if row == self.rows - 1 and col == 0:
            return [[row-1,0],[row-1,1],[row,1]]
        if row == self.rows - 1 and col == self.cols - 1:
            return [[row-1,col],[row-1,col-1],[row,col-1]]

        if row == 0:
            return [[0,col-1],[1,col-1],[1,col],[1,col+1],[0,col+1]]
        if row == self.rows - 1:
            return [[row,col-1],[row-1,col-1],[row-1,col],[row-1,col+1],[row,col+1]]		

        if col == 0:
            return [[row-1,col],[row-1,col+1],[row,col+1],[row+1,col+1],[row+1,col]]
        if col == self.cols - 1:
            return [[row-1,col],[row-1,col-1],[row,col-1],[row+1,col-1],[row+1,col]]
        
        if 0 < row < self.rows - 1 and 0 < col < self.cols - 1:
            return[[row-1,col-1],[row-1,col],[row-1,col+1],[row,col+1],[row+1,col+1]
                ,[row+1,col],[row+1,col-1],[row,col-1]]