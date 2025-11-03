'''
Implements the GUI for user interaction using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import requests
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.show_button = tk.Button(master, text="Show Students", command=self.show_students)
        self.show_button.pack()
        self.students_list = tk.Listbox(master)
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
    def show_students(self):
        self.students_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            for student in students:
                self.students_list.insert(tk.END, student['name'])
        else:
            messagebox.showerror("Error", "Failed to retrieve students.")
def run_gui():
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()