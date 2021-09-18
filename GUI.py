import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
import tksheet
import pandas as pd
import numpy as np
import os
  
  
root = tk.Tk()
root.title("Statistical Analysis")
root.geometry('1000x600')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
    
##style = ttk.Style(root)
##style.configure('TNotebook.Tab', width=root.winfo_screenwidth())


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

# Create Text Field to display Data
text = tk.Text(tab0, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
text.grid(column = 1,
           row = 1,
           padx = 15,
           pady = 15,
           sticky='ew')


## IMPORTING DATA TAB
def open_text_file(): 
    # file type
    filetypes = (
        ('CSV files', '*.csv'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes)
    df = pd.read_csv(f, encoding='utf-8')
    # read the text file and show its content on the Text
    text.insert('1.0', df)

open_button = ttk.Button(tab0,
                         text='Import CSV',
                         command=open_text_file)
open_button.grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)

## Run the App

root.mainloop()  
