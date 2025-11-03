'''
Implements a simple GUI for interacting with the FastAPI application.
'''
try:
    import tkinter as tk
    import requests
    import re  # Importing regex for email validation
    class StudentApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Student Management")
            # Student input section
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
            self.fetch_button = tk.Button(root, text="Fetch Students", command=self.fetch_students)
            self.fetch_button.pack()
            # Course input section
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
            # Teacher input section
            self.teacher_name_label = tk.Label(root, text="Teacher Name:")
            self.teacher_name_label.pack()
            self.teacher_name_entry = tk.Entry(root)
            self.teacher_name_entry.pack()
            self.teacher_email_label = tk.Label(root, text="Teacher Email:")
            self.teacher_email_label.pack()
            self.teacher_email_entry = tk.Entry(root)
            self.teacher_email_entry.pack()
            self.add_teacher_button = tk.Button(root, text="Add Teacher", command=self.add_teacher)
            self.add_teacher_button.pack()
            self.output_text = tk.Text(root)
            self.output_text.pack()
        def add_student(self):
            name = self.name_entry.get()
            email = self.email_entry.get()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                self.output_text.insert(tk.END, "Invalid email format\n")
                return
            response = requests.post("http://127.0.0.1:8000/students", json={"name": name, "email": email})
            if response.status_code == 200:
                self.output_text.insert(tk.END, f"Added: {name}, Email: {email}\n")
            else:
                self.output_text.insert(tk.END, "Failed to add student\n")
        def fetch_students(self):
            response = requests.get("http://127.0.0.1:8000/students")
            if response.status_code == 200:
                students = response.json()
                self.output_text.delete(1.0, tk.END)
                for student in students:
                    self.output_text.insert(tk.END, f"Student ID: {student['id']}, Name: {student['name']}, Email: {student['email']}\n")
            else:
                self.output_text.insert(tk.END, "Failed to fetch students\n")
        def add_course(self):
            course_name = self.course_name_entry.get()
            course_level = self.course_level_entry.get()
            response = requests.post("http://127.0.0.1:8000/courses", json={"name": course_name, "level": course_level})
            if response.status_code == 200:
                self.output_text.insert(tk.END, f"Added Course: {course_name}, Level: {course_level}\n")
            else:
                self.output_text.insert(tk.END, "Failed to add course\n")
        def add_teacher(self):
            name = self.teacher_name_entry.get()
            email = self.teacher_email_entry.get()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                self.output_text.insert(tk.END, "Invalid email format\n")
                return
            response = requests.post("http://127.0.0.1:8000/teachers", json={"name": name, "email": email})
            if response.status_code == 200:
                self.output_text.insert(tk.END, f"Added Teacher: {name}, Email: {email}\n")
            else:
                self.output_text.insert(tk.END, "Failed to add teacher\n")
    if __name__ == "__main__":
        root = tk.Tk()
        app = StudentApp(root)
        root.mainloop()
except ImportError:
    print("tkinter is not installed. Please install it to run the GUI application.")