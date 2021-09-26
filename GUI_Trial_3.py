import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
import tksheet
import pandas as pd
import numpy as np
import os
import sys

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

tabControl.add(tab0, text ='View Dataset')
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
                         text='View CSV File',
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
           row = 5,
           padx = 0,
           pady = 15,
           sticky='ew')

## Add the Scrollbars for the Text Field
yscrollbar1 = ttk.Scrollbar(tab1, orient='vertical', command=text1.yview)
yscrollbar1.grid(row=5, column=2, sticky='ns')

xscrollbar1 = ttk.Scrollbar(tab1, orient='horizontal', command=text1.xview)
xscrollbar1.grid(row=6, column=1, sticky='ew')

#  communicate back to the scrollbar
text1['yscrollcommand'] = yscrollbar1.set
text1['xscrollcommand'] = xscrollbar1.set

entry1_1=tk.StringVar()
entry1_2=tk.StringVar()

def Coor():
    from scipy.stats import pearsonr
    from scipy.stats import spearmanr
    from scipy.stats import kendalltau
    from scipy.stats import chi2_contingency
    direc="C:/Users/Ammon Van/Desktop/Fun Projects/Statistic Analysis/Tests"
    filetypes = (("CSV", "*.CSV"), ("All Files", "*.*"))
    url = fd.askopenfilename(initialdir=direc, title="Open File", filetypes=filetypes)
    stuff = pd.read_csv(url)
    stuff = stuff.select_dtypes(include=["float64", "int64"])
    line = """-------------------------------------------------------------------------------- \n"""


    try:
        stat, p = pearsonr(stuff["{}".format(entry1_1.get())],
                           stuff["{}".format(entry1_2.get())])
        text1.insert(END, "Pearson's Test \n \n")
        text1.insert(END, "                          ASSUMPTIONS                         \n")
        text1.insert(END, "    1. Observations in each sample are independent and identically distributed \n")
        text1.insert(END, "    2. Observations in each sample are normally distributed \n")
        text1.insert(END, "    3. Observations in each sample have the same variance \n\n\n")
        text1.insert(END, '                Pearson’s correlation coefficient R = %.4f \n' % (stat), "\n")
        text1.insert(END, '                P-Value = %.4f \n' % (p), "\n")
        text1.insert(END, "\n")
        if p > 0.05:
            text1.insert(END, 'H0: the two samples are probably independent. \n \n \n')
            text1.insert(END, line)
        else:
            text1.insert(END, 'H1: there is probably a dependency between the samples \n \n \n')
            text1.insert(END, line)
    except ValueError:
        text1.insert(END, ValueError)
        text1.insert(END, "                Pearson's Test \n")
        text1.insert(END, "                Passed")
        text1.insert(END, line)
        pass

        
    try:
        stat, p = spearmanr(stuff["{}".format(entry1_1.get())],
                            stuff["{}".format(entry1_2.get())],
                            nan_policy="omit",
                            alternative="two-sided")
        
        text1.insert(END, "Spearman’s Rank Correlation \n \n")
        text1.insert(END, "                          ASSUMPTIONS                         \n")
        text1.insert(END, "    1. Observations in each sample are independent and identically distributed \n")
        text1.insert(END, "    2. Observations in each sample can be ranked \n \n")
        text1.insert(END, '                Spearman correlation coefficient = %.4f \n' % (stat), "\n")
        text1.insert(END, '                P-Value = %.4f \n' % (p), "\n")
        text1.insert(END, "\n")

        if p > 0.05:
            text1.insert(END, 'H0: the two samples are probably independent. \n \n \n')
            text1.insert(END, line)
        else:
            text1.insert(END, 'H1: there is probably a dependency between the samples \n \n \n')
            text1.insert(END, line)
    except ValueError:
        text1.insert(END, ValueError)
        text1.insert(END, "                Spearman’s Rank Correlation \n")
        text1.insert(END, "                Passed")
        text1.insert(END, line)
        pass



    try:
        stat, p = kendalltau(stuff["{}".format(entry1_1.get())],
                           stuff["{}".format(entry1_2.get())],
                           nan_policy="omit",
                           method="auto",
                           variant="b")
        
        text1.insert(END, "Kendall Tau's Test \n \n")
        text1.insert(END, "                          ASSUMPTIONS                         \n")
        text1.insert(END, "    1. Observations in each sample are independent and identically distributed \n")
        text1.insert(END, "    2. Observations in each sample can be ranked \n \n")
        text1.insert(END, '                Tau statistic = %.4f \n' % (stat), "\n")
        text1.insert(END, '                P-Value = %.4f \n' % (p), "\n")
        text1.insert(END, "\n")
        if p > 0.05:
            text1.insert(END, 'H0: the two samples are probably independent. \n \n \n')
            text1.insert(END, line)
        else:
            text1.insert(END, 'H1: there is probably a dependency between the samples \n \n \n')
            text1.insert(END, line)
    except ValueError:
        text1.insert(END, ValueError)
        text1.insert(END, "                Kendall Tau's Test \n")
        text1.insert(END, "                Passed")
        text1.insert(END, line)
        pass


    
        
    try:
        table = [stuff["{}".format(entry1_1.get())],
                 stuff["{}".format(entry1_2.get())]]
        
        stat, p, dof, expected = chi2_contingency(table)
        
        text1.insert(END, "CHI_2 Contingency \n \n")
        text1.insert(END, "                          ASSUMPTIONS                         \n")
        text1.insert(END, "    1. Observations used in the calculation of the contingency table are independent \n")
        text1.insert(END, "    2. 25 or more examples in each cell of the contingency table \n \n")
        text1.insert(END, '                CHI2 = %.4f \n' % (stat), "\n")
        text1.insert(END, '                P-Value = %.4f \n' % (p), "\n")
        text1.insert(END, '                Degrees of Freedom = %.4f \n' % (dof), "\n")
        text1.insert(END, "\n")
        if p > 0.05:
            text1.insert(END, 'H0: the two samples are probably independent. \n \n \n')
            text1.insert(END, line)
        else:
            text1.insert(END, 'H1: there is probably a dependency between the samples \n \n \n')
            text1.insert(END, line)
    except ValueError:
        text1.insert(END, ValueError)
        text1.insert(END, "                CHI_2 Contingency \n")
        text1.insert(END, "                Passed")
        text1.insert(END, line)
        pass



    
    return

