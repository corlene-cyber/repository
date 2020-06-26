from tkinter import *
import random


class Convertor:
    def __init__(self):
       
       #Formatting variables...
       background_color = "light blue"
       
       #Convertor Main Screen GUI...
       self.converter_frame = Frame (width=600, height=600, bg=background_color)
       self.converter_frame.grid()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
