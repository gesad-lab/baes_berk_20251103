'''
Implements the graphical user interface for student registration and course creation.
'''
import tkinter as tk
from tkinter import messagebox
import requests
import re  # Import regex for email validation
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration")
        # Student Registration
        self.label_name = tk.Label(root, text="Enter Student Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(root)
        self.entry_name.pack()
        self.label_email = tk.Label(root, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()
        self.submit_button = tk.Button(root, text="Submit Student", command=self.submit_student)
        self.submit_button.pack()
        # Course Registration
        self.label_course_name = tk.Label(root, text="Enter Course Name:")
        self.label_course_name.pack()
        self.entry_course_name = tk.Entry(root)
        self.entry_course_name.pack()
        self.label_course_level = tk.Label(root, text="Enter Course Level:")
        self.label_course_level.pack()
        self.entry_course_level = tk.Entry(root)
        self.entry_course_level.pack()
        self.submit_course_button = tk.Button(root, text="Submit Course", command=self.submit_course)
        self.submit_course_button.pack()
    def is_valid_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)
    def submit_student(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        if name and email:
            if self.is_valid_email(email):
                response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
                if response.status_code == 201:
                    messagebox.showinfo("Success", "Student registered successfully!")
                else:
                    messagebox.showerror("Error", "Failed to register student.")
            else:
                messagebox.showwarning("Warning", "Invalid email format.")
        else:
            messagebox.showwarning("Warning", "Name and email cannot be empty.")
    def submit_course(self):
        course_name = self.entry_course_name.get()
        course_level = self.entry_course_level.get()
        if course_name and course_level:
            response = requests.post("http://127.0.0.1:8000/courses/", json={"name": course_name, "level": course_level})
            if response.status_code == 201:
                messagebox.showinfo("Success", "Course registered successfully!")
            else:
                messagebox.showerror("Error", "Failed to register course.")
        else:
            messagebox.showwarning("Warning", "Course name and level cannot be empty.")