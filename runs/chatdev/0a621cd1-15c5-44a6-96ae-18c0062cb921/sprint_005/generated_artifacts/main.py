'''
Main GUI for the Student Management application.
'''
import tkinter as tk
import requests
# Check if tkinter is available
try:
    import tkinter
except ImportError:
    raise ImportError("Tkinter is not installed. Please install it to run the application.")
class StudentApp:
    def __init__(self, master):
        self.master = master
        master.title("Student Management")
        # Student Entry
        self.label = tk.Label(master, text="Enter Student Name:")
        self.label.pack()
        self.entry = tk.Entry(master)
        self.entry.pack()
        self.label_email = tk.Label(master, text="Enter Student Email:")
        self.label_email.pack()
        self.entry_email = tk.Entry(master)
        self.entry_email.pack()
        # Course Entry
        self.label_course_name = tk.Label(master, text="Enter Course Name:")
        self.label_course_name.pack()
        self.entry_course_name = tk.Entry(master)
        self.entry_course_name.pack()
        self.label_course_level = tk.Label(master, text="Enter Course Level:")
        self.label_course_level.pack()
        self.entry_course_level = tk.Entry(master)
        self.entry_course_level.pack()
        # Teacher Entry
        self.label_teacher_name = tk.Label(master, text="Enter Teacher Name:")
        self.label_teacher_name.pack()
        self.entry_teacher_name = tk.Entry(master)
        self.entry_teacher_name.pack()
        self.label_teacher_email = tk.Label(master, text="Enter Teacher Email:")
        self.label_teacher_email.pack()
        self.entry_teacher_email = tk.Entry(master)
        self.entry_teacher_email.pack()
        self.submit_student_button = tk.Button(master, text="Add Student", command=self.add_student)
        self.submit_student_button.pack()
        self.submit_course_button = tk.Button(master, text="Add Course", command=self.add_course)
        self.submit_course_button.pack()
        self.submit_teacher_button = tk.Button(master, text="Add Teacher", command=self.add_teacher)
        self.submit_teacher_button.pack()
        self.view_button = tk.Button(master, text="View Students", command=self.view_students)
        self.view_button.pack()
        self.view_courses_button = tk.Button(master, text="View Courses", command=self.view_courses)
        self.view_courses_button.pack()
        self.view_teachers_button = tk.Button(master, text="View Teachers", command=self.view_teachers)
        self.view_teachers_button.pack()
        self.output = tk.Text(master)
        self.output.pack()
    def add_student(self):
        name = self.entry.get()
        email = self.entry_email.get()
        if not name.strip() or not email.strip():
            self.output.insert(tk.END, "Error: Name and Email cannot be empty.\n")
            return
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output.insert(tk.END, "Error adding student.\n")
    def add_course(self):
        name = self.entry_course_name.get()
        level = self.entry_course_level.get()
        if not name.strip() or not level.strip():
            self.output.insert(tk.END, "Error: Course Name and Level cannot be empty.\n")
            return
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Course: {response.json()}\n")
        else:
            self.output.insert(tk.END, "Error adding course.\n")
    def add_teacher(self):
        name = self.entry_teacher_name.get()
        email = self.entry_teacher_email.get()
        if not name.strip() or not email.strip():
            self.output.insert(tk.END, "Error: Teacher Name and Email cannot be empty.\n")
            return
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Teacher: {response.json()}\n")
        else:
            self.output.insert(tk.END, "Error adding teacher.\n")
    def view_students(self):
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")
        else:
            self.output.insert(tk.END, "Error retrieving students.\n")
    def view_courses(self):
        response = requests.get("http://127.0.0.1:8000/courses/")
        if response.status_code == 200:
            courses = response.json()
            self.output.delete(1.0, tk.END)
            for course in courses:
                self.output.insert(tk.END, f"ID: {course['id']}, Name: {course['name']}, Level: {course['level']}\n")
        else:
            self.output.insert(tk.END, "Error retrieving courses.\n")
    def view_teachers(self):
        response = requests.get("http://127.0.0.1:8000/teachers/")
        if response.status_code == 200:
            teachers = response.json()
            self.output.delete(1.0, tk.END)
            for teacher in teachers:
                self.output.insert(tk.END, f"ID: {teacher['id']}, Name: {teacher['name']}, Email: {teacher['email']}\n")
        else:
            self.output.insert(tk.END, "Error retrieving teachers.\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()