from tkinter import Tk, Canvas, Button
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
        topBar = Canvas(window, bg="grey", width = self.width, height = 30)
        topBar.grid(row = 0, column = 0, columnspan = 20)
        window.grid_rowconfigure(0, weight=1)

    def createButtons(self, window):
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col] = Button(window, image = self.images["button.png"])
                self.cells[row][col].grid(row = row + 1, column = col)
                window.grid_columnconfigure(col, weight = 1)
                window.grid_rowconfigure(row + 1, weight = 1)

    def createResetButton(self, window):
        resetButton = Button(window, image = self.images["smilyFace"])
        resetButton.grid(row = 0, column = self.calc_mid_col() ,columnspan = 2, pady = 3)
        return resetButton

    
    def createAllImages(self):
        self.images["button.png"] = createImage("button.png", self.img_width, self.img_height)
        self.images["smilyFace"] = createImage("smilyFace.png", self.img_width, self.img_height)
        self.images["wonderFace"] = createImage("wonderFace.png", self.img_width, self.img_height)
        self.images["deadFace"] = createImage("deadFace.png", self.img_width, self.img_height)
        self.images["mine"] = createImage("mine.png", self.img_width, self.img_height)
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
    
    def calc_mid_col(self):
        if self.cols % 2 == 0:
            return self.cols // 2 - 1
        else:
            return self.cols // 2
        

def createImage(image_path, width, height):
    img = Image.open(image_path).resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)



"""before using ImageTk.PhotoImage Tk() must be invoked and it can only be 
   invoked once otherwise program won't work"""
