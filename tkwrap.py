# -*- coding: utf-8 -*-
"""
@author: labra
"""
#%%

import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter.messagebox import showinfo


#%%
class App(tk.Tk):
    def __init__(self, labelstr, titlestr):
        super().__init__()
        
        # Modify for variable input
        self.labelstr = labelstr
        self.titlestr = titlestr

        # configure the root window
        root = ttk.Frame(self)
        root.grid(column=0, row=0, columnspan=3, rowspan=3)
        self.title(f'{titlestr}')
        self.geometry('300x150')
        
        # Configure Interior Frame
        frame = ttk.Frame(root, borderwidth=5, relief="ridge", width=200, height=100)
        frame.grid(column=0, row=0, columnspan=2, rowspan=2)
        
        # Label the Frame
        label = ttk.Label(frame, text=f'{labelstr}')
        label.grid(column=0, row=0)

        # action button
        button = ttk.Button(frame, text='Do Something')
        button['command'] = self.button_clicked
        button.grid(column=0, row=1)
        
        # quit button
        qbutton = ttk.Button(frame, text='GTFO')
        qbutton['command'] = self.gtfo
        qbutton.grid(column=2, row=2)
    
    # Button Commands
    def gozer(self):
        app.destroy()        
    
    def button_clicked(self):
        showinfo(title='Information', message='I guess this is something')
    
    # Exit and Confirmation Dialog 
    def gtfo(self):
        qtr = Toplevel(self)
        confirm = ttk.Frame(qtr)
        confirm.grid(column=0, row=0, columnspan=3, rowspan=2)
        confirmlabel = ttk.Label(confirm, text='Exit?')
        confirmlabel.grid(column=1, row=0)
        quity = ttk.Button(confirm, text='Yes')
        quity.grid(column=0, row=1)
        quity['command'] = self.gozer
        quitn = ttk.Button(confirm, text='No')
        quitn.grid(column=2, row=1)
        quitn['command'] = qtr.destroy

#%%
if __name__ == "__main__":
    app = App()
    app.mainloop()
