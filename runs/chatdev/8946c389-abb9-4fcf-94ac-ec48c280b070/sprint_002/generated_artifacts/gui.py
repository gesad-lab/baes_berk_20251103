'''
Implements the GUI for user interaction using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import requests
# Check if tkinter is available
try:
    import tkinter
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(master)
        self.entry_email.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.show_button = tk.Button(master, text="Show Students", command=self.show_students)
        self.show_button.pack()
        self.students_list = tk.Listbox(master)
        self.students_list.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.entry_email.get()  # Get email input
        if name and email:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully!")
                self.entry.delete(0, tk.END)
                self.entry_email.delete(0, tk.END)  # Clear email entry
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Warning", "Name and email cannot be empty.")
    def show_students(self):
        self.students_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            for student in students:
                self.students_list.insert(tk.END, f"{student['name']} - {student['email']}")  # Show email
        else:
            messagebox.showerror("Error", "Failed to retrieve students.")
def run_gui():
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()