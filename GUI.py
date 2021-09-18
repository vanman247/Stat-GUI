import tkinter as tk                    
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
import os
  
  
root = tk.Tk()
root.title("Statistical Analysis")

## SETTING UP THE TABS
tabControl = ttk.Notebook(root)
tab0 = ttk.Frame(tabControl)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tabControl.add(tab0, text ='Importing Data')
tabControl.add(tab1, text ='Correlation Testing')
tabControl.add(tab2, text ='Non-Parametric Hypothesis Test')
tabControl.add(tab3, text ='Normal Testing')
tabControl.add(tab4, text ='Parametric Hypothesis Testing')
tabControl.add(tab5, text ='Stationary Testing')
tabControl.pack(expand = 1, fill ="both")
  
ttk.Label(tab0).grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
ttk.Label(tab1,
          text ='Correlation Testing').grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)

ttk.Label(tab2,
          text ='Non-Parametric Hypothesis Test').grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
ttk.Label(tab3,
          text ='Normal Testing').grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
ttk.Label(tab4,
          text ='Parametric Hypothesis Testing').grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
ttk.Label(tab5,
          text ='Stationary Testing').grid(column = 0,
                                    row = 0, 
                                    padx = 30,
                                    pady = 30)
## IMPORTING DATA TAB
def show():
    url = "C:/Users/Ammon Van/Downloads/"
    tf = filedialog.askopenfilename(initialdir = url,
                                          title = "Select a File",
                                          filetypes = (("CSV files",
                                                        "*.csv*"),
                                                       ("All files",
                                                        "*.*")))
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    T.insert(END, data)
    tf.close()
    
pathh = Entry(tab0)
  
  
# Create button, it will change label text
button = Button(tab0, text = "Import CSV" , command = show).grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)
  
# Create Label
label = Label(tab0, text = " " )
label.grid(column = 2,
           row = 0,
           padx = 5,
           pady = 5)

# Create Text Field to display Data
T = Text(tab0).grid(column = 2,
           row = 2,
           padx = 15,
           pady = 15)


## Run the App
root.mainloop()  
