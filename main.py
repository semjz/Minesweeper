from minesweeper import Minesweeper
from constants import *

def main():
    game = Minesweeper(ROWS, COLS)
    game.run()

if __name__ == "__main__":
    main()