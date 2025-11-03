'''
Graphical User Interface for the Student application using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import requests
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.label = tk.Label(root, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.fetch_button = tk.Button(root, text="Fetch Students", command=self.fetch_students)
        self.fetch_button.pack()
        self.students_list = tk.Listbox(root)
        self.students_list.pack()
    def add_student(self):
        name = self.entry.get()
        if name:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully!")
                self.entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Warning", "Name cannot be empty.")
    def fetch_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.students_list.delete(0, tk.END)
            for student in students:
                self.students_list.insert(tk.END, student['name'])
        else:
            messagebox.showerror("Error", "Failed to fetch students.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()