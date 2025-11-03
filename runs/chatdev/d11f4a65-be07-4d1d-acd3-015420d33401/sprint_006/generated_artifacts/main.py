'''
Implements a simple GUI using Tkinter to interact with the API.
'''
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not installed. Please install it using your package manager.")
    print("For example, on Ubuntu, you can run: sudo apt-get install python3-tk")
    exit(1)
import requests
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.label = tk.Label(root, text="Student Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.email_label = tk.Label(root, text="Student Email:")  # Added email label
        self.email_label.pack()  # Added email label
        self.email_entry = tk.Entry(root)  # Added email entry
        self.email_entry.pack()  # Added email entry
        self.submit_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.submit_button.pack()
        self.output = tk.Text(root, height=10, width=30)
        self.output.pack()
    def add_student(self):
        '''
        Sends a request to add a new student to the API.
        '''
        name = self.entry.get()
        email = self.email_entry.get()  # Get email input
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})  # Send email in request
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()['name']} with Email: {response.json()['email']}\n")
        else:
            self.output.insert(tk.END, "Failed to add student.\n")
class CourseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Management")
        self.label = tk.Label(root, text="Course Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.level_label = tk.Label(root, text="Course Level:")
        self.level_label.pack()
        self.level_entry = tk.Entry(root)
        self.level_entry.pack()
        self.teacher_label = tk.Label(root, text="Teacher ID:")  # Added teacher label
        self.teacher_label.pack()  # Added teacher label
        self.teacher_entry = tk.Entry(root)  # Added teacher entry
        self.teacher_entry.pack()  # Added teacher entry
        self.submit_button = tk.Button(root, text="Add Course", command=self.add_course)
        self.submit_button.pack()
        self.output = tk.Text(root, height=10, width=30)
        self.output.pack()
    def add_course(self):
        '''
        Sends a request to add a new course to the API.
        '''
        name = self.entry.get()
        level = self.level_entry.get()
        teacher_id = self.teacher_entry.get()  # Get teacher ID input
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level, "teacher_id": teacher_id})  # Send teacher_id in request
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Course: {response.json()['name']} with Level: {response.json()['level']} and Teacher ID: {response.json()['teacher_id']}\n")
        else:
            self.output.insert(tk.END, "Failed to add course.\n")
class TeacherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Management")
        self.label = tk.Label(root, text="Teacher Name:")
        self.label.pack()
        self.entry = tk.Entry(root)
        self.entry.pack()
        self.email_label = tk.Label(root, text="Teacher Email:")  # Added email label
        self.email_label.pack()  # Added email label
        self.email_entry = tk.Entry(root)  # Added email entry
        self.email_entry.pack()  # Added email entry
        self.submit_button = tk.Button(root, text="Add Teacher", command=self.add_teacher)
        self.submit_button.pack()
        self.output = tk.Text(root, height=10, width=30)
        self.output.pack()
    def add_teacher(self):
        '''
        Sends a request to add a new teacher to the API.
        '''
        name = self.entry.get()
        email = self.email_entry.get()  # Get email input
        response = requests.post("http://127.0.0.1:8000/teachers/", json={"name": name, "email": email})  # Send email in request
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Teacher: {response.json()['name']} with Email: {response.json()['email']}\n")
        else:
            self.output.insert(tk.END, "Failed to add teacher.\n")
if __name__ == "__main__":
    root = tk.Tk()
    student_app = StudentApp(root)
    course_app = CourseApp(root)
    teacher_app = TeacherApp(root)  # Added TeacherApp instance
    root.mainloop()