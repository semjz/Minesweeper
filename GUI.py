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
        self.configWindow(self.window, self.width, self.height)
        self.createAllImages()
        self.createTopBar(self.window)
        self.resetButton = self.createResetButton(self.window)
        self.flagCounter = self.createFlagCounter(self.window)
        self.timer = self.createTimer(self.window)
        self.cells = [[None] * self.cols for _ in range(self.rows)]
        self.createButtons(self.window)


    def configWindow(self, window, width, height):
        ws = window.winfo_screenwidth() #screen width
        hs = window.winfo_screenheight() #screen height
        # coords which put the window in the center of screen
        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)
        window.geometry(("%dx%d+%d+%d") % (width, height, x, y)) #window size

    def createTopBar(self, window):
        topBar = Canvas(window, bg="grey", width = self.width, height = 35)
        topBar.grid(row = 0, column = 0, columnspan = 20)
        window.grid_rowconfigure(0, weight = 1)

    def createFlagCounter(self, window):
        flag_counter = Label(window, bg="grey", text = "0", fg = "blue", font=("Arial", 17))
        flag_counter.place(x = 0, y = 2)
        window.update()
        print(WIDTH / 4 - flag_counter.winfo_width() / 2)
        flag_counter.place(x = WIDTH / 4 - flag_counter.winfo_width() / 2, y = 2)
        return flag_counter

    def createTimer(self, window):
        timer = Label(window, bg="grey", text = "0", fg = "blue", font=("Arial", 17))
        timer.place(x = 0, y = 2)
        window.update()
        print(timer.winfo_width())
        timer.place(x = WIDTH * 3 / 4 - timer.winfo_width() / 2, y = 2)
        return timer

    def createButtons(self, window):
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col] = Label(window, image = self.images["button.png"]
                                            , disabledforeground = "black")
                self.cells[row][col].grid(row = row + 1, column = col)
                window.grid_columnconfigure(col, weight = 1)
                window.grid_rowconfigure(row + 1, weight = 1)

    def createResetButton(self, window):
        resetButton = Button(window, image = self.images["smilyFace"],bd = 1)
        resetButton.place(x = WIDTH / 2 - CELL_SIZE / 2, y = (30 - CELL_SIZE) / 2)
        return resetButton

    
    def createAllImages(self):
        self.images["button.png"] = createImage("button.png", self.img_width, self.img_height)
        self.images["smilyFace"] = createImage("smilyFace.png", self.img_width, self.img_height)
        self.images["wonderFace"] = createImage("wonderFace.png", self.img_width, self.img_height)
        self.images["deadFace"] = createImage("deadFace.png", self.img_width, self.img_height)
        self.images["win_face"] = createImage("win_face.png", self.img_width, self.img_height)
        self.images["mine"] = createImage("mine.png", self.img_width, self.img_height)
        self.images["red_mine"] = createImage("red_mine.png", self.img_width, self.img_height)
        self.images["buttonPressed"] = createImage("0.png", self.img_width, self.img_height)  
        self.images["one"] = createImage("1.png", self.img_width, self.img_height)  
        self.images["two"] = createImage("2.png", self.img_width, self.img_height)  
        self.images["three"] = createImage("3.png", self.img_width, self.img_height)  
        self.images["four"] = createImage("4.png", self.img_width, self.img_height)  
        self.images["five"] = createImage("5.png", self.img_width, self.img_height)  
        self.images["six"] = createImage("6.png", self.img_width, self.img_height)  
        self.images["seven"] = createImage("7.png", self.img_width, self.img_height)  
        self.images["eight"] = createImage("8.png", self.img_width, self.img_height)
        self.images["flag"] = createImage("flag.png", self.img_width, self.img_height)
        self.images["wrong_flag"] = createImage("wrong_flag.png", self.img_width, self.img_height)
    

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
