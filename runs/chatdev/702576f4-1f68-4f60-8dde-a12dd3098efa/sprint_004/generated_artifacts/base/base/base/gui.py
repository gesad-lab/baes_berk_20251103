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
        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.students_button = tk.Button(self.root, text="Show Students", command=self.show_students)
        self.students_button.pack()
    def add_student(self):
        name = self.entry.get()
        if name:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Input Error", "Please enter a name.")
    def show_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            student_list = "\n".join([f"{student['id']}: {student['name']}" for student in students])
            messagebox.showinfo("Students", student_list)
        else:
            messagebox.showerror("Error", "Failed to retrieve students.")
    def run(self):
        self.root.mainloop()