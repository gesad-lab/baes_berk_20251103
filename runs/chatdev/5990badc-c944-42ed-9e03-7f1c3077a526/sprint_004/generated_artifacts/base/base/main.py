'''
Main entry point for the Student application.
'''
# Import necessary modules and start the application
from gui import StudentApp
import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()