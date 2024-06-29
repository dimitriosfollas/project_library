import tkinter as tk
import tkinter.ttk as ttk

class SearchFrame(ttk.Frame):
    """  """
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(relief='groove', padding=(100, 10))
        self.grid(sticky='ew')
        
        # Create the search label
        self.label_search_by = tk.Label(master=self, text="Search by:")
        self.label_search_by.grid(row=0, column=0, padx=10)
        
        # Create the search box
        self.cb_search_by = ttk.Combobox(self, values=["Member ID", "Member Name", "Book ISBN", "Book Title", "Loaned Book Title", "Surname of Lender"], state="readonly")
        self.cb_search_by.set("Member ID")        
        #self.cb_search_by.bind("<<ComboboxSelected>>", print(self.cb_search_by.get())) 
        self.cb_search_by.grid(row=0, column=1, padx=10)
               
        # Create the search entry
        self.entry_id = tk.Entry(master=self)
        self.entry_id.grid(row=0, column=2, padx=10)

        # Create the search button
        self.button_search = tk.Button(master=self, text="Search")
        self.button_search.grid(row=0, column=3, padx=10)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=2)
        self.grid_columnconfigure(3, weight=1)
        
if __name__ == '__main__':
    # Test the SearchFrame class
    root = tk.Tk()
    root.title("Test Search Frame")
    root.geometry("800x600")
    search_frame = SearchFrame(root)
    root.mainloop()
    