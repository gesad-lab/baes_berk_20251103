'''
Implements the GUI using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import requests
from database import create_database  # Import the create_database function
# Check if tkinter is available, if not, raise an error
try:
    import tkinter
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        # Student management UI components
        # ...
    # Student management methods
    # ...
if __name__ == "__main__":
    create_database()  # Ensure the database and tables are created and migrations are applied
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()