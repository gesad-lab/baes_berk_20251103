'''
Graphical User Interface for the Student application.
'''
import tkinter as tk
from tkinter import messagebox
import requests
class StudentApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Management")
        self.label = tk.Label(self.root, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.root.mainloop()
    def add_student(self):
        '''
        Add a student by sending a POST request to the FastAPI application.
        '''
        name = self.entry.get()
        if name:
            try:
                response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
                if response.status_code == 201:  # Check for 201 Created
                    messagebox.showinfo("Success", "Student added successfully!")
                    self.entry.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Failed to add student.")
            except requests.exceptions.RequestException as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter a name.")
if __name__ == "__main__":
    StudentApp()