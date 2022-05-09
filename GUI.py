from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk
from constants import *


class GUI:

    def __init__(self, window, width, height, rows, cols):
        self.window = window
        self.rows = rows
        self.cols = cols
        self.ConfigWindow(self.window, width, height)
        self.CreateTopBar(self.window)
        self.resetButton = self.createResetButton(self.window)
        self.cells = [[None] * COLS for _ in range(ROWS)]
        self.createButtons(self.window)


    def ConfigWindow(self, window, width, height):
        ws = window.winfo_screenwidth() #screen width
        hs = window.winfo_screenheight() #screen height
        # coords which put the window in the center of screen
        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)
        window.geometry(("%dx%d+%d+%d") % (width, height, x, y)) #window size

    def createButtons(self, window):
        for row in range(1 , self.rows + 1):
            for col in range(self.cols):
                self.cells[row - 1][col] = Button(window, image = availableSquare)
                self.cells[row - 1][col].grid(row = row, column = col)
                self.cells[row - 1][col].bind("<Button-1>", self.wonder)
                window.grid_columnconfigure(col, weight = 1)
                window.grid_rowconfigure(row, weight = 1)

    def createResetButton(self, window):
        resetButton = Button(window, image = smilyFace)
        resetButton.grid(row = 0, column = Calc_mid_col() ,columnspan = 2, pady = 3)
        return resetButton

    def CreateTopBar(self, window):
        topBar = Canvas(window, bg="grey", width = WIDTH, height = 30)
        topBar.grid(row = 0, column = 0, columnspan = 20)
        window.grid_rowconfigure(0, weight=1)

    def wonder(self, event):
	    self.resetButton.configure(image = wonderFace)

def Calc_mid_col():
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
   
window = Tk()
availableSquare = createImage("button.png",IMG_WIDTH,IMG_HEIGHT)
smilyFace = createImage("smilyFace.png",IMG_WIDTH,IMG_HEIGHT)
wonderFace = createImage("wonderFace.png",IMG_WIDTH,IMG_HEIGHT)
deadFace = createImage("deadFace.png",IMG_WIDTH,IMG_HEIGHT)
mine = createImage("mine.png",IMG_WIDTH,IMG_HEIGHT)
buttonPressed = createImage("0.png",IMG_WIDTH,IMG_HEIGHT)  
one = createImage("1.png",IMG_WIDTH,IMG_HEIGHT)  
two = createImage("2.png",IMG_WIDTH,IMG_HEIGHT)  
three = createImage("3.png",IMG_WIDTH,IMG_HEIGHT)  
four = createImage("4.png",IMG_WIDTH,IMG_HEIGHT)  
five = createImage("5.png",IMG_WIDTH,IMG_HEIGHT)  
six = createImage("6.png",IMG_WIDTH,IMG_HEIGHT)  
seven = createImage("7.png",IMG_WIDTH,IMG_HEIGHT)  
eight = createImage("8.png",IMG_WIDTH,IMG_HEIGHT)  

gui = GUI(window, WIDTH, HIEGHT, ROWS, COLS)
window.mainloop()

