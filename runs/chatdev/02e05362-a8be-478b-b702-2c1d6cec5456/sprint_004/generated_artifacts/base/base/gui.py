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
        self.name_label = tk.Label(self.root, text="Student Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        self.email_label = tk.Label(self.root, text="Student Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()
        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.view_button = tk.Button(self.root, text="View Students", command=self.view_students)
        self.view_button.pack()
        self.students_list = tk.Listbox(self.root)
        self.students_list.pack()
    def add_student(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        if name and email:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
            if response.status_code == 201:  # Changed to 201 for created
                messagebox.showinfo("Success", "Student added successfully!")
                self.name_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Warning", "Please enter both name and email.")
    def view_students(self):
        self.students_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            for student in students:
                self.students_list.insert(tk.END, f"{student['name']} - {student['email']}")
    def run(self):
        self.root.mainloop()