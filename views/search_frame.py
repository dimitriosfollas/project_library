import tkinter as tk
import tkinter.ttk as ttk

class SearchFrame(ttk.Frame):
    """  """
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(relief='groove', padding=(100, 10))
        self.grid(row=0, column=0, sticky='nwes', ipady=30)
        
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=25)
        #[self.columnconfigure(i, weight=1) for i in range(6)]
        self.columnconfigure(0, weight=1)
        self.columnconfigure(7, weight=1)
        
        # Create the search label
        self.label_search_by = tk.Label(master=self, text="Search by:")
        self.label_search_by.grid(row=0, column=1, padx=10)
        self.label_search_by.configure(font=("Arial", 12))
        
        # Create the search box
        self.cb_search_by = ttk.Combobox(self, values=["Member ID", "Member Name", "Book ISBN", "Book Title", "Loaned Book Title", "Surname of Lender"], state="readonly")
        self.cb_search_by.set("Member ID")        
        self.cb_search_by.bind("<<ComboboxSelected>>", self.load_unter_layout) 
        self.cb_search_by.grid(row=0, column=2, padx=10)
        self.cb_search_by.configure(font=("Arial", 12))
               
        # Create the search entry
        self.entry_id = tk.Entry(master=self)
        self.entry_id.grid(row=0, column=3, columnspan=3, padx=10)
        self.entry_id.configure(font=("Arial", 12))

        # Create the search button
        self.button_search = tk.Button(master=self, text="Search")
        self.button_search.grid(row=0, column=6, padx=10)
        self.button_search.configure(font=("Arial", 12))
        
        self.results_frame = ttk.Frame(self)
        self.results_frame.grid(row=2, column=0, columnspan=7, padx=10, pady=10, sticky="nswe")
        
        self.load_unter_layout(None)
        
    
    def load_unter_layout(self, event):
        """Φορτώνει το layout του πλαισίου αποτελεσμάτων ανάλογα με το κριτήριο αναζήτησης."""
        
        colu_names = ()
        selected_criterion = self.cb_search_by.get()

        #Καθαρισμός πλαισίου αποτελεσμάτων
        for widget in self.results_frame.winfo_children():
            widget.destroy()
            
        try:
            # Μέλη
            if selected_criterion == "Member ID" or selected_criterion == "Member Name":
                # Ονόματα στηλών
                colu_names=("Member ID", "Member Name", "Address", "Birthdate", "Telephone", "Email")
                # Ενέργειες
                self.edit_button = tk.Button(self.results_frame, text="Change member details", command=lambda: self.edit_member(), font=("Arial", 10))
                self.edit_button.grid(row=2, column=1, columnspan=2, pady=10, padx=10)
                self.loan_button = tk.Button(self.results_frame, text="Book loan", command=lambda: self.loan_book(self.results_tree), font=("Arial", 10))
                self.loan_button.grid(row=2, column=3,  columnspan=2, pady=10, padx=10)
                #self.return_button = tk.Button(self.results_frame, text="Επιστροφή βιβλίου", command=lambda: self.return_book(), font=("Arial", 10))
                #self.return_button.grid(row=2, column=3, pady=10, padx=10)
                self.delete_button = tk.Button(self.results_frame, text="Delete member", command=lambda: self.delete_member(), font=("Arial", 10))
                self.delete_button.grid(row=2, column=6, pady=10, padx=10)


            # Βιβλία    
            elif selected_criterion == "Book ISBN" or selected_criterion == "Book Title":
                # Ονόματα στηλών
                colu_names=("Book ISBN", "Book Title", "Author", "Category", "Published", "Available")
                # Ενέργειες
                self.edit_book_button = tk.Button(self.results_frame, text="Change book details ", command=lambda: self.edit_book(), font=("Arial", 10))
                self.edit_book_button.grid(row=2, column=1, columnspan=2, pady=10, padx=10)
                self.loan_book_button = tk.Button(self.results_frame, text="Book loan", command=lambda: self.loan_book(self.results_tree), font=("Arial", 10))
                self.loan_book_button.grid(row=2, column=1, columnspan=2, pady=10, padx=10)
                #self.return_book_button = tk.Button(self.results_frame, text="Επιστροφή βιβλίου", command=lambda: self.return_book(), font=("Arial", 10))
                #self.return_book_button.grid(row=2, column=3, pady=10, padx=10)
                self.delete_book_button = tk.Button(self.results_frame, text="Delete Book", command=lambda: self.delete_book(), font=("Arial", 10))
                self.delete_book_button.grid(row=2, column=4, pady=10, padx=10)
            
            # Δανεισμοί                                    
            elif selected_criterion == "Loaned Book Title" or selected_criterion == "Surname":
                # Ονόματα στηλών
                colu_names=("Loan ID","Member ID", "Member Name", "Book ISBN", "Book Title", "Loan Date", "Date of return")
                # Ενέργειες
                self.return_book_button = tk.Button(self.results_frame, text="Return book", command=lambda: self.return_loan(self.results_tree), font=("Arial", 10))
                self.return_book_button.grid(row=2, column=1, pady=10, padx=10)
                self.extend_loan_button = tk.Button(self.results_frame, text="Extend loan", command=lambda: self.extend_loan(self.results_tree), font=("Arial", 10))
                self.extend_loan_button.grid(row=2, column=2, pady=10, padx=10)

            self.results_tree = ttk.Treeview(self.results_frame, columns=colu_names, show="headings", selectmode="browse")

            for c in colu_names:
                self.results_tree.heading(c, text=c)
                self.results_tree.column(c, anchor="center", width=100, minwidth=100, stretch=True)
            
            self.results_tree.grid(row=3, column=0, columnspan=7, padx=10, pady=10, sticky="nswe")
            
            #scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.results_tree.yview)
            #scrollbar.grid(row=3, column=6, sticky="ns")

        except Exception as e:
            print(f"The error '{e}' occured")       
        

if __name__ == '__main__':
    # Test the SearchFrame class
    root = tk.Tk(baseName="Test Search Frame")
    root.title("Test Search Frame")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.minsize(800, 600)
    search_frame = SearchFrame(root)
    #search_frame.grid(row=0, column=0, sticky='se')
    root.mainloop()
    