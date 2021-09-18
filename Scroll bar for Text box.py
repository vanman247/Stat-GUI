import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tabControl = ttk.Notebook(root)
tab0 = ttk.Frame(tabControl)
tab1 = ttk.Frame(tabControl)

tabControl.add(tab0, text ='Importing Data')
tabControl.add(tab1, text ='Correlation Testing')
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

text=tk.Text(tab0, height=10, width=50)
y_scroll_bar= tk.Scrollbar(tab0, command=text.yview, orient="vertical")
y_scroll_bar.grid(row=0, column=1, sticky="ns")
text.grid(row=0,column=0)
text.configure(yscrollcommand=y_scroll_bar.set)
Quote=("""Suck\ne\ne\ne\ne\ne\ne\ne\ne\ne\nee\ne\ne\ne\ne\ne\ne\ne\nee\ned\ne\ne\nde\nd\ne\nded\nc\nc\nx\nc\nx\nc\nzc\ns\nds\nx\nwd\ns\nd\nwd""")
text.insert(tk.END,Quote)

root.mainloop()
