'''
Implements the GUI using Tkinter for managing Students and Courses.
'''
import tkinter as tk
import requests
from tkinter import messagebox
# Check if tkinter is available
try:
    import tkinter
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run this application.")
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        # Student section
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(root)
        self.name_entry.pack()
        self.email_label = tk.Label(root, text="Student Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(root)
        self.email_entry.pack()
        self.add_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.show_button = tk.Button(root, text="Show Students", command=self.show_students)
        self.show_button.pack()
        self.students_list = tk.Listbox(root)
        self.students_list.pack()
        # Course section
        self.course_name_label = tk.Label(root, text="Course Name:")
        self.course_name_label.pack()
        self.course_name_entry = tk.Entry(root)
        self.course_name_entry.pack()
        self.course_level_label = tk.Label(root, text="Course Level:")
        self.course_level_label.pack()
        self.course_level_entry = tk.Entry(root)
        self.course_level_entry.pack()
        self.add_course_button = tk.Button(root, text="Add Course", command=self.add_course)
        self.add_course_button.pack()
        self.show_courses_button = tk.Button(root, text="Show Courses", command=self.show_courses)
        self.show_courses_button.pack()
        self.courses_list = tk.Listbox(root)
        self.courses_list.pack()
    def add_student(self):
        name = self.name_entry.get()
        email = self.email_entry.get()  # Get email from entry
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.name_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)  # Clear email entry
            self.show_students()
        else:
            messagebox.showerror("Error", "Failed to add student: " + response.text)
    def show_students(self):
        self.students_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/students/")
        students = response.json()
        for student in students:
            self.students_list.insert(tk.END, f"{student['name']} - {student['email']}")  # Show email
    def add_course(self):
        name = self.course_name_entry.get()
        level = self.course_level_entry.get()  # Get level from entry
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
        if response.status_code == 200:
            self.course_name_entry.delete(0, tk.END)
            self.course_level_entry.delete(0, tk.END)  # Clear level entry
            self.show_courses()
        else:
            messagebox.showerror("Error", "Failed to add course: " + response.text)
    def show_courses(self):
        self.courses_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/courses/")
        courses = response.json()
        for course in courses:
            self.courses_list.insert(tk.END, f"{course['name']} - {course['level']}")  # Show course level
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()