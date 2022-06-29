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
    def __init__(self):
        super().__init__()
        
       # self.label = label
       # self.button = button
       # self.qbutton = qbutton

        # configure the root window
        root = ttk.Frame(self)
        root.grid(column=0, row=0, columnspan=3, rowspan=3)
        frame = ttk.Frame(root, borderwidth=5, relief="ridge", width=200, height=100)
        frame.grid(column=0, row=0, columnspan=2, rowspan=2)
        self.title('Test App')
        self.geometry('300x150')

        # label
        label = ttk.Label(frame, text='Is this a GUI?')
        label.grid(column=0, row=0)

        # action button
        button = ttk.Button(frame, text='Do Something')
        button['command'] = self.button_clicked
        button.grid(column=0, row=1)
        
        # quit button
        qbutton = ttk.Button(root, text='GTFO')
        qbutton['command'] = self.qbutton_clicked
        qbutton.grid(column=2, row=2)

    def gozer(self):
        app.destroy()        
    
    def button_clicked(self):
        showinfo(title='Information', message='I guess this is something')
    
    def qbutton_clicked(self):
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
