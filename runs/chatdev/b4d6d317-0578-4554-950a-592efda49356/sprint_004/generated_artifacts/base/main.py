'''
Implements the graphical user interface using Tkinter.
'''
import tkinter as tk
import requests
try:
    import tkinter as tk
except ImportError:
    print("Tkinter is not installed. Please install it to run the application.")
    exit()
class StudentApp:
    def __init__(self, root):
        '''
        Initialize the GUI application.
        Parameters:
        - root: tk.Tk - The root window for the application.
        '''
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
        self.submit_button = tk.Button(root, text="Add Student", command=self.add_student)
        self.submit_button.pack()
        self.students_button = tk.Button(root, text="Show Students", command=self.show_students)
        self.students_button.pack()
        self.output = tk.Text(root, height=10, width=50)
        self.output.pack()
        # Course section
        self.course_name_label = tk.Label(root, text="Course Name:")
        self.course_name_label.pack()
        self.course_name_entry = tk.Entry(root)
        self.course_name_entry.pack()
        self.course_level_label = tk.Label(root, text="Course Level:")
        self.course_level_label.pack()
        self.course_level_entry = tk.Entry(root)
        self.course_level_entry.pack()
        self.submit_course_button = tk.Button(root, text="Add Course", command=self.add_course)
        self.submit_course_button.pack()
        self.courses_button = tk.Button(root, text="Show Courses", command=self.show_courses)
        self.courses_button.pack()
    def add_student(self):
        '''
        Add a new student by sending a POST request to the API.
        '''
        name = self.name_entry.get()
        email = self.email_entry.get()
        response = requests.post("http://127.0.0.1:8000/students/", json={"name": name, "email": email})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Student: {response.json()}\n")
        else:
            self.output.insert(tk.END, "Error adding student\n")
    def show_students(self):
        '''
        Show the list of students by sending a GET request to the API.
        '''
        response = requests.get("http://127.0.0.1:8000/students/")
        if response.status_code == 200:
            students = response.json()
            self.output.delete(1.0, tk.END)
            for student in students:
                self.output.insert(tk.END, f"ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")
        else:
            self.output.insert(tk.END, "Error fetching students\n")
    def add_course(self):
        '''
        Add a new course by sending a POST request to the API.
        '''
        name = self.course_name_entry.get()
        level = self.course_level_entry.get()
        response = requests.post("http://127.0.0.1:8000/courses/", json={"name": name, "level": level})
        if response.status_code == 200:
            self.output.insert(tk.END, f"Added Course: {response.json()}\n")
        else:
            self.output.insert(tk.END, "Error adding course\n")
    def show_courses(self):
        '''
        Show the list of courses by sending a GET request to the API.
        '''
        response = requests.get("http://127.0.0.1:8000/courses/")
        if response.status_code == 200:
            courses = response.json()
            self.output.delete(1.0, tk.END)
            for course in courses:
                self.output.insert(tk.END, f"ID: {course['id']}, Name: {course['name']}, Level: {course['level']}\n")
        else:
            self.output.insert(tk.END, "Error fetching courses\n")
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()