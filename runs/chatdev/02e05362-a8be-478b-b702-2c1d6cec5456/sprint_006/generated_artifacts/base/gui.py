'''
Graphical User Interface for the Student application.
'''
try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    raise ImportError("tkinter module is not available. Please install it to run the GUI.")
import requests
class StudentApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Management")
        # Student Section
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
        # Course Section
        self.course_name_label = tk.Label(self.root, text="Course Name:")
        self.course_name_label.pack()
        self.course_name_entry = tk.Entry(self.root)
        self.course_name_entry.pack()
        self.course_level_label = tk.Label(self.root, text="Course Level:")
        self.course_level_label.pack()
        self.course_level_entry = tk.Entry(self.root)
        self.course_level_entry.pack()
        self.add_course_button = tk.Button(self.root, text="Add Course", command=self.add_course)
        self.add_course_button.pack()
        self.view_courses_button = tk.Button(self.root, text="View Courses", command=self.view_courses)
        self.view_courses_button.pack()
        self.courses_list = tk.Listbox(self.root)
        self.courses_list.pack()
        # Teacher Section
        self.teacher_name_label = tk.Label(self.root, text="Teacher Name:")
        self.teacher_name_label.pack()
        self.teacher_name_entry = tk.Entry(self.root)
        self.teacher_name_entry.pack()
        self.teacher_email_label = tk.Label(self.root, text="Teacher Email:")
        self.teacher_email_label.pack()
        self.teacher_email_entry = tk.Entry(self.root)
        self.teacher_email_entry.pack()
        self.add_teacher_button = tk.Button(self.root, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack()
        self.view_teachers_button = tk.Button(self.root, text="View Teachers", command=self.view_teachers)
        self.view_teachers_button.pack()
        self.teachers_list = tk.Listbox(self.root)
        self.teachers_list.pack()
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
    def add_course(self):
        name = self.course_name_entry.get()
        level = self.course_level_entry.get()
        if name and level:
            response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
            if response.status_code == 201:
                messagebox.showinfo("Success", "Course added successfully!")
                self.course_name_entry.delete(0, tk.END)
                self.course_level_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Failed to add course.")
        else:
            messagebox.showwarning("Warning", "Please enter both course name and level.")
    def view_courses(self):
        self.courses_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/courses/")
        if response.status_code == 200:
            courses = response.json()
            for course in courses:
                self.courses_list.insert(tk.END, f"{course['name']} - {course['level']}")
    def add_teacher(self):  # New method to add Teacher
        name = self.teacher_name_entry.get()
        email = self.teacher_email_entry.get()
        if name and email:
            response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
            if response.status_code == 201:
                messagebox.showinfo("Success", "Teacher added successfully!")
                self.teacher_name_entry.delete(0, tk.END)
                self.teacher_email_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Failed to add teacher.")
        else:
            messagebox.showwarning("Warning", "Please enter both name and email.")
    def view_teachers(self):  # New method to view Teachers
        self.teachers_list.delete(0, tk.END)
        response = requests.get("http://127.0.0.1:8000/teachers/")
        if response.status_code == 200:
            teachers = response.json()
            for teacher in teachers:
                self.teachers_list.insert(tk.END, f"{teacher['name']} - {teacher['email']}")
    def run(self):
        self.root.mainloop()