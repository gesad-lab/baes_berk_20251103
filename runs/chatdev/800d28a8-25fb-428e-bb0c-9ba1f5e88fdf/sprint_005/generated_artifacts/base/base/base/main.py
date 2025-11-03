'''
Implements the GUI using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import requests
# Check if tkinter is available, if not, raise an error
try:
    import tkinter
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the GUI.")
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.email_label = tk.Label(root, text="Student Email:")  # Added email label
        self.email_label.pack()
        self.email_entry = tk.Entry(root)  # Added email entry
        self.email_entry.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.show_button = tk.Button(root, text="Show Students", command=self.show_students)
        self.show_button.pack()
        self.students_list = tk.Listbox(root)
        self.students_list.pack()
    def add_student(self):
        name = self.name_entry.get()
        email = self.email_entry.get()  # Get email from entry
        if name and email:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Send email
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully!")
                self.name_entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)  # Clear email entry
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Input Error", "Please enter both student name and email.")
    def show_students(self):
        self.students_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            for student in students:
                self.students_list.insert(tk.END, f"{student['id']}: {student['name']} - {student['email']}")  # Show email
        else:
            messagebox.showerror("Error", "Failed to retrieve students.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()