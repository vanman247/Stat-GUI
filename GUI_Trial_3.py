import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
import tksheet
import pandas as pd
import numpy as np
import os
import sys
from Tests import correlation_test


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


##################################################################################
##################################################################################
##################################################################################
##                          Tab0                                                ##
##################################################################################
##################################################################################
##################################################################################

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
    return

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

def Coor():
    correlation_test.main()
    return

open_button1 = ttk.Button(tab1,
                         text='Run Corrilation Tests',
                         command=Coor)
open_button1.grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)

##################################################################################
##################################################################################
##################################################################################
##                          Tab2                                                ##
##################################################################################
##################################################################################
##################################################################################

text2 = tk.Text(tab2,
               wrap="none")

text2.grid(column = 1,
           row = 1,
           padx = 0,
           pady = 15,
          
           sticky='ew')

## Add the Scrollbars for the Text Field
yscrollbar2 = ttk.Scrollbar(tab2, orient='vertical', command=text2.yview)
yscrollbar2.grid(row=1, column=3, sticky='ns')

xscrollbar2 = ttk.Scrollbar(tab2, orient='horizontal', command=text2.xview)
xscrollbar2.grid(row=2, column=1, sticky='ew')

#  communicate back to the scrollbar
text2['yscrollcommand'] = yscrollbar2.set
text2['xscrollcommand'] = xscrollbar2.set

def Non_Param():
    pass

open_button2 = ttk.Button(tab2,
                         text='Run Non Parametric Tests',
                         command=Non_Param)
open_button2.grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)


##################################################################################
##################################################################################
##################################################################################
##                          Tab3                                                ##
##################################################################################
##################################################################################
##################################################################################

text3 = tk.Text(tab3,
               wrap="none")

text3.grid(column = 1,
           row = 1,
           padx = 0,
           pady = 15,
          
           sticky='ew')

## Add the Scrollbars for the Text Field
yscrollbar3 = ttk.Scrollbar(tab3, orient='vertical', command=text3.yview)
yscrollbar3.grid(row=1, column=3, sticky='ns')

xscrollbar3 = ttk.Scrollbar(tab3, orient='horizontal', command=text3.xview)
xscrollbar3.grid(row=2, column=1, sticky='ew')

#  communicate back to the scrollbar
text3['yscrollcommand'] = yscrollbar3.set
text3['xscrollcommand'] = xscrollbar3.set

def Normal_Test():
    pass

open_button3 = ttk.Button(tab3,
                         text='Run Normalicy Testing',
                         command=Normal_Test)
open_button3.grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)


##################################################################################
##################################################################################
##################################################################################
##                          Tab4                                                ##
##################################################################################
##################################################################################
##################################################################################

text4 = tk.Text(tab4,
               wrap="none")

text4.grid(column = 1,
           row = 1,
           padx = 0,
           pady = 15,
          
           sticky='ew')

## Add the Scrollbars for the Text Field
yscrollbar4 = ttk.Scrollbar(tab4, orient='vertical', command=text4.yview)
yscrollbar4.grid(row=1, column=3, sticky='ns')

xscrollbar4 = ttk.Scrollbar(tab4, orient='horizontal', command=text4.xview)
xscrollbar4.grid(row=2, column=1, sticky='ew')

#  communicate back to the scrollbar
text4['yscrollcommand'] = yscrollbar4.set
text4['xscrollcommand'] = xscrollbar4.set

def Param_Testing():
    pass

open_button4 = ttk.Button(tab4,
                         text='Run Parameter Testing',
                         command=Param_Testing)
open_button4.grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)


##################################################################################
##################################################################################
##################################################################################
##                          Tab5                                                ##
##################################################################################
##################################################################################
##################################################################################

text5 = tk.Text(tab5,
               wrap="none")

text5.grid(column = 1,
           row = 1,
           padx = 0,
           pady = 15,
          
           sticky='ew')

## Add the Scrollbars for the Text Field
yscrollbar5 = ttk.Scrollbar(tab5, orient='vertical', command=text5.yview)
yscrollbar5.grid(row=1, column=3, sticky='ns')

xscrollbar5 = ttk.Scrollbar(tab5, orient='horizontal', command=text5.xview)
xscrollbar5.grid(row=2, column=1, sticky='ew')

#  communicate back to the scrollbar
text5['yscrollcommand'] = yscrollbar5.set
text5['xscrollcommand'] = xscrollbar5.set

def Stationary_Test():
    pass

open_button5 = ttk.Button(tab5,
                         text='Run Stationary Tests',
                         command=Stationary_Test)
open_button5.grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)


## Run the App

root.mainloop()  
