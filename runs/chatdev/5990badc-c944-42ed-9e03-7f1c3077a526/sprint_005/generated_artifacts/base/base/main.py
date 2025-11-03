'''
Main entry point for the Student application.
'''
# Import necessary modules and start the application
from gui import StudentApp
import tkinter as tk
from database import upgrade_database  # Import the upgrade_database function
if __name__ == "__main__":
    upgrade_database()  # Ensure the database is upgraded with the Course table
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()