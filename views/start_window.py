import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class LibraryApplication(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Library Management System")
        self.configure(background="whitesmoke")
        self.minsize(800, 600)
        
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # File Menu
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label='Exit Program', command=self.confirm_exit)
        
        # Insert File Menu
        menubar.add_cascade(label='File', menu=file_menu)
        
        #
        self.mainloop()

    def confirm_exit(self) -> None:
        """Ask the user to confirm exit from the program.

        Returns:
            None: _description_
        """
        result = messagebox.askquestion("Exit", "Are you sure you want to exit", icon='warning')
        if result == "yes":
            self.destroy()
        else:
            return None
        
if __name__ == '__main__':
    app = LibraryApplication()
        