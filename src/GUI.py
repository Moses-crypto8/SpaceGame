# Import Module
from tkinter import *

class GUI:
    def __init__(self, root):
        self.root = root
        self.display_frame = LabelFrame(self.root, bg="green", fg="white", padx=7)
        
        # Displaying the frame1 in row 0 and column 0
        self.display_frame.grid(row=0, column=0, ipadx=355, ipady=150)
        # Constructing the second frame, frame2
        self.interactive_frame = LabelFrame(self.root, bg="red", padx=1)
        
        # Displaying the frame2 in row 0 and column 1
        self.interactive_frame.grid(row=1, column=0, ipadx=355, ipady=85)
        
        self.root.mainloop()
        self.description_text = Label()

    def set_incomming_text(self):
        pass
    
    def set_interactive_text(self):
        pass

# create root window
root = Tk()
# root window title and dimension
root.title("Space Game")
# Set geometry (widthxheight)
root.geometry('800x567')
#root.resizable(False, False)

gui = GUI(root)

