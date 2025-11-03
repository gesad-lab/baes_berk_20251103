'''
Main entry point for the application.
'''
import tkinter as tk
from tkinter import messagebox
import requests
# Check if tkinter is available
try:
    import tkinter
except ImportError:
    raise ImportError("tkinter module is not installed. Please install it to run the application.")
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.label = tk.Label(root, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.label_email = tk.Label(root, text="Enter Student Email:")  # Added email label
        self.label_email.pack()
        self.entry_email = tk.Entry(root)  # Added email entry
        self.entry_email.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.list_button = tk.Button(root, text="List Students", command=self.list_students)
        self.list_button.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.entry_email.get()  # Get email input
        if name and email:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Updated to include email
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")
    def list_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            student_list = "\n".join([f"{student['id']}: {student['name']} - {student['email']}" for student in students])  # Display email
            messagebox.showinfo("Student List", student_list)
        else:
            messagebox.showerror("Error", "Failed to retrieve students.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()