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
        # Student Section
        self.label = tk.Label(self.root, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.email_label = tk.Label(self.root, text="Enter Student Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack()
        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.students_button = tk.Button(self.root, text="Show Students", command=self.show_students)
        self.students_button.pack()
        # Course Section
        self.course_label = tk.Label(self.root, text="Enter Course Name:")
        self.course_label.pack()
        self.course_entry = tk.Entry(self.root)
        self.course_entry.pack()
        self.level_label = tk.Label(self.root, text="Enter Course Level:")
        self.level_label.pack()
        self.level_entry = tk.Entry(self.root)
        self.level_entry.pack()
        self.teacher_id_label = tk.Label(self.root, text="Enter Teacher ID for Course:")
        self.teacher_id_label.pack()
        self.teacher_id_entry = tk.Entry(self.root)
        self.teacher_id_entry.pack()
        self.add_course_button = tk.Button(self.root, text="Add Course", command=self.add_course)
        self.add_course_button.pack()
        self.courses_button = tk.Button(self.root, text="Show Courses", command=self.show_courses)
        self.courses_button.pack()
        # Teacher Section
        self.teacher_label = tk.Label(self.root, text="Enter Teacher Name:")
        self.teacher_label.pack()
        self.teacher_entry = tk.Entry(self.root)
        self.teacher_entry.pack()
        self.teacher_email_label = tk.Label(self.root, text="Enter Teacher Email:")
        self.teacher_email_label.pack()
        self.teacher_email_entry = tk.Entry(self.root)
        self.teacher_email_entry.pack()
        self.add_teacher_button = tk.Button(self.root, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack()
        self.teachers_button = tk.Button(self.root, text="Show Teachers", command=self.show_teachers)
        self.teachers_button.pack()
        # Enrollment Section
        self.enroll_label = tk.Label(self.root, text="Enroll Student in Course (Student ID, Course ID):")
        self.enroll_label.pack()
        self.student_id_entry = tk.Entry(self.root)
        self.student_id_entry.pack()
        self.course_id_entry = tk.Entry(self.root)
        self.course_id_entry.pack()
        self.enroll_button = tk.Button(self.root, text="Enroll", command=self.enroll_student)
        self.enroll_button.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.email_entry.get()
        if name and email:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")
    def show_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            student_list = "\n".join([f"{student['id']}: {student['name']} ({student['email']})" for student in students])
            messagebox.showinfo("Students", student_list)
        else:
            messagebox.showerror("Error", "Failed to retrieve students.")
    def add_course(self):
        name = self.course_entry.get()
        level = self.level_entry.get()
        teacher_id = self.teacher_id_entry.get()
        if name and level and teacher_id:
            response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level, "teacher_id": teacher_id})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Course added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add course.")
        else:
            messagebox.showwarning("Input Error", "Please enter course name, level, and teacher ID.")
    def show_courses(self):
        response = requests.get("http://127.0.0.1:8000/courses/")
        if response.status_code == 200:
            courses = response.json()
            course_list = "\n".join([f"{course['id']}: {course['name']} (Level: {course['level']}, Teacher ID: {course['teacher_id']})" for course in courses])
            messagebox.showinfo("Courses", course_list)
        else:
            messagebox.showerror("Error", "Failed to retrieve courses.")
    def add_teacher(self):
        name = self.teacher_entry.get()
        email = self.teacher_email_entry.get()
        if name and email:
            response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Teacher added successfully!")
            else:
                messagebox.showerror("Error", "Failed to add teacher.")
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")
    def show_teachers(self):
        response = requests.get("http://127.0.0.1:8000/teachers/")
        if response.status_code == 200:
            teachers = response.json()
            teacher_list = "\n".join([f"{teacher['id']}: {teacher['name']} ({teacher['email']})" for teacher in teachers])
            messagebox.showinfo("Teachers", teacher_list)
        else:
            messagebox.showerror("Error", "Failed to retrieve teachers.")
    def enroll_student(self):
        student_id = self.student_id_entry.get()
        course_id = self.course_id_entry.get()
        if student_id and course_id:
            response = requests.post(f"http://127.0.0.1:8000/students/{student_id}/courses/{course_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student enrolled in course successfully!")
            else:
                messagebox.showerror("Error", "Failed to enroll student.")
        else:
            messagebox.showwarning("Input Error", "Please enter both Student ID and Course ID.")
    def run(self):
        self.root.mainloop()