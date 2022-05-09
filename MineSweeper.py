from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk
import random
from constants import *

def CreateWindow(width, height):
	ws = window.winfo_screenwidth() #screen width
	hs = window.winfo_screenheight() #screen height
	# coords which put the window in the center of screen
	x = (ws/2) - (width/2)
	y = (hs/2) - (height/2)
	window.geometry(("%dx%d+%d+%d") % (width, height, x, y)) #window size

def topRow():
	global resetButton
	topBar = Canvas(window, bg="grey", width = WIDTH, height = 30)
	topBar.grid(row = 0, column = 0, columnspan = 20)
	resetButton = Button(window, image = smilyFace, command = reset)
	resetButton.grid(row = 0, column = Calc_mid_col() ,columnspan = 2, pady = 3)
	window.grid_rowconfigure(0, weight=1)

def Calc_mid_col():
	if COLS % 2 == 0:
		return COLS // 2 - 1
	else:
		return COLS // 2

def createButtons():
	for row in range(1,ROWS+1):
		for col in range(COLS):
			tiles[row - 1][col] = Button(window, image = availableSquare
										 , command = lambda i = row - 1
										 , j = col:buttonClickedupdate(i,j))
			tiles[row - 1][col].grid(row=row, column=col)
			window.grid_columnconfigure(col, weight=1)
			window.grid_rowconfigure(row, weight=1)
			tiles[row - 1][col].bind("<Button-1>", wonder)

			
def createMines(n):
	for i in range(n):
		i,j = random.randint(0, ROWS - 1),random.randint(0, COLS - 1)
		while squareStatus[i][j] == "mine":
			i,j = random.randint(0, ROWS - 1),random.randint(0, COLS - 1)
		squareStatus[i][j] = "mine"
	

def countSurrondingMines():
	for i in range(ROWS):
		for j in range(COLS):
			counter = 0
			if squareStatus[i][j] == None:
				if 0 < i and 0 < j:
					if squareStatus[i-1][j-1] == "mine":
						counter += 1
				if 0 < i:
					if squareStatus[i-1][j] == "mine":
						counter += 1
				if 0 < i and j < COLS - 1:	
					if squareStatus[i-1][j+1] == "mine":
						counter += 1
				if 0 < j:
					if squareStatus[i][j-1] == "mine":
						counter += 1	
				if j < COLS - 1:	
					if squareStatus[i][j+1] == "mine":
						counter += 1
				if i < ROWS - 1 and 0 < j:
					if squareStatus[i+1][j-1] == "mine":
						counter += 1
				if i < ROWS - 1:	
					if squareStatus[i+1][j] == "mine":
						counter += 1
				if i < ROWS - 1 and j < COLS - 1:	
					if squareStatus[i+1][j+1] == "mine":
						counter += 1
				squareStatus[i][j] = counter
	

def buttonClickedupdate(i,j):
	tiles_visited_status[i][j] = True

	if squareStatus[i][j] == "mine":
		mineClicked()
		tiles[i][j].configure(image=mine,state="normal",command=0,relief="sunken")
		tiles[i][j].unbind("<Button-1>")

	else:
		if squareStatus[i][j] == 0:
			clearSrounding(i,j)
			tiles[i][j].configure(image=buttonPressed,state="normal",command=0,relief="sunken")
			resetButton.configure(image=smilyFace)
			tiles[i][j].unbind("<Button-1>")
			
		if squareStatus[i][j] == 1:
			tiles[i][j].configure(image=one,state="normal",command=0,relief="sunken")
			resetButton.configure(image=smilyFace)
			tiles[i][j].unbind("<Button-1>")

		if squareStatus[i][j] == 2:
			tiles[i][j].configure(image=two,state="normal",command=0,relief="sunken")
			resetButton.configure(image=smilyFace)
			tiles[i][j].unbind("<Button-1>")

		if squareStatus[i][j] == 3:
			tiles[i][j].configure(image=three,state="normal",command=0,relief="sunken")
			resetButton.configure(image=smilyFace)
			tiles[i][j].unbind("<Button-1>")

		if squareStatus[i][j] == 4:
			tiles[i][j].configure(image=four,state="normal",command=0,relief="sunken")
			resetButton.configure(image=smilyFace)
			tiles[i][j].unbind("<Button-1>")

		if squareStatus[i][j] == 5:
			tiles[i][j].configure(image=five,state="normal",command=0,relief="sunken")
			resetButton.configure(image=smilyFace)
			tiles[i][j].unbind("<Button-1>")

		if squareStatus[i][j] == 6:
			tiles[i][j].configure(image=six,state="normal",command=0,relief="sunken")
			resetButton.configure(image=smilyFace)
			tiles[i][j].unbind("<Button-1>")

		if squareStatus[i][j] == 7:
			tiles[i][j].configure(image=seven,state="normal",command=0,relief="sunken")
			resetButton.configure(image=smilyFace)
			tiles[i][j].unbind("<Button-1>")

		if squareStatus[i][j] == 8:	
			tiles[i][j].configure(image=eight,state="normal",command=0,relief="sunken")
			resetButton.configure(image=smilyFace)
			tiles[i][j].unbind("<Button-1>")
		
		if playerWins():
			print("wins")