open_button1 = ttk.Button(tab1,
                         text='Run correlation Tests',
                         command=Coor)
open_button1.grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)

entry1_1_label = tk.Label(tab1, text="Data Feature 1")
entry1_1_label.grid(column = 0,
           row = 1,
           padx = 5,
           pady = 5)

entry1_1 = tk.Entry(tab1, textvariable=None)
entry1_1.grid(column = 0,
           row = 2,
           padx = 5,
           pady = 5)

entry1_2_label = tk.Label(tab1, text="Data Feature 2")
entry1_2_label.grid(column = 0,
           row = 3,
           padx = 5,
           pady = 5)

entry1_2 = tk.Entry(tab1, textvariable=None)
entry1_2.grid(column = 0,
           row = 4,
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
           row = 5,
           padx = 0,
           pady = 15,
           sticky='ew')

## Add the Scrollbars for the Text Field
yscrollbar2 = ttk.Scrollbar(tab2, orient='vertical', command=text2.yview)
yscrollbar2.grid(row=5, column=2, sticky='ns')

xscrollbar2 = ttk.Scrollbar(tab2, orient='horizontal', command=text2.xview)
xscrollbar2.grid(row=6, column=1, sticky='ew')

#  communicate back to the scrollbar
text2['yscrollcommand'] = yscrollbar2.set
text2['xscrollcommand'] = xscrollbar2.set

entry2_1=tk.StringVar()
entry2_2=tk.StringVar()

