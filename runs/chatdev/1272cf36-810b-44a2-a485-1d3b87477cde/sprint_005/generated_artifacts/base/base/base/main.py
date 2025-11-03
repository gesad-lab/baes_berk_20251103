'''
Graphical User Interface for the Student application.
'''
import tkinter as tk
from tkinter import messagebox
import requests
# Ensure tkinter is installed
try:
    import tkinter
except ImportError:
    raise ImportError("tkinter is not installed. Please install it to run the application.")
class StudentApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Registration")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Student Name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        tk.Label(self.root, text="Email:").pack()  # New label for email
        self.email_entry = tk.Entry(self.root)  # New entry for email
        self.email_entry.pack()
        tk.Button(self.root, text="Add Student", command=self.add_student).pack()
    def add_student(self):
        '''
        Add a student by sending a POST request to the FastAPI backend.
        '''
        name = self.name_entry.get()
        email = self.email_entry.get()  # Get email input
        if name and email:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
            if response.status_code == 201:
                messagebox.showinfo("Success", "Student added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")
    def run(self):
        '''
        Run the Tkinter main loop.
        '''
        self.root.mainloop()
if __name__ == "__main__":
    app = StudentApp()
    app.run()