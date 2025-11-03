'''
Implements the GUI using Tkinter for user interaction.
'''
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not installed. Please install it to use the GUI.")
    exit(1)
from database import create_database, run_migrations
from gui import StudentApp
if __name__ == "__main__":
    create_database()  # Create the database if it doesn't exist
    run_migrations()  # Run migrations before starting the GUI
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()