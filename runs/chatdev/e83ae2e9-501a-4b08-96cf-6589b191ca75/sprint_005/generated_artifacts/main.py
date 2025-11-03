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
        # Student input fields
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.email_label = tk.Label(master, text="Enter Student Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(master)
        self.email_entry.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.view_button = tk.Button(master, text="View Students", command=self.view_students)
        self.view_button.pack()
        self.students_list = tk.Listbox(master)
        self.students_list.pack()
        # Course input fields
        self.course_name_label = tk.Label(master, text="Enter Course Name:")
        self.course_name_label.pack()
        self.course_name_entry = tk.Entry(master)
        self.course_name_entry.pack()
        self.course_level_label = tk.Label(master, text="Enter Course Level:")
        self.course_level_label.pack()
        self.course_level_entry = tk.Entry(master)
        self.course_level_entry.pack()
        self.add_course_button = tk.Button(master, text="Add Course", command=self.add_course)
        self.add_course_button.pack()
        self.courses_list = tk.Listbox(master)
        self.courses_list.pack()
        self.view_courses_button = tk.Button(master, text="View Courses", command=self.view_courses)
        self.view_courses_button.pack()
        self.enroll_button = tk.Button(master, text="Enroll Student in Course", command=self.enroll_student)
        self.enroll_button.pack()
        # Teacher input fields
        self.teacher_name_label = tk.Label(master, text="Enter Teacher Name:")
        self.teacher_name_label.pack()
        self.teacher_name_entry = tk.Entry(master)
        self.teacher_name_entry.pack()
        self.teacher_email_label = tk.Label(master, text="Enter Teacher Email:")
        self.teacher_email_label.pack()
        self.teacher_email_entry = tk.Entry(master)
        self.teacher_email_entry.pack()
        self.add_teacher_button = tk.Button(master, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack()
        self.teachers_list = tk.Listbox(master)
        self.teachers_list.pack()
        self.view_teachers_button = tk.Button(master, text="View Teachers", command=self.view_teachers)
        self.view_teachers_button.pack()
    def add_student(self):
        '''
        Add a new student to the database.
        '''
        name = self.entry.get()
        email = self.email_entry.get()
        if name and email:
            response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student added successfully!")
                self.entry.delete(0, tk.END)
                self.email_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", response.json().get("detail", "Failed to add student."))
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")
    def view_students(self):
        '''
        View the list of students from the database.
        '''
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.students_list.delete(0, tk.END)
            for student in students:
                self.students_list.insert(tk.END, f"{student['id']} - {student['name']} - {student['email']}")
        else:
            messagebox.showerror("Error", "Failed to retrieve students.")
    def add_course(self):
        '''
        Add a new course to the database.
        '''
        name = self.course_name_entry.get()
        level = self.course_level_entry.get()
        if name and level:
            response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Course added successfully!")
                self.course_name_entry.delete(0, tk.END)
                self.course_level_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", response.json().get("detail", "Failed to add course."))
        else:
            messagebox.showwarning("Input Error", "Please enter both course name and level.")
    def view_courses(self):
        '''
        View the list of courses from the database.
        '''
        response = requests.get("http://127.0.0.1:8000/courses/")
        if response.status_code == 200:
            courses = response.json()
            self.courses_list.delete(0, tk.END)
            for course in courses:
                self.courses_list.insert(tk.END, f"{course['id']} - {course['name']} - {course['level']}")
        else:
            messagebox.showerror("Error", "Failed to retrieve courses.")
    def enroll_student(self):
        '''
        Enroll a selected student in a selected course.
        '''
        selected_student = self.students_list.curselection()
        selected_course = self.courses_list.curselection()
        if selected_student and selected_course:
            student_info = self.students_list.get(selected_student[0]).split(" - ")
            course_info = self.courses_list.get(selected_course[0]).split(" - ")
            student_id = int(student_info[0])  # Get the actual student ID
            course_id = int(course_info[0])  # Get the actual course ID
            response = requests.post(f"http://127.0.0.1:8000/students/{student_id}/courses/{course_id}")
            if response.status_code == 200:
                messagebox.showinfo("Success", "Student enrolled in course successfully!")
            else:
                messagebox.showerror("Error", response.json().get("detail", "Failed to enroll student."))
        else:
            messagebox.showwarning("Selection Error", "Please select both a student and a course.")
    def add_teacher(self):
        '''
        Add a new teacher to the database.
        '''
        name = self.teacher_name_entry.get()
        email = self.teacher_email_entry.get()
        if name and email:
            response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
            if response.status_code == 200:
                messagebox.showinfo("Success", "Teacher added successfully!")
                self.teacher_name_entry.delete(0, tk.END)
                self.teacher_email_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", response.json().get("detail", "Failed to add teacher."))
        else:
            messagebox.showwarning("Input Error", "Please enter both name and email.")
    def view_teachers(self):
        '''
        View the list of teachers from the database.
        '''
        response = requests.get("http://127.0.0.1:8000/teachers/")
        if response.status_code == 200:
            teachers = response.json()
            self.teachers_list.delete(0, tk.END)
            for teacher in teachers:
                self.teachers_list.insert(tk.END, f"{teacher['id']} - {teacher['name']} - {teacher['email']}")
        else:
            messagebox.showerror("Error", "Failed to retrieve teachers.")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()