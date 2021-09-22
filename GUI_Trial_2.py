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
root.geometry('800x550')
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 1000)
    
## SETTING UP THE TABS
################################################################################
################################################################################
################################################################################

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
                                    padx = 5,
                                    pady = 10)
ttk.Label(tab1).grid(column = 0,
                                    row = 0, 
                                    padx = 5,
                                    pady = 5)

ttk.Label(tab2).grid(column = 0,
                                    row = 0, 
                                    padx = 5,
                                    pady = 5)
ttk.Label(tab3).grid(column = 0,
                                    row = 0, 
                                    padx = 5,
                                    pady = 5)
ttk.Label(tab4).grid(column = 0,
                                    row = 0, 
                                    padx = 5,
                                    pady = 5)
ttk.Label(tab5).grid(column = 0,
                                    row = 0, 
                                    padx = 5,
                                    pady = 5)


# Create Text Field to display Data(TAB0)
########################################################################
########################################################################

text = tk.Text(tab0,
               wrap="none")

text.grid(column = 1,
           row = 1,
           padx = 0,
           pady = 0,
          
           sticky='ew')

## Add the Scrollbars for the Text Field
yscrollbar = ttk.Scrollbar(tab0, orient='vertical', command=text.yview)
yscrollbar.grid(row=1, column=3, sticky='ns')

xscrollbar = ttk.Scrollbar(tab0, orient='horizontal', command=text.xview)
xscrollbar.grid(row=2, column=1, sticky='ew')

#  communicate back to the scrollbar
text['yscrollcommand'] = yscrollbar.set
text['xscrollcommand'] = xscrollbar.set

global df 
global cos

df = 0

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
    text.insert(tk.END, df)
    cos = list(df.columns)
    return df, cos

open_button = ttk.Button(tab0,
                         text='Import CSV',
                         command=open_text_file)
open_button.grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)


##################################################################################
##################################################################################
##################################################################################
##                          Tab1                                                ##
##################################################################################
##################################################################################
##################################################################################

text1 = tk.Text(tab1,
               wrap="none")

text1.grid(column = 1,
           row = 1,
           padx = 0,
           pady = 15,
          
           sticky='ew')

## Add the Scrollbars for the Text Field
yscrollbar1 = ttk.Scrollbar(tab1, orient='vertical', command=text1.yview)
yscrollbar1.grid(row=1, column=3, sticky='ns')

xscrollbar1 = ttk.Scrollbar(tab1, orient='horizontal', command=text1.xview)
xscrollbar1.grid(row=2, column=1, sticky='ew')

#  communicate back to the scrollbar
text1['yscrollcommand'] = yscrollbar1.set
text1['xscrollcommand'] = xscrollbar1.set

options = []
    
run = ttk.Button(tab1,
                 text='Run Correlation Tests',
                 command=open_text_file)

run.grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)

# Dropdown menu options
options = cos
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( " " )

clicked1 = StringVar()
  
# initial menu text
clicked1.set( " " )
  
# Create Dropdown menu
drop = OptionMenu(tab1, clicked , *options )
drop.grid(column = 0,
           row = 1,
           padx = 5,
           pady = 5)
drop1 = OptionMenu(tab1, clicked1, *options )
drop1.grid(column = 1,
           row = 0,
           padx = 5,
           pady = 5)



## Run the App

root.mainloop()  

