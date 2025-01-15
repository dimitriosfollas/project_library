import tkinter as tk
import tkinter.ttk as ttk
from views.search_frame import SearchFrame
from tkinter import messagebox


class LibraryApplication(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("Library Wanna-Be Management System")
        self.configure(background="whitesmoke")
        self.minsize(800, 600)
        
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # File Menu
        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(label='Exit Program', command=self.ask_exit_confirmation)
        
        # Insert File Menu
        menubar.add_cascade(label='File', menu=file_menu)
        
        # Load the search frame
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.search_frame = SearchFrame(self)
        
        # Closing the window
        self.protocol("WM_DELETE_WINDOW", self.ask_exit_confirmation)
        
        # Start the main loop
        self.mainloop()


    def ask_exit_confirmation(self) -> None:
        """Ask the user to confirm exit from the program."""
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?", icon='warning'):
            self.destroy()
        else:
            return None
        
if __name__ == '__main__':
    app = LibraryApplication()
        