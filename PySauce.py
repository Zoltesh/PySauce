#PySauce.py

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.master.geometry('1200x900')

        self.tkvar = tk.StringVar(self.master)
        choices = ['one', 'two', 'three', 'four', 'five']
        self.tkvar.set('one')
        

        self.popupMenu = tk.OptionMenu(self, self.tkvar, *choices, command=self.change_dropdown)
        tk.Label(self, text="Select a program").grid(row=1, column=2)
        self.popupMenu.grid(row=2, column=1)

    
        
        self.tkvar.trace('w', self.change_dropdown)
        
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.config(height=1, width=10)
        self.quit.grid(row=3, column=1)

    def change_dropdown(self, *args):
        print(args[0][1])

if __name__ == "__main__":
    
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
