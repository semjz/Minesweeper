from tkinter import Tk, Canvas, Button, Label
from PIL import Image, ImageTk
from constants import *


class GUI:

    def __init__(self, width, height, rows, cols):
        self.window = Tk()
        self.window.title("Minesweeper") #title of window
        self.window.resizable(width = False, height = False)
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.img_width = CELL_SIZE
        self.img_height = CELL_SIZE
        self.images = {}
        self.configWindow(self.width, self.height)
        self.createAllImages()
        self.cells_frontend = [[None] * self.cols for _ in range(self.rows)]
        self.createButtons()
        self.createTopBar()
        self.resetButton = self.createResetButton()
        self.flagCounter = self.createFlagCounter()
        self.timer = self.createTimer()
        self.update_flag_conter_pos()
        self.update_timer_pos()


    def configWindow(self, width, height):
        ws = self.window.winfo_screenwidth() #screen width
        hs = self.window.winfo_screenheight() #screen height
        # coords which put the window in the center of screen
        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)
        self.window.geometry(("%dx%d+%d+%d") % (width, height, x, y)) #window size

    def createTopBar(self):
        topBar = Canvas(self.window, bg="grey", width = self.width, height = 35)
        topBar.grid(row = 0, column = 0, columnspan = 20)
        self.window.grid_rowconfigure(0, weight = 1)

    def createFlagCounter(self):
        flag_counter = Label(self.window, bg="grey", text = "10", fg = "blue", font=("Arial", 17))
        flag_counter.place(x = WIDTH / 4 , y = 2)
        self.window.update()
        flag_counter.place(x = WIDTH / 4 - flag_counter.winfo_width() / 2, y = 2)
        return flag_counter

    def createTimer(self):
        timer = Label(self.window, bg="grey", text = "0", fg = "blue", font=("Arial", 17))
        timer.place(x = WIDTH * 3 / 4, y = 2)
        self.window.update()
        timer.place(x = WIDTH * 3 / 4 - timer.winfo_width() / 2, y = 2)
        return timer

    def update_timer_pos(self):
        self.window.update()
        self.timer.place(x = WIDTH * 3 / 4 - self.timer.winfo_width() / 2, y = 2)
        self.timer.after(1000, self.update_timer_pos)

    def update_flag_conter_pos(self):
        self.window.update()
        self.flagCounter.place(x = WIDTH  / 4 - self.flagCounter.winfo_width() / 2, y = 2)
        self.flagCounter.after(1000, self.update_flag_conter_pos)

    def createButtons(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells_frontend[row][col] = Label(self.window, image = self.images["button.png"]
                                                      , disabledforeground = "black")
                self.cells_frontend[row][col].grid(row = row + 1, column = col)
                self.window.grid_columnconfigure(col, weight = 1)
                self.window.grid_rowconfigure(row + 1, weight = 1)

    def createResetButton(self):
        resetButton = Button(self.window, image = self.images["smilyFace"],bd = 1)
        resetButton.place(x = WIDTH / 2 - CELL_SIZE / 2 - 2, y = (30 - CELL_SIZE + 2) / 2)
        return resetButton

    
    def createAllImages(self):
        self.images["button.png"] = createImage("img\\button.png", self.img_width, self.img_height)
        self.images["smilyFace"] = createImage("img\\smilyFace.png", self.img_width, self.img_height)
        self.images["wonderFace"] = createImage("img\\wonderFace.png", self.img_width, self.img_height)
        self.images["deadFace"] = createImage("img\\deadFace.png", self.img_width, self.img_height)
        self.images["win_face"] = createImage("img\\win_face.png", self.img_width, self.img_height)
        self.images["mine"] = createImage("img\\mine.png", self.img_width, self.img_height)
        self.images["red_mine"] = createImage("img\\red_mine.png", self.img_width, self.img_height)
        self.images["buttonPressed"] = createImage("img\\0.png", self.img_width, self.img_height)  
        self.images["one"] = createImage("img\\1.png", self.img_width, self.img_height)  
        self.images["two"] = createImage("img\\2.png", self.img_width, self.img_height)  
        self.images["three"] = createImage("img\\3.png", self.img_width, self.img_height)  
        self.images["four"] = createImage("img\\4.png", self.img_width, self.img_height)  
        self.images["five"] = createImage("img\\5.png", self.img_width, self.img_height)  
        self.images["six"] = createImage("img\\6.png", self.img_width, self.img_height)  
        self.images["seven"] = createImage("img\\7.png", self.img_width, self.img_height)  
        self.images["eight"] = createImage("img\\8.png", self.img_width, self.img_height)
        self.images["flag"] = createImage("img\\flag.png", self.img_width, self.img_height)
        self.images["wrong_flag"] = createImage("img\\wrong_flag.png", self.img_width, self.img_height)
    

def calc_mid_col(cols):
    if cols % 2 == 0:
        return cols // 2 - 1
    else:
        return cols // 2 
        

def createImage(image_path, width, height):
    img = Image.open(image_path).resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)



"""before using ImageTk.PhotoImage Tk() must be invoked and it can only be 
   invoked once otherwise program won't work"""