def getNeighbours(row, col):

	if row == 0 and col == 0:
		return [[1,0],[1,1],[0,1]]
	if row == 0  and col == COLS - 1:
		return [[0,col-1],[1,col-1],[1,col]]
	if row == ROWS - 1 and col == 0:
		return [[row-1,0],[row-1,1],[row,1]]
	if row == ROWS - 1 and col == COLS - 1:
		return [[row-1,col],[row-1,col-1],[row,col-1]]

	if row == 0:
		return [[0,col-1],[1,col-1],[1,col],[1,col+1],[0,col+1]]
	if row == ROWS - 1:
		return [[row,col-1],[row-1,col-1],[row-1,col],[row-1,col+1],[row,col+1]]		

	if col == 0:
		return [[row-1,col],[row-1,col+1],[row,col+1],[row+1,col+1],[row+1,col]]
	if col == COLS - 1:
		return [[row-1,col],[row-1,col-1],[row,col-1],[row+1,col-1],[row+1,col]]
	
	if 0 < row < ROWS - 1 and 0 < col < COLS - 1:
		return[[row-1,col-1],[row-1,col],[row-1,col+1],[row,col+1],[row+1,col+1]
			   ,[row+1,col],[row+1,col-1],[row,col-1]]


def clearSrounding(row, col):
	if squareStatus[row][col] == 0 and playerWins():
		print("wins")
		
	if squareStatus[row][col] == 0:
		tiles_visited_status[row][col] = True
		tiles[row][col].configure(image=buttonPressed,state="normal",command=0,relief="sunken")
		tiles[row][col].unbind("<Button-1>")
		neighbours = getNeighbours(row,col)
		for n in neighbours:
			a,b = n[0],n[1]
			if not tiles_visited_status[a][b]:
				clearSrounding(a,b)

	else:
		return buttonClickedupdate(row,col)
		
	
def mineClicked():
	for i in range (ROWS):
		for j in range(COLS):
			tiles[i][j].configure(state="normal",command=0,relief="sunken")
			tiles[i][j].unbind("<Button-1>")
			if squareStatus[i][j] == "mine":
				tiles[i][j].configure(image=mine)
	resetButton.configure(image=deadFace)


def resetSquareStatus():
	for i in range(ROWS):
		for j in range(COLS):
			squareStatus[i][j] = None

def resetVisited():
	for i in range(ROWS):
		for j in range(COLS):
			tiles_visited_status[i][j] = None

def resetTiles():
	for i in range(ROWS):
		for j in range(COLS):
			tiles[i][j] = None

def reConfigTiles():
	for row in range(1,ROWS+1):
		for col in range(COLS):
			tiles[row - 1][col].configure(image = availableSquare
										  , command = lambda i = row - 1
										  , j = col:buttonClickedupdate(i,j)
										  , relief="raised")
			tiles[row - 1][col].bind("<Button-1>", wonder)

	
def reset():
	resetSquareStatus()
	resetVisited()
	reConfigTiles()
	createMines(NO_OF_MINES)
	countSurrondingMines()
	resetButton.configure(image=smilyFace)


def playerWins():
	no_of_visited_tiles = 0
	for row_tiles_visited_status in tiles_visited_status:
		for tile_visited_status in row_tiles_visited_status:
			if tile_visited_status:
				no_of_visited_tiles += 1
	print(no_of_visited_tiles)
	return no_of_visited_tiles == NO_OF_TILES - NO_OF_MINES

def wonder(event):
	resetButton.configure(image=wonderFace)

def createImage(image_path, width, height):
	img = Image.open(image_path).resize((width, height), Image.LANCZOS)
	return ImageTk.PhotoImage(img)

resetButton = None
tiles = [[None]*COLS for _ in range(ROWS)]
squareStatus = [[None]*COLS for _ in range(ROWS)]
tiles_visited_status = [[False]*COLS for _ in range(ROWS)]
window = Tk() #title of window
window.title("Minesweeper") #title of window
window.resizable(width=False, height=False)
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

CreateWindow(WIDTH, HIEGHT)
topRow()
createMines(NO_OF_MINES)
countSurrondingMines()
createButtons()
window.mainloop()

