from cells_engine import Cells_engine
from gui import GUI
from constants import *

class Minesweeper():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self._time_updater = None
        self._is_first_click = True
        self.no_of_mines = round(0.15 * self.rows * self.cols)
        self.no_of_flags_left = self.no_of_mines
        self._seconds_elapsed = 0
        self.mine_is_clicked = False
        self.cell_engine = Cells_engine(self.rows, self.cols)
        self.cell_engine.create_mines(self.no_of_mines)
        self.cell_engine.count_surronding_mines_for_all()
        self.gui = GUI(WIDTH, HIEGHT, self.rows, self.cols)
        self.add_command_to_cells()
        self.config_no_of_flag()

    def add_command_to_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.gui.cells_frontend[row ][col].bind("<Button-1>", lambda event, i = row , j = col
                                                                      : self.update_cell_on_click(i, j))
                self.gui.cells_frontend[row ][col].bind("<Button-3>", lambda event, cell_row = row, cell_col = col
                                                                      : self.flag(event, cell_row, cell_col))
                                                         
        self.gui.resetButton.configure(command = self.reset)

    def add_mine_hint_to_cells(self, row, col):
        self.gui.cells_frontend[row ][col].bind("<Button-1>", lambda event, i = row , j = col
                                                              : self.make_cells_sunken_and_add_hint_sur_mines(i, j))

    def config_no_of_flag(self):
        self.gui.flagCounter.configure(text = self.no_of_flags_left)

    def make_cells_sunken_and_add_hint_sur_mines(self, row, col):
        neighbours_cords = self.cell_engine.get_neighbours_cords(row, col)
        for neighbour_cords in neighbours_cords:
            neighbour_i, neighbour_j = neighbour_cords[0], neighbour_cords[1]
            if self.cell_is_not_clicked(neighbour_i, neighbour_j):
                self.gui.cells_frontend[neighbour_i][neighbour_j].configure(relief = "sunken")

        self.gui.cells_frontend[row ][col].bind("<ButtonRelease-1>", lambda event, i = row , j = col
                                                                : self.hint_sur_mines(i, j))
    def hint_sur_mines(self, row, col):
            
        no_of_sur_flags = 0
        neighbours_cords = self.cell_engine.get_neighbours_cords(row, col)

        for neighbour_cords in neighbours_cords:
            neighbour_i, neighbour_j = neighbour_cords[0], neighbour_cords[1]
            if self.cell_engine.cells_backend[neighbour_i][neighbour_j].get_is_flag():
                no_of_sur_flags += 1

        if self.cell_engine.cells_backend[row][col].get_no_of_sur_mines() == no_of_sur_flags:
            for neighbour_cords in neighbours_cords:
                neighbour_i, neighbour_j = neighbour_cords[0], neighbour_cords[1]
                self.gui.cells_frontend[neighbour_i][neighbour_j].configure(relief = "flat")
                if self.cell_is_not_clicked(neighbour_i, neighbour_j):
                    self.update_cell_on_click(neighbour_i, neighbour_j)
        else:
            for neighbour_cords in neighbours_cords:
                neighbour_i, neighbour_j = neighbour_cords[0], neighbour_cords[1]
                if self.cell_is_not_clicked(neighbour_i, neighbour_j):
                    self.gui.cells_frontend[neighbour_i][neighbour_j].configure(relief = "flat")



    def cell_is_not_clicked(self, row, col):
        return not (self.cell_engine.cells_backend[row][col].get_is_visited() \
                    or self.cell_engine.cells_backend[row][col].get_is_flag())

    def update_cell_on_click(self, row, col):
        self.cell_engine.cells_backend[row][col].set_is_visited(True)

        if self._is_first_click and self.cell_engine.cells_backend[row][col].get_is_mine():
            self.cell_engine.move_mind_pos(row, col)
            self.cell_engine.reset_no_of_surronding_mines()
            self.cell_engine.count_surronding_mines_for_all()

        elif self.cell_engine.cells_backend[row][col].get_is_mine():
            self.mine_is_clicked = True
            self.gameover(row, col)

        if self._is_first_click:
            self.increment_timer()
            self._is_first_click = False
    
        if self.cell_has_no_of_sur_mines(0, row, col) and not self.cell_engine.cells_backend[row][col].get_is_mine():
            self.clear_srounding(row, col)
            self.gui.cells_frontend[row][col].configure(image=self.gui.images["buttonPressed"])
            self.unbind_all_buttons_for_cell(row, col)

        num_button_images_key = ["one", "two", "three", "four"
                                    , "five", "six", "seven", "eight"]
            
        for num in range(1,9):
            if self.cell_has_no_of_sur_mines(num, row, col) and not self.cell_engine.cells_backend[row][col].get_is_mine():
                self.gui.cells_frontend[row][col].configure(image=self.gui.images[num_button_images_key[num - 1]])
                self.add_mine_hint_to_cells(row, col)
                self.gui.cells_frontend[row][col].unbind("<Button-3>")
        
        if self.playerWins():
            self.gui.resetButton.configure(image = self.gui.images["win_face"])
            self.unbind_all_cells()


    def cell_has_no_of_sur_mines(self, num, row, col):
        return self.cell_engine.cells_backend[row][col].get_no_of_sur_mines() == num

    def unbind_all_buttons_for_cell(self, row, col):
            self.gui.cells_frontend[row][col].unbind("<Button-1>")
            self.gui.cells_frontend[row][col].unbind("<Button-3>")

    def clear_srounding(self, row, col):
        if self.cell_engine.cells_backend[row][col].get_is_flag():
            self.no_of_flags_left += 1
            self.cell_engine.cells_backend[row][col].set_is_flag(False)
            self.config_no_of_flag()

        if self.cell_has_no_of_sur_mines(0, row, col) and self.playerWins():
            self.gui.resetButton.configure(image = self.gui.images["win_face"])
            self.unbind_all_cells()
            return 
            
        if self.cell_has_no_of_sur_mines(0, row, col):
            self.cell_engine.cells_backend[row][col].set_is_visited(True)
            self.gui.cells_frontend[row][col].configure(image = self.gui.images["buttonPressed"])
            self.unbind_all_buttons_for_cell(row, col)
            neighbours_cords = self.cell_engine.get_neighbours_cords(row,col)
            for neighbour_cords in neighbours_cords:
                neighbour_i, neighbour_j = neighbour_cords[0], neighbour_cords[1]
                if not self.cell_engine.cells_backend[neighbour_i][neighbour_j].get_is_visited():
                    self.clear_srounding(neighbour_i, neighbour_j)

        else:
            return self.update_cell_on_click(row,col)

    def playerWins(self):
        for cell_list in self.cell_engine.cells_backend:
            for cell in cell_list:
                if not cell.get_is_visited() and not cell.get_is_mine():
                    return False
        return True

    def gameover(self, row, col):
        for i in range (self.rows):
            for j in range(self.cols):
                self.unbind_all_buttons_for_cell(i, j)
                if i == row and j == col:
                    self.gui.cells_frontend[i][j].configure(image = self.gui.images["red_mine"])
                
                elif self.cell_engine.cells_backend[i][j].get_is_mine() \
                    and not self.cell_engine.cells_backend[i][j].get_is_flag():
                    self.gui.cells_frontend[i][j].configure(image = self.gui.images["mine"])
                
                if not self.cell_engine.cells_backend[i][j].get_is_mine() \
                    and self.cell_engine.cells_backend[i][j].get_is_flag():
                        self.gui.cells_frontend[i][j].configure(image = self.gui.images["wrong_flag"])

        self.gui.resetButton.configure(image = self.gui.images["deadFace"])

    def unbind_all_cells(self):
        for row in range (self.rows):
            for col in range(self.cols):
                self.gui.cells_frontend[row][col].unbind("<Button-1>")
                self.gui.cells_frontend[row][col].unbind("<Button-3>")

    
    def reset_cell_engine(self):
        for cell_list in self.cell_engine.cells_backend:
            for cell in cell_list:
                cell.set_is_visited(False)
                cell.set_is_mine(False)
                cell.set_no_of_sur_mines(0)
                cell.set_is_flag(False)

    def reset_cell_gui(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.gui.cells_frontend[row][col].configure(image = self.gui.images["button.png"])
                self.gui.cells_frontend[row][col].bind("<Button-1>", lambda event, i = row , j = col
                                                                      : self.update_cell_on_click(i,j))
                self.gui.cells_frontend[row][col].bind("<Button-3>", lambda event, cell_row = row, cell_col = col
                                                                      : self.flag(event, cell_row, cell_col))
                self.gui.cells_frontend[row][col].unbind("<ButtonRelease-1>")
    
    def flag(self, event, cell_row, cell_col):
        if self._is_first_click:
            self.increment_timer()
            self._is_first_click = False
            
        if self.cell_engine.cells_backend[cell_row][cell_col].get_is_flag():
            event.widget.configure(image = self.gui.images["button.png"])
            self.gui.cells_frontend[cell_row ][cell_col].bind("<Button-1>", lambda event, i = cell_row , j = cell_col
                                                                            : self.update_cell_on_click(i, j))
            self.cell_engine.cells_backend[cell_row][cell_col].set_is_flag(False)
            self.no_of_flags_left += 1
        else:
            self.cell_engine.cells_backend[cell_row][cell_col].set_is_flag(True)
            event.widget.unbind("<Button-1>")
            event.widget.configure(image = self.gui.images["flag"])
            self.no_of_flags_left -= 1
        
        self.config_no_of_flag()

    def increment_timer(self):
        if self._seconds_elapsed <= 3600 and not self.playerWins() and not self.mine_is_clicked:
            self.gui.timer.configure(text = self._seconds_elapsed)
            self._seconds_elapsed += 1
        
        self._time_updater = self.gui.timer.after(1000, self.increment_timer)

    def reset_timer(self):
        self._seconds_elapsed = 0
        self.gui.timer.configure(text = self._seconds_elapsed)

    def reset(self):
        self._is_first_click = True
        self.mine_is_clicked = False
        self.reset_cell_engine()
        self.reset_cell_gui()
        self.cell_engine.create_mines(self.no_of_mines)
        self.cell_engine.count_surronding_mines_for_all()
        self.gui.resetButton.configure(image=self.gui.images["smilyFace"])
        self.no_of_flags_left = self.no_of_mines
        self.config_no_of_flag()
        if self._seconds_elapsed > 0:
            self.gui.timer.after_cancel(self._time_updater)
        self.reset_timer()

    def run(self):
        self.gui.window.mainloop()
        