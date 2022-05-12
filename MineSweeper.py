from faulthandler import disable
from cells_engine import Cells_engine
from gui import GUI
from constants import *

class Minesweeper():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.no_of_mines = round(0.15 * self.rows * self.cols)
        self.cell_engine = Cells_engine(self.rows, self.cols)
        self.cell_engine.createMines(self.no_of_mines)
        self.cell_engine.countSurrondingMines()
        self.gui = GUI(WIDTH, HIEGHT, self.rows, self.cols)
        self.add_command_to_buttons()

    def add_command_to_buttons(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.gui.cells[row ][col].configure(command =  lambda i = row 
										            , j = col:self.buttonClickedupdate(i,j))
                self.gui.cells[row ][col].bind("<Button-1>", self.wonder)
                self.gui.cells[row ][col].bind("<Button-3>", lambda event="<Button-3>"
                                               , cell_row = row, cell_col = col
                                               : self.flag(event, cell_row, cell_col))
        self.gui.resetButton.configure(command = self.reset)


    def buttonClickedupdate(self,i,j):
        self.cell_engine.cells[i][j].set_is_visited(True)

        if self.cell_engine.cells[i][j].get_is_mine():
            self.mineClicked()
            self.gui.cells[i][j].configure(image=self.gui.images["mine"],state="normal",command=0,relief="sunken")
            self.gui.cells[i][j].unbind("<Button-1>")
            self.gui.cells[i][j].unbind("<Button-3>")

        else:
            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 0:
                self.clearSrounding(i,j)
                self.gui.cells[i][j].configure(image=self.gui.images["buttonPressed"],state="normal",command=0,relief="sunken")
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")
                
            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 1:
                self.gui.cells[i][j].configure(image=self.gui.images["one"],state="normal",command=0,relief="sunken")
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 2:
                self.gui.cells[i][j].configure(image=self.gui.images["two"],state="normal",command=0,relief="sunken")
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 3:
                self.gui.cells[i][j].configure(image=self.gui.images["three"],state="normal",command=0,relief="sunken")
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 4:
                self.gui.cells[i][j].configure(image=self.gui.images["four"],state="normal",command=0,relief="sunken")
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 5:
                self.gui.cells[i][j].configure(image=self.gui.images["five"],state="normal",command=0,relief="sunken")
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 6:
                self.gui.cells[i][j].configure(image=self.gui.images["six"],state="normal",command=0,relief="sunken")
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 7:
                self.gui.cells[i][j].configure(image=self.gui.images["seven"],state="normal",command=0,relief="sunken")
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 8:	
                self.gui.cells[i][j].configure(image=self.gui.images["eight"],state="normal",command=0,relief="sunken")
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")
            
            if self.playerWins():
                print("wins")

    def clearSrounding(self,row, col):
        if self.cell_engine.cells[row][col].get_no_of_sur_mines() == 0 and self.playerWins():
            print("wins")
            
        if self.cell_engine.cells[row][col].get_no_of_sur_mines() == 0:
            self.cell_engine.cells[row][col].set_is_visited(True)
            self.gui.cells[row][col].configure(image=self.gui.images["buttonPressed"],state="normal",command=0,relief="sunken")
            self.gui.cells[row][col].unbind("<Button-1>")
            self.gui.cells[row][col].unbind("<Button-3>")
            neighbours = self.cell_engine.getNeighbours(row,col)
            for n in neighbours:
                a,b = n[0],n[1]
                if not self.cell_engine.cells[a][b].get_is_visited():
                    self.clearSrounding(a,b)

        else:
            return self.buttonClickedupdate(row,col)

    def playerWins(self):
        no_of_visited_tiles = 0
        for cell_list in self.cell_engine.cells:
            for cell in cell_list:
                if cell.get_is_visited():
                    no_of_visited_tiles += 1
        print(no_of_visited_tiles)
        return no_of_visited_tiles == self.rows * self.cols - self.no_of_mines

    def mineClicked(self):
        for i in range (self.rows):
            for j in range(self.cols):
                self.gui.cells[i][j].configure(state="normal",command=0,relief="sunken")
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")
                if self.cell_engine.cells[i][j].get_is_mine():
                    self.gui.cells[i][j].configure(image=self.gui.images["mine"])
        self.gui.resetButton.configure(image=self.gui.images["deadFace"])
    
    def reset_cell_engine(self):
        for cell_list in self.cell_engine.cells:
            for cell in cell_list:
                cell.set_is_visited(False)
                cell.set_is_mine(False)
                cell.set_no_of_sur_mines(0)

    def reset_cell_gui(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.gui.cells[row][col].configure(image = self.gui.images["button.png"]
                                            , command = lambda i = row
                                            , j = col:self.buttonClickedupdate(i,j)
                                            , relief="raised")
                self.gui.cells[row][col].bind("<Button-1>", self.wonder)

    def wonder(self, event):
        self.gui.resetButton.configure(image = self.gui.images["wonderFace"])
    
    def flag(self, event, cell_row, cell_col):
        event.widget.configure(image = self.gui.images["flag"])
        event.widget.configure(state="normal",command=0,relief="sunken")
        event.widget.unbind("<Button-1>")
        event.widget.unbind("<Button-3>")
        print(cell_row, cell_col)    
    
    def reset(self):
        self.reset_cell_engine()
        self.reset_cell_gui()
        self.cell_engine.createMines(self.no_of_mines)
        self.cell_engine.countSurrondingMines()
        self.gui.resetButton.configure(image=self.gui.images["smilyFace"])

    def run(self):
        self.gui.window.mainloop()