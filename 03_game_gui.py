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

        # hide start up window
        root.withdraw()


class Game:
    if __name__ == '__main__':
        def __init__(self, partner, stakes, starting_balance):
            print(stakes)
            print(starting_balance)

            # gui setup
            self.game_box = Toplevel()
            self.game_frame = Frame(self.game_box)
            self.game_frame.grid()

            # heading row
            self.heading_label = Label(self.game_frame, text="Play",
                                       font="Arial 24 bold", padx=10, pady=10)
            self.heading_label.grid(row=0)

            instructions = "Please click 'Open Boxes' to open the boxes."

            self.instructions_label = Label(self.game_frame, text=instructions,
                                       font="Arial 12 bold", padx=10, pady=10)
            self.instructions_label.grid(row=1)

            # set up three boxes..
            self.box_row_frame = Frame(self.game_frame)
            self.box_row_frame.grid(row = 2)

            # buttons, start at row 0 of box_row_frame\
            self.box_one = Label(self.box_row_frame, text = "?", font = "Arial 16 bold",
                                 padx= 20, pady=20, bg="green")
            self.box_one.grid(row=0, column=0, pady=20)

                        # buttons, start at row 0 of box_row_frame\
            self.box_two = Label(self.box_row_frame, text="?", font="Arial 16 bold",
                                 padx=20, pady=20, bg="green")
            self.box_two.grid(row=0, column=1, pady=20, padx=20)

            0


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box")
    something = Start(root)
    root.mainloop()

