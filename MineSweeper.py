from faulthandler import disable
from cells_engine import Cells_engine
from gui import GUI
from constants import *

class Minesweeper():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.no_of_mines = round(0.15 * self.rows * self.cols)
        self.no_of_flags_left = self.no_of_mines
        self.seconds_elapsed = 0
        self.mine_is_cliced = False
        self.cell_engine = Cells_engine(self.rows, self.cols)
        self.cell_engine.createMines(self.no_of_mines)
        self.cell_engine.countSurrondingMines()
        self.gui = GUI(WIDTH, HIEGHT, self.rows, self.cols)
        self.add_command_to_buttons()
        self.config_no_of_flag()
        self.increment_timer()

    def add_command_to_buttons(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.gui.cells[row ][col].bind("<Button-1>", lambda event="<Button-1>",i = row , j = col
                                                            :self.buttonClickedupdate(event,i,j))
                self.gui.cells[row ][col].bind("<Button-3>", lambda event="<Button-3>"
                                               , cell_row = row, cell_col = col
                                               : self.flag(event, cell_row, cell_col))
        self.gui.resetButton.configure(command = self.reset)

    def config_no_of_flag (self):
        self.gui.flagCounter.configure(text = self.no_of_flags_left)

    def buttonClickedupdate(self, event,i,j):
        self.cell_engine.cells[i][j].set_is_visited(True)

        if self.cell_engine.cells[i][j].get_is_mine():
            self.mine_is_cliced = True
            self.mineClicked(i,j)

        else:
            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 0:
                self.clearSrounding(event,i,j)
                self.gui.cells[i][j].configure(image=self.gui.images["buttonPressed"])
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")
                
            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 1:
                self.gui.cells[i][j].configure(image=self.gui.images["one"])
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 2:
                self.gui.cells[i][j].configure(image=self.gui.images["two"])
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 3:
                self.gui.cells[i][j].configure(image=self.gui.images["three"])
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 4:
                self.gui.cells[i][j].configure(image=self.gui.images["four"])
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 5:
                self.gui.cells[i][j].configure(image=self.gui.images["five"])
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 6:
                self.gui.cells[i][j].configure(image=self.gui.images["six"])
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 7:
                self.gui.cells[i][j].configure(image=self.gui.images["seven"])
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

            if self.cell_engine.cells[i][j].get_no_of_sur_mines() == 8:	
                self.gui.cells[i][j].configure(image=self.gui.images["eight"])
                self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")
            
            if self.playerWins():
                self.gui.resetButton.configure(image = self.gui.images["win_face"])
                self.unbind_all_cells()

    def clearSrounding(self,event,row, col):
        if self.cell_engine.cells[row][col].get_is_flag():
            self.no_of_flags_left += 1
            self.cell_engine.cells[row][col].set_is_flag(False)
            self.config_no_of_flag()

        if self.cell_engine.cells[row][col].get_no_of_sur_mines() == 0 and self.playerWins():
            self.gui.resetButton.configure(image = self.gui.images["win_face"])
            self.unbind_all_cells()
            
        if self.cell_engine.cells[row][col].get_no_of_sur_mines() == 0:
            self.cell_engine.cells[row][col].set_is_visited(True)
            self.gui.cells[row][col].configure(image = self.gui.images["buttonPressed"])
            self.gui.cells[row][col].unbind("<Button-1>")
            self.gui.cells[row][col].unbind("<Button-3>")
            neighbours = self.cell_engine.getNeighbours(row,col)
            for n in neighbours:
                a,b = n[0],n[1]
                if not self.cell_engine.cells[a][b].get_is_visited():
                    self.clearSrounding(event,a,b)

        else:
            return self.buttonClickedupdate(event,row,col)

    def playerWins(self):
        no_of_visited_tiles = 0
        for cell_list in self.cell_engine.cells:
            for cell in cell_list:
                if cell.get_is_visited():
                    no_of_visited_tiles += 1
        print(no_of_visited_tiles)
        return no_of_visited_tiles == self.rows * self.cols - self.no_of_mines

    def mineClicked(self, row, col):
        for i in range (self.rows):
            for j in range(self.cols):
                self.gui.cells[i][j].unbind("<Button-1>")
                self.gui.cells[i][j].unbind("<Button-3>")

                if i == row and j == col:
                    self.gui.cells[i][j].configure(image = self.gui.images["red_mine"])
                
                elif self.cell_engine.cells[i][j].get_is_mine() \
                    and not self.cell_engine.cells[i][j].get_is_flag():
                    self.gui.cells[i][j].configure(image = self.gui.images["mine"])
                
                if not self.cell_engine.cells[i][j].get_is_mine() \
                    and self.cell_engine.cells[i][j].get_is_flag():
                        self.gui.cells[i][j].configure(image = self.gui.images["wrong_flag"])

        self.gui.resetButton.configure(image = self.gui.images["deadFace"])

    def unbind_all_cells(self):
        for row in range (self.rows):
            for col in range(self.cols):
                self.gui.cells[row][col].unbind("<Button-1>")
                self.gui.cells[row][col].unbind("<Button-3>")

    
    def reset_cell_engine(self):
        for cell_list in self.cell_engine.cells:
            for cell in cell_list:
                cell.set_is_visited(False)
                cell.set_is_mine(False)
                cell.set_no_of_sur_mines(0)
                cell.set_is_flag(False)

    def reset_cell_gui(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.gui.cells[row][col].configure(image = self.gui.images["button.png"])
                self.gui.cells[row ][col].bind("<Button-1>", lambda event="<Button-1>",i = row , j = col
                                                            :self.buttonClickedupdate(event,i,j))
                self.gui.cells[row ][col].bind("<Button-3>", lambda event="<Button-3>"
                                                            , cell_row = row, cell_col = col
                                                            : self.flag(event, cell_row, cell_col))
    
    def flag(self, event, cell_row, cell_col):
        if self.cell_engine.cells[cell_row][cell_col].get_is_flag():
            event.widget.configure(image = self.gui.images["button.png"])
            self.gui.cells[cell_row ][cell_col].bind("<Button-1>", lambda event="<Button-1>",i = cell_row , j = cell_col
                                                                   :self.buttonClickedupdate(event,i,j))
            self.cell_engine.cells[cell_row][cell_col].set_is_flag(False)
            self.no_of_flags_left += 1
        else:
            self.cell_engine.cells[cell_row][cell_col].set_is_flag(True)
            event.widget.unbind("<Button-1>")
            event.widget.configure(image = self.gui.images["flag"])
            self.no_of_flags_left -= 1
        
        self.config_no_of_flag()

    def increment_timer(self):
        if self.seconds_elapsed <= 3600 and not self.playerWins() and not self.mine_is_cliced:
            self.gui.timer.configure(text = self.seconds_elapsed)
            self.seconds_elapsed += 1
        
        self.gui.timer.after(1000, self.increment_timer)

    def reset_timer(self):
        self.seconds_elapsed = 0
        self.gui.timer.configure(text = self.seconds_elapsed)

    def reset(self):
        self.mine_is_cliced = False
        self.reset_cell_engine()
        self.reset_cell_gui()
        self.cell_engine.createMines(self.no_of_mines)
        self.cell_engine.countSurrondingMines()
        self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
        self.no_of_flags_left = self.no_of_mines
        self.config_no_of_flag()
        self.reset_timer()

    def run(self):
        self.gui.window.mainloop()
        