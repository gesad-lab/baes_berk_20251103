'''
Graphical User Interface for the Student application.
'''
import tkinter as tk
from tkinter import messagebox
import requests
# Check if tkinter is available
try:
    import tkinter
except ImportError:
    raise ImportError("tkinter module is not available. Please install it to run this application.")
class StudentApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Registration")
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Student Name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        tk.Label(self.root, text="Email:").pack()  # New label for email
        self.email_entry = tk.Entry(self.root)  # New entry for email
        self.email_entry.pack()
        tk.Label(self.root, text="Course Name:").pack()  # New label for course name
        self.course_name_entry = tk.Entry(self.root)  # New entry for course name
        self.course_name_entry.pack()
        tk.Label(self.root, text="Course Level:").pack()  # New label for course level
        self.course_level_entry = tk.Entry(self.root)  # New entry for course level
        self.course_level_entry.pack()
        tk.Label(self.root, text="Student ID:").pack()  # New label for student ID
        self.student_id_entry = tk.Entry(self.root)  # New entry for student ID
        self.student_id_entry.pack()
        tk.Label(self.root, text="Course ID:").pack()  # New label for course ID
        self.course_id_entry = tk.Entry(self.root)  # New entry for course ID
        self.course_id_entry.pack()
        tk.Button(self.root, text="Add Student", command=self.add_student).pack()
        tk.Button(self.root, text="Add Course", command=self.add_course).pack()
        tk.Button(self.root, text="Enroll Student in Course", command=self.enroll_student).pack()
    def add_student(self):
        name = self.name_entry.get()
        email = self.email_entry.get()  # Get email input
        if name and email:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
            if response.status_code == 201:
                messagebox.showinfo("Success", "Student added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")
    def add_course(self):
        course_name = self.course_name_entry.get()  # Use new entry for course name
        course_level = self.course_level_entry.get()  # Use new entry for course level
        if course_name and course_level:
            response = requests.post("http://127.0.0.1:8000/courses/", json={"name": course_name, "level": course_level})
            if response.status_code == 201:
                messagebox.showinfo("Success", "Course added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add course.")
        else:
            messagebox.showwarning("Input Error", "Please enter both course name and level.")
    def enroll_student(self):
        student_id = self.student_id_entry.get()  # Use new entry for student ID
        course_id = self.course_id_entry.get()  # Use new entry for course ID
        if student_id.isdigit() and course_id.isdigit():
            response = requests.post(f"http://127.0.0.1:8000/students/{student_id}/courses/{course_id}")
            if response.status_code == 204:
                messagebox.showinfo("Success", "Student enrolled in course successfully!")
            else:
                messagebox.showerror("Error", response.json().get("detail", "Failed to enroll student in course."))
        else:
            messagebox.showwarning("Input Error", "Please enter valid student and course IDs.")
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = StudentApp()
    app.run()