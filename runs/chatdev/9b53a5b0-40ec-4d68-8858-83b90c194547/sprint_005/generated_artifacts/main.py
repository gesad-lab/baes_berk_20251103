'''
Implements a simple GUI using Tkinter to interact with the FastAPI backend.
'''
import tkinter as tk
import requests
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        # Student components
        self.label_name = tk.Label(master, text="Enter Student Name:")
        self.label_name.pack()
        self.entry_name = tk.Entry(master)
        self.entry_name.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(master)
        self.entry_email.pack()
        self.add_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.add_button.pack()
        self.view_button = tk.Button(master, text="View Students", command=self.view_students)
        self.view_button.pack()
        # Course components
        self.label_course_name = tk.Label(master, text="Enter Course Name:")
        self.label_course_name.pack()
        self.entry_course_name = tk.Entry(master)
        self.entry_course_name.pack()
        self.label_course_level = tk.Label(master, text="Enter Course Level:")
        self.label_course_level.pack()
        self.entry_course_level = tk.Entry(master)
        self.entry_course_level.pack()
        self.add_course_button = tk.Button(master, text="Add Course", command=self.add_course)
        self.add_course_button.pack()
        self.view_courses_button = tk.Button(master, text="View Courses", command=self.view_courses)
        self.view_courses_button.pack()
        # Teacher components
        self.label_teacher_name = tk.Label(master, text="Enter Teacher Name:")
        self.label_teacher_name.pack()
        self.entry_teacher_name = tk.Entry(master)
        self.entry_teacher_name.pack()
        self.label_teacher_email = tk.Label(master, text="Enter Teacher Email:")
        self.label_teacher_email.pack()
        self.entry_teacher_email = tk.Entry(master)
        self.entry_teacher_email.pack()
        self.add_teacher_button = tk.Button(master, text="Add Teacher", command=self.add_teacher)
        self.add_teacher_button.pack()
        self.view_teachers_button = tk.Button(master, text="View Teachers", command=self.view_teachers)
        self.view_teachers_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {name}, Email: {email}\n")
        else:
            self.output.insert(tk.END, "Failed to add student.\n")
    def view_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")
        else:
            self.output.insert(tk.END, "Failed to retrieve students.\n")
    def add_course(self):
        name = self.entry_course_name.get()
        level = self.entry_course_level.get()
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Course: {name}, Level: {level}\n")
        else:
            self.output.insert(tk.END, "Failed to add course.\n")
    def view_courses(self):
        response = requests.get("http://127.0.0.1:8000/courses/")
        if response.status_code == 200:
            courses = response.json()
            self.output.delete(1.0, tk.END)
            for course in courses:
                self.output.insert(tk.END, f"ID: {course['id']}, Name: {course['name']}, Level: {course['level']}\n")
        else:
            self.output.insert(tk.END, "Failed to retrieve courses.\n")
    def add_teacher(self):
        name = self.entry_teacher_name.get()
        email = self.entry_teacher_email.get()
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Teacher: {name}, Email: {email}\n")
        else:
            self.output.insert(tk.END, "Failed to add teacher.\n")
    def view_teachers(self):
        response = requests.get("http://127.0.0.1:8000/teachers/")
        if response.status_code == 200:
            teachers = response.json()
            self.output.delete(1.0, tk.END)
            for teacher in teachers:
                self.output.insert(tk.END, f"ID: {teacher['id']}, Name: {teacher['name']}, Email: {teacher['email']}\n")
        else:
            self.output.insert(tk.END, "Failed to retrieve teachers.\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()