'''
Implements the GUI for the application using Tkinter.
'''
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not installed. Please install it to run the GUI.")
    exit(1)
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
        self.email_label = tk.Label(master, text="Enter Student Email:")  # Added email label
        self.email_label.pack()
        self.email_entry = tk.Entry(master)  # Added email entry
        self.email_entry.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.view_button = tk.Button(master, text="View Students", command=self.view_students)
        self.view_button.pack()
        self.students_list = tk.Listbox(master)
        self.students_list.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.email_entry.get()  # Get email from entry
        if name and email:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Updated to send email
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully!")
                self.entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)  # Clear email entry
            else:
                messagebox.showerror("Error", response.json().get("detail", "Failed to add student."))
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")
    def view_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.students_list.delete(0, tk.END)
            for student in students:
                self.students_list.insert(tk.END, f"{student['name']} - {student['email']}")  # Display email
        else:
            messagebox.showerror("Error", "Failed to retrieve students.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()