def Non_Param():
    from scipy.stats import mannwhitneyu
    from scipy.stats import wilcoxon
    from scipy.stats import kruskal
    from scipy.stats import friedmanchisquare
    direc="C:/Users/Ammon Van/Desktop/Fun Projects/Statistic Analysis/Tests"
    filetypes = (("CSV", "*.CSV"), ("All Files", "*.*"))
    url = fd.askopenfilename(initialdir=direc, title="Open File", filetypes=filetypes)
    stuff = pd.read_csv(url)
    stuff = stuff.select_dtypes(include=["float64", "int64"])
    line = """-------------------------------------------------------------------------------- \n"""

    try:
        stat, p = mannwhitneyu(stuff["{}".format(entry2_1.get())],
                               stuff["{}".format(entry2_2.get())],
                               method="auto")
        text2.insert(END, "Mann-Whitney U Test \n \n")
        text2.insert(END, "                          ASSUMPTIONS                         \n")
        text2.insert(END, "    1. Observations in each sample are independent and identically distributed \n")
        text2.insert(END, "    2. Observations in each sample can be Ranked \n \n")
        text2.insert(END, '                Mann-Whitney U Test Stat = %.4f \n' % (stat), "\n")
        text2.insert(END, '                P-Value = %.4f \n' % (p), "\n")
        text2.insert(END, "\n")
        if p > 0.05:
            text2.insert(END, 'H0: the distributions of both samples are equal. \n \n \n')
            text2.insert(END, line)
        else:
            text2.insert(END, 'H1: the distributions of both samples are not equal. \n \n \n')
            text2.insert(END, line)
    except ValueError:
        text2.insert(END, ValueError)
        text2.insert(END, "                Mann-Whitney U Test \n")
        text2.insert(END, "                Passed")
        text2.insert(END, line)
        pass

    try:
        stat, p = wilcoxon(stuff["{}".format(entry2_1.get())],
                               stuff["{}".format(entry2_2.get())],
                               zero_method="pratt",
                               correction=True,
                               mode="auto")
        text2.insert(END, "Wilcoxon Test \n \n")
        text2.insert(END, "                          ASSUMPTIONS                         \n")
        text2.insert(END, "    1. Observations in each sample are independent and identically distributed \n")
        text2.insert(END, "    2. Observations in each sample can be Ranked \n \n")
        text2.insert(END, '                Mann-Whitney U Test Stat = %.4f \n' % (stat), "\n")
        text2.insert(END, '                P-Value = %.4f \n' % (p), "\n")
        text2.insert(END, "\n")
        if p > 0.05:
            text2.insert(END, 'H0: the distributions of both samples are equal. \n \n \n')
            text2.insert(END, line)
        else:
            text2.insert(END, 'H1: the distributions of both samples are not equal. \n \n \n')
            text2.insert(END, line)
    except ValueError:
        text2.insert(END, ValueError)
        text2.insert(END, "                Wilcoxon Test \n")
        text2.insert(END, "                Passed")
        text2.insert(END, line)
        pass













    
        
    return

open_button2 = ttk.Button(tab2,
                         text='Run Non Parametric Tests',
                         command=Non_Param)
open_button2.grid(column = 0,
           row = 0,
           padx = 5,
           pady = 5)

entry2_1_label = tk.Label(tab2, text="Data Feature 1")
entry2_1_label.grid(column = 0,
           row = 1,
           padx = 5,
           pady = 5)

entry2_1 = tk.Entry(tab2, textvariable=None)
entry2_1.grid(column = 0,
           row = 2,
           padx = 5,
           pady = 5)

entry2_2_label = tk.Label(tab2, text="Data Feature 2")
entry2_2_label.grid(column = 0,
           row = 3,
           padx = 5,
           pady = 5)

entry2_2 = tk.Entry(tab2, textvariable=None)
entry2_2.grid(column = 0,
           row = 4,
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
