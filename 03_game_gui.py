from tkinter import *
from functools import partial
import random

class Start:
    def __init__(self, parent):

        # gui to get starting bal and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        self.push_me_button = Button(text="push me", command=self.to_game)
        self.push_me_button.grid(row=0, pady=10)

    def to_game(self):

        # retrieve starting bal
        starting_balance = 50
        stakes = 1

        Game(self, stakes, starting_balance)

        # hide start up windiw
        root.withdraw()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()