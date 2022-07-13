# -*- coding: utf-8 -*-
"""
@author: labra
"""
#%%
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import glob


#%%
class GlobController:
    def __init__(self, parent):
        self.parent = parent
        self.model = GlobModel(self)
        self.view = GlobView(self)
#%%

class GlobModel:
    def __init__(self, globpath, recurs):
        self.globpath = globpath
        self.recursive_toggle = recurs
        
        if self.recursive_toggle.get() == True:
            globpath = f"{self.path}\\**\\*.{self.file_type}"
            files = glob.glob(globpath, recursive=True)
        else:
            globpath = f"{self.path}\\*.{self.file_type}"
            files = glob.glob(globpath, recursive=False)

#%%
class GlobView(tk.Frame):
    def create_view():
        raise NotImplementedError

class Form(GlobView):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entries = {}
        self.buttons = {}
        self.comboboxes = {}
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title("Path Input")
        
        mainframe = tk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        parent.rowconfigure(0, minsize=200, weight=1)
        parent.columnconfigure(0, minsize=200, weight=1)
        
        self.recursive_toggle = tk.BooleanVar(value=1)
        self.check_recurs= tk.Checkbutton(self, text='Recursive?', 
                                  command=self.recursive_changed, variable=self.recursive_toggle,
                                  onvalue=1, offvalue=0)
        btn_path = tk.Button(self, text="Path", command=self.get_path)
        btn_path.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        
        self.controller = None
    
    def get_path(self):
        path = fd.askdirectory()

    def get_types(self):
        formats = ('docx', 'md', 'html', 'latex', 'txt')
    
    def recursive_changed(self):
        recurs = self.recursive_toggle.get()
        
    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller
        
class Form(GlobView):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.entries = {}
        self.buttons = {}
        self.comboboxes = {}
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

# %%

# %%

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('File Globber')

        # create a model
        model = GlobModel()

        # create a view and place it on the root window
        view = GlobView(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = GlobController(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()   
# %%
