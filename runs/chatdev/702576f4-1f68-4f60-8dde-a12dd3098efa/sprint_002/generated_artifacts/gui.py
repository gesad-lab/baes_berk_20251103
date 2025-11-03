'''
Implements the GUI using Tkinter for user interaction.
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
        self.email_label = tk.Label(self.root, text="Enter Student Email:")  # New label for email
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)  # New entry for email
        self.email_entry.pack()
        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.students_button = tk.Button(self.root, text="Show Students", command=self.show_students)
        self.students_button.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.email_entry.get()  # Get email input
        if name and email:  # Check both name and email
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Send email
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")  # Updated warning message
    def show_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            student_list = "\n".join([f"{student['id']}: {student['name']} ({student['email']})" for student in students])  # Updated to include email
            messagebox.showinfo("Students", student_list)
        else:
            messagebox.showerror("Error", "Failed to retrieve students.")
    def run(self):
        self.root.mainloop()