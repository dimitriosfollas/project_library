import tkinter as tk
import tkinter.ttk as ttk

class SearchFrame(ttk.Frame):
    """  """
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(relief='groove', padding=(10, 10))
        self.grid(row=0, column=0, sticky='nsew')
        
        # Create the search label
        self.cb_search_by = ttk.Combobox(self, values=["Αριθμός Μέλους", "Όνομα Μέλους", "ISBN Βιβλίου", "Τίτλος Βιβλίου", "Τίτλος Δανεισμένου Βιβλίου", "Επώνυμο Δανειζόμενου"], state="readonly")
        self.cb_search_by.set("Αριθμός Μέλους")        
        #self.cb_search_by.bind("<<ComboboxSelected>>", print(self.cb_search_by.get())) 
        self.cb_search_by.grid()
        
        # Create the search label
        self.label_search_by = tk.Label(master=self, text="Κριτήριο αναζήτησης:")
        self.label_search_by.grid()
               
        # Create the search entry
        self.entry_id = tk.Entry(master=self)
        self.entry_id.grid()

        # Create the search button
        self.button_search = tk.Button(master=self, text="Αναζήτηση")
        self.button_search.grid()
        
if __name__ == '__main__':
    # Test the SearchFrame class
    root = tk.Tk()
    root.title("Test Search Frame")
    search_frame = SearchFrame(root)
    root.mainloop()
    