from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk
from constants import *


class GUI:

    def __init__(self, width, height, rows, cols):
        self.window = Tk()
        self.window.title("Minesweeper") #title of window
        self.window.resizable(width = False, height = False)
        self.rows = rows
        self.cols = cols
        self.images = {}
        self.createAllImages()
        self.configWindow(self.window, width, height)
        self.createTopBar(self.window)
        self.resetButton = self.createResetButton(self.window)
        self.cells = [[None] * COLS for _ in range(ROWS)]
        self.createButtons(self.window)


    def configWindow(self, window, width, height):
        ws = window.winfo_screenwidth() #screen width
        hs = window.winfo_screenheight() #screen height
        # coords which put the window in the center of screen
        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)
        window.geometry(("%dx%d+%d+%d") % (width, height, x, y)) #window size

    def createButtons(self, window):
        for row in range(1 , self.rows + 1):
            for col in range(self.cols):
                self.cells[row - 1][col] = Button(window, image = self.images["button.png"])
                self.cells[row - 1][col].grid(row = row, column = col)
                self.cells[row - 1][col].bind("<Button-1>", self.wonder)
                window.grid_columnconfigure(col, weight = 1)
                window.grid_rowconfigure(row, weight = 1)

    def createResetButton(self, window):
        resetButton = Button(window, image = self.images["smilyFace"])
        resetButton.grid(row = 0, column = calc_mid_col() ,columnspan = 2, pady = 3)
        return resetButton

    def createTopBar(self, window):
        topBar = Canvas(window, bg="grey", width = WIDTH, height = 30)
        topBar.grid(row = 0, column = 0, columnspan = 20)
        window.grid_rowconfigure(0, weight=1)
    
    def createAllImages(self):
        self.images["button.png"] = createImage("button.png", IMG_WIDTH, IMG_HEIGHT)
        self.images["smilyFace"] = createImage("smilyFace.png", IMG_WIDTH, IMG_HEIGHT)
        self.images["wonderFace"] = createImage("wonderFace.png", IMG_WIDTH, IMG_HEIGHT)
        self.images["deadFace"] = createImage("deadFace.png", IMG_WIDTH, IMG_HEIGHT)
        self.images["mine"] = createImage("mine.png", IMG_WIDTH, IMG_HEIGHT)
        self.images["buttonPressed"] = createImage("0.png", IMG_WIDTH, IMG_HEIGHT)  
        self.images["one"] = createImage("1.png", IMG_WIDTH, IMG_HEIGHT)  
        self.images["two"] = createImage("2.png", IMG_WIDTH, IMG_HEIGHT)  
        self.images["three"] = createImage("3.png", IMG_WIDTH, IMG_HEIGHT)  
        self.images["four"] = createImage("4.png", IMG_WIDTH, IMG_HEIGHT)  
        self.images["five"] = createImage("5.png", IMG_WIDTH, IMG_HEIGHT)  
        self.images["six"] = createImage("6.png", IMG_WIDTH, IMG_HEIGHT)  
        self.images["seven"] = createImage("7.png", IMG_WIDTH, IMG_HEIGHT)  
        self.images["eight"] = createImage("8.png", IMG_WIDTH, IMG_HEIGHT) 

    def wonder(self, event):
	    self.resetButton.configure(image = self.images["wonderFace"]) 
        

def calc_mid_col():
	if COLS % 2 == 0:
		return COLS // 2 - 1
	else:
		return COLS // 2

def createImage(image_path, width, height):
    img = Image.open(image_path).resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

"""before using ImageTk.PhotoImage to create an image Tk()
   must be invoked and it can only be invoked once otherwise 
   program won't work"""

gui = GUI(WIDTH, HIEGHT, ROWS, COLS)
gui.window.mainloop()

