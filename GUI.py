from tkinter import Tk, Canvas, Button, Label, Frame
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
        self.topBar = self.createTopBar()
        self.resetButton = self.createResetButton()
        self.flagCounter = self.createFlagCounter()
        self.timer = self.createTimer()


    def configWindow(self, width, height):
        ws = self.window.winfo_screenwidth() #screen width
        hs = self.window.winfo_screenheight() #screen height
        # coords which put the window in the center of screen
        x = (ws/2) - (width/2)
        y = (hs/2) - (height/2)
        self.window.geometry(("%dx%d+%d+%d") % (width, height, x, y)) #window size

    def createTopBar(self):
        topBar = Canvas(self.window, bg="grey", width = self.width, height = TOP_BAR_HEIGHT)
        topBar.grid(row = 0, column = 0, columnspan = 20)
        self.window.grid_rowconfigure(0, weight = 1)
        return topBar

    def createFlagCounter(self):
        flag_counter = Label(self.topBar, bg="grey", text = "10", fg = "blue", font=("Arial", 17))
        flag_counter.place(relx = 0.25 , rely = 0.5, anchor = "center")
        return flag_counter

    def createTimer(self):
        timer = Label(self.topBar, bg="grey", text = "0", fg = "blue", font=("Arial", 17))
        timer.place(relx = 0.75 , rely = 0.5, anchor = "center")
        return timer

    def createButtons(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells_frontend[row][col] = Label(self.window, image = self.images["button.png"]
                                                      , disabledforeground = "black")
                self.cells_frontend[row][col].grid(row = row + 1, column = col)
                self.window.grid_columnconfigure(col, weight = 1)
                self.window.grid_rowconfigure(row + 1, weight = 1)

    def createResetButton(self):
        resetButton = Button(self.topBar, image = self.images["smilyFace"], bd = 1)
        resetButton.place(relx = 0.5, rely = 0.5 , anchor = "center")
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
