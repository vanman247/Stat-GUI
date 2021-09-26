######Output Shell to Textwidget

from tkinter import *


def check_expression():
    #Your code that checks the expression
    varContent = inputentry.get() # get what's written in the inputentry entry widget
    outputtext.delete("0", 'end-1c') # clear the outputtext text widget
    outputtext.insert(varContent)

root = Tk()
root.title("Post-fix solver")
root.geometry("500x500")

mainframe = Frame(root)
mainframe.grid(column=0, row=0)

inputentry = Entry(mainframe)
inputentry.grid(column=1, row=1)

executebutton = Button(mainframe, text="Run", command=check_expression)
executebutton.grid(column=1, row=3)              

outputtext = Text(mainframe)
outputtext.grid(column=1, row=2)

root.mainloop()